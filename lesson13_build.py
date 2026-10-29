import csv
import json
import tempfile
from dataclasses import dataclass
from pathlib import Path
import random
from itertools import islice
import math
from collections import Counter

import operator
import time
import tracemalloc



@dataclass(frozen=True)
class Record:
    features: tuple[float, ...]
    label: int


def row_to_record(row, names, label_field="label"):
    if label_field not in row:
        raise ValueError(
            f"row has no {label_field!r} field: {row}"
        )

    if set(row) != {*names, label_field}:
        raise ValueError(
            f"row fields {list(row)} do not match "
            f"{[*names, label_field]}"
        )

    return Record(
        tuple(float(row[name]) for name in names),
        int(row[label_field]),
    )


def load_records(path, label_field="label"):
    path = Path(path)

    if path.suffix == ".json":
        rows = json.loads(
            path.read_text(encoding="utf-8")
        )

    elif path.suffix == ".csv":
        with path.open(
            newline="",
            encoding="utf-8"
        ) as fh:
            rows = list(csv.DictReader(fh))

    else:
        raise ValueError(
            f"unsupported file type: {path.suffix!r}"
        )

    if not rows:
        return []

    names = [
        key
        for key in rows[0]
        if key != label_field
    ]

    return [
        row_to_record(row, names, label_field)
        for row in rows
    ]


with tempfile.TemporaryDirectory() as tmp:
    csv_path = Path(tmp) / "data.csv"

    csv_path.write_text(
        "x1,x2,label\n"
        "1.5,60,1\n"
        "1.8,82.5,0\n",
        encoding="utf-8",
    )

    json_path = Path(tmp) / "data.json"

    json_path.write_text(
        '[{"x1": 1.5, "x2": 60, "label": 1}]',
        encoding="utf-8",
    )

    print(load_records(csv_path))
    print(load_records(json_path))



# ============================================================
# STEP 2: SEEDED TRAIN / TEST SPLIT
# ============================================================

def train_test_split(items, test_fraction=0.2, seed=0):
    if not 0.0 < test_fraction < 1.0:
        raise ValueError(
            f"test_fraction must be between 0 and 1, got {test_fraction}"
        )

    if len(items) < 2:
        raise ValueError(
            f"need at least 2 items to split, got {len(items)}"
        )

    order = list(range(len(items)))

    random.Random(seed).shuffle(order)

    n_test = min(
        max(1, round(len(items) * test_fraction)),
        len(items) - 1,
    )

    test = [items[i] for i in order[:n_test]]
    train = [items[i] for i in order[n_test:]]

    return train, test


items = list(range(10))

print(train_test_split(items, seed=1))
print(
    train_test_split(items, seed=1)
    == train_test_split(items, seed=1)
)
print(train_test_split(items, seed=2)[1])
print(items)


# ============================================================
# STEP 3: MINI-BATCH GENERATOR
# ============================================================

def batches(items, batch_size, drop_last=False):
    if batch_size < 1:
        raise ValueError(
            f"batch_size must be at least 1, got {batch_size}"
        )

    return _batch_iter(
        iter(items),
        batch_size,
        drop_last,
    )


def _batch_iter(iterator, batch_size, drop_last):
    while True:
        batch = list(
            islice(iterator, batch_size)
        )

        if not batch or (
            drop_last
            and len(batch) < batch_size
        ):
            return

        yield batch


print(list(batches(range(10), 4)))
print(
    list(
        batches(
            range(10),
            4,
            drop_last=True,
        )
    )
)

squares = (
    i * i
    for i in range(7)
)

print(
    [
        len(batch)
        for batch in batches(squares, 3)
    ]
)

for epoch in range(2):
    sizes = [
        len(batch)
        for batch in batches(range(10), 4)
    ]

    print(
        f"epoch {epoch}: {sizes}"
    )


    # ============================================================
# STEP 4: PURE-PYTHON VECTOR MATH
# ============================================================

def dot(a, b):
    return sum(
        x * y
        for x, y in zip(a, b, strict=True)
    )


def mean(values):
    if not values:
        raise ValueError(
            "mean() needs at least one value"
        )

    return sum(values) / len(values)


def std(values):
    mu = mean(values)

    return math.sqrt(
        sum(
            (value - mu) ** 2
            for value in values
        )
        / len(values)
    )


print(dot([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]))
print(mean([2.0, 4.0, 6.0]))
print(std([2.0, 4.0, 6.0]))


# ============================================================
# STEP 5: STANDARDIZE FEATURES
# ============================================================

def make_standardizer(rows):
    columns = list(zip(*rows))

    means = [
        mean(column)
        for column in columns
    ]

    stds = [
        std(column)
        for column in columns
    ]

    scales = [
        s if s > 0 else 1.0
        for s in stds
    ]

    def standardize(row):
        return [
            (value - mu) / scale
            for value, mu, scale
            in zip(row, means, scales, strict=True)
        ]

    return standardize


train_rows = [
    (1.0, 100.0),
    (2.0, 300.0),
    (3.0, 500.0),
]

standardize = make_standardizer(train_rows)

print([
    [
        round(value, 3)
        for value in standardize(row)
    ]
    for row in train_rows
])

# ============================================================
# STEP 5: COMPLETE RUN
# ============================================================

def fit_centroids(labelled_batches):
    sums = {}
    counts = Counter()

    for batch in labelled_batches:
        for row, label in batch:
            previous = sums.get(
                label,
                [0.0] * len(row)
            )

            sums[label] = [
                old + value
                for old, value
                in zip(previous, row, strict=True)
            ]

            counts[label] += 1

    return {
        label: [
            value / counts[label]
            for value in sums[label]
        ]
        for label in sorted(sums)
    }


def squared_distance(a, b):
    difference = [
        x - y
        for x, y in zip(a, b, strict=True)
    ]

    return dot(difference, difference)


def predict(centroids, row):
    return min(
        centroids,
        key=lambda label: squared_distance(
            row,
            centroids[label]
        ),
    )


def accuracy(centroids, pairs):
    correct = sum(
        predict(centroids, row) == label
        for row, label in pairs
    )

    return correct / len(pairs)


training_data = [
    ([1.0, 1.0], 0),
    ([1.2, 0.8], 0),
    ([4.0, 4.0], 1),
    ([4.2, 3.8], 1),
]

centroids = fit_centroids(
    batches(training_data, 2)
)

print(centroids)
print(
    predict(
        centroids,
        [1.1, 1.0]
    )
)

print(
    accuracy(
        centroids,
        training_data
    )
)

# ============================================================
# STEP 6: SPEED AND MEMORY
# ============================================================

def dot_index_loop(a, b):
    total = 0.0

    for i in range(len(a)):
        total += a[i] * b[i]

    return total


def dot_map(a, b):
    return sum(map(operator.mul, a, b))


def best_time(fn, *args, repeat=5):
    times = []

    for _ in range(repeat):
        start = time.perf_counter()
        fn(*args)
        times.append(
            time.perf_counter() - start
        )

    return min(times)


def peak_bytes(fn):
    tracemalloc.start()

    try:
        fn()
        return tracemalloc.get_traced_memory()[1]

    finally:
        tracemalloc.stop()


def sum_squares_list(n):
    return sum([
        i * i
        for i in range(n)
    ])


def sum_squares_generator(n):
    return sum(
        i * i
        for i in range(n)
    )


rng = random.Random(7)

a = [
    rng.random()
    for _ in range(100_000)
]

b = [
    rng.random()
    for _ in range(100_000)
]

print(
    "index loop:",
    round(best_time(dot_index_loop, a, b) * 1000, 2),
    "ms",
)

print(
    "generator:",
    round(best_time(dot, a, b) * 1000, 2),
    "ms",
)

print(
    "map:",
    round(best_time(dot_map, a, b) * 1000, 2),
    "ms",
)

print(
    "list peak:",
    peak_bytes(
        lambda: sum_squares_list(100_000)
    ),
)

print(
    "generator peak:",
    peak_bytes(
        lambda: sum_squares_generator(100_000)
    ),
)