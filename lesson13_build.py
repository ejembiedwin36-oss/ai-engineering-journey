import csv
import json
import tempfile
from dataclasses import dataclass
from pathlib import Path
import random



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