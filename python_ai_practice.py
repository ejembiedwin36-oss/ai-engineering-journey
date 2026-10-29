"""Lesson 13: Python for AI Engineering practice.

This file restores the concepts practiced so far. Expensive demonstrations are
kept behind functions so running the file stays lightweight on shared lab PCs.
"""

from collections import Counter, defaultdict, deque
from collections.abc import Iterable, Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field
from itertools import chain, islice, product
from pathlib import Path
import csv
import json
import os
import sys
import tempfile
import time


# ============================================================
# 1. VALUES, COLLECTIONS, AND UNPACKING
# ============================================================

weights = [0.5, -1.2, 3.0]
alias = weights
alias[0] = 99.0

independent = list(weights)
independent[1] = 0.0

grid = [[0] * 3] * 2
grid[0][0] = 1

safe_grid = [[0] * 3 for _ in range(2)]
safe_grid[0][0] = 1

shape = (32, 784)
batch_size, n_features = shape

first, *middle, last = [1, 2, 3, 4, 5]

x, y = 1.0, 3.0
x, y = y, x

config = {"lr": 0.01, "epochs": 5}

tokens = ["the", "cat", "sat", "on", "the", "mat"]
vocab = set(tokens)

loss = 0.123456
lr = 0.01

sentence_tokens = ["<s>", "the", "cat", "sat", "on", "the", "mat", "</s>"]


# ============================================================
# 2. COMPREHENSIONS
# ============================================================

scores = [0.91, 0.42, 0.77, 0.15, 0.66]
labels = [1 if score >= 0.5 else 0 for score in scores]
high = [score for score in scores if score > 0.6]
squares = {i: i * i for i in range(4)}
lengths = {len(word) for word in ["a", "bb", "cc", "ddd"]}
sum_sq = sum(score * score for score in scores)

matrix = [[1, 2, 3], [4, 5, 6]]
flat = [value for row in matrix for value in row]
transposed = [list(column) for column in zip(*matrix)]


# ============================================================
# 3. FUNCTIONS, ARGUMENTS, AND CLOSURES
# ============================================================


def clip(value, low=0.0, high=1.0):
    return max(low, min(high, value))


def train(data, *, lr=0.01, epochs=3):
    return f"{len(data)} samples, lr={lr}, epochs={epochs}"


def make_scaler(factor):
    def scale(values):
        return [value * factor for value in values]

    return scale


to_percent = make_scaler(100)


def add_bad(item, bucket=[]):
    """Intentional example of the mutable-default trap."""
    bucket.append(item)
    return bucket


def add_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


# ============================================================
# 4. CLASSES AND DATACLASSES
# ============================================================


@dataclass(frozen=True)
class Example:
    features: tuple[float, ...]
    label: int


@dataclass
class TrainConfig:
    lr: float = 0.01
    epochs: int = 5
    hidden: list[int] = field(default_factory=lambda: [64, 32])

    def describe(self):
        return f"lr={self.lr} epochs={self.epochs} hidden={self.hidden}"


class SquaresDataset:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError(index)
        return index, index * index


# ============================================================
# 5. ITERATORS AND GENERATORS
# ============================================================


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def read_rows(path):
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split(",")
        for line in fh:
            yield dict(zip(header, line.rstrip("\n").split(",")))


def memory_demo(limit=100_000):
    """Compare list and generator object sizes without stressing the lab PC.

    The official lesson uses 1_000_000 values. We already observed that larger
    run during the lesson; this smaller default is safer for repeated runs.
    """
    as_list = [i * i for i in range(limit)]
    as_generator = (i * i for i in range(limit))
    return sys.getsizeof(as_list), sys.getsizeof(as_generator)


# ============================================================
# 6. CONTEXT MANAGERS AND EXCEPTIONS
# ============================================================


@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {(time.perf_counter() - start) * 1000:.1f} ms")


def parse_label(text):
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"label must be an integer, got {text!r}") from None


# ============================================================
# 7. TYPE HINTS, MODULES, AND MAIN GUARD
# ============================================================


def mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("mean() needs at least one value")
    return sum(values) / len(values)


def count_tokens(docs: Iterable[str]) -> int:
    return sum(len(doc.split()) for doc in docs)


# ============================================================
# 8. FILES, JSON, CSV, AND SORTING
# ============================================================

review_rows = [
    {"text": "great movie", "label": 1, "score": 0.93},
    {"text": "boring plot", "label": 0, "score": 0.12},
    {"text": "fine acting", "label": 1, "score": 0.58},
]


def json_csv_demo():
    with tempfile.TemporaryDirectory() as tmp:
        json_path = Path(tmp) / "reviews.json"
        json_path.write_text(json.dumps(review_rows, indent=2), encoding="utf-8")
        from_json = json.loads(json_path.read_text(encoding="utf-8"))

        csv_path = Path(tmp) / "reviews.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=["text", "label", "score"])
            writer.writeheader()
            writer.writerows(review_rows)

        with csv_path.open(newline="", encoding="utf-8") as fh:
            from_csv = list(csv.DictReader(fh))

        typed_rows = [
            {
                "text": row["text"],
                "label": int(row["label"]),
                "score": float(row["score"]),
            }
            for row in from_csv
        ]

    by_score = sorted(review_rows, key=lambda row: row["score"], reverse=True)
    return from_json, from_csv, typed_rows, by_score


# ============================================================
# 9. COUNTING, GROUPING, AND ITERATOR TOOLS
# ============================================================


def iterator_tools_demo():
    animal_labels = ["cat", "dog", "cat", "bird", "cat", "dog"]

    counts = Counter(animal_labels)

    positions = defaultdict(list)
    for index, label in enumerate(animal_labels):
        positions[label].append(index)

    recent = deque(maxlen=3)
    for recent_loss in [2.0, 1.5, 1.2, 1.1, 0.9]:
        recent.append(recent_loss)

    combinations = list(product([0.1, 0.01], [16, 32]))
    joined = list(chain([1, 2], [3], [4, 5]))
    sliced = list(islice(range(100), 5, 10))

    return (
        counts.most_common(2),
        dict(positions),
        list(recent),
        combinations,
        joined,
        sliced,
    )


# ============================================================
# LIGHTWEIGHT CHECK
# ============================================================


def main() -> None:
    print("Lesson 13 practice restored")
    print(mean([1.0, 2.0, 4.0]))
    print(count_tokens(["the cat sat", "on the mat"]))

    from_json, from_csv, typed_rows, by_score = json_csv_demo()
    print(from_json == review_rows)
    print(from_csv[0])
    print(typed_rows == review_rows)
    print([row["text"] for row in by_score])

    print(iterator_tools_demo())


if __name__ == "__main__":
    main()
