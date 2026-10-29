import csv
import json
import tempfile
from dataclasses import dataclass
from pathlib import Path


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