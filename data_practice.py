import random

examples = [{"id": i, "text": f"Review {i}", "label": i % 2} for i in range(20)]

shuffled = examples.copy()
random.Random(42).shuffle(shuffled)

train = shuffled[:14]
validation = shuffled[14:17]
test = shuffled[17:]

print("Training examples:", len(train))
print("Validation examples:", len(validation))
print("Test examples:", len(test))
print("Total:", len(train) + len(validation) + len(test))


train_ids = {row["id"] for row in train}
validation_ids = {row["id"] for row in validation}
test_ids = {row["id"] for row in test}

assert train_ids.isdisjoint(validation_ids)
assert train_ids.isdisjoint(test_ids)
assert validation_ids.isdisjoint(test_ids)

print("No examples are shared between the groups.")

import json

with open("train.json", "w") as file:
    json.dump(train, file, indent=2)

print("Saved training examples to train.json")

with open("train.json", "r") as file:
    loaded_train = json.load(file)

assert loaded_train == train

print("Loaded examples:", len(loaded_train))
print("Loaded data matches the original training data.")


import csv

with open("train.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "text", "label"])
    writer.writeheader()
    writer.writerows(train)

print("Saved training examples to train.csv")

with open("train.csv", "r", newline="") as file:
    loaded_csv = list(csv.DictReader(file))

print("Loaded CSV examples:", len(loaded_csv))
print("First CSV example:", loaded_csv[0])


for row in loaded_csv:
    row["id"] = int(row["id"])
    row["label"] = int(row["label"])

assert loaded_csv == train

print("CSV data matches the original training data.")


from datasets import load_dataset

dataset = load_dataset("csv", data_files="train.csv", split="train")

print("Dataset rows:", len(dataset))
print("First example:", dataset[0])
print("Column types:", dataset.features)

dataset.to_parquet("train.parquet")

restored = load_dataset(
    "parquet", data_files="train.parquet", split="train"
)

assert restored.to_list() == dataset.to_list()
print("Parquet data matches the original dataset.")


from pathlib import Path

for filename in ["train.csv", "train.json", "train.parquet"]:
    size = Path(filename).stat().st_size
    print(f"{filename}: {size} bytes")

from datasets import Dataset

full_dataset = Dataset.from_list(examples)

first = full_dataset.train_test_split(test_size=0.30, seed=42)
remaining = first["test"].train_test_split(test_size=0.50, seed=42)

hf_train = first["train"]
hf_validation = remaining["train"]
hf_test = remaining["test"]

assert [len(hf_train), len(hf_validation), len(hf_test)] == [14, 3, 3]

repeated = full_dataset.train_test_split(test_size=0.30, seed=42)
assert first["train"].to_list() == repeated["train"].to_list()

print("Library split: 14 training, 3 validation, 3 test.")
print("Repeated split produced the same training examples.")


hub_dataset = load_dataset("lhoestq/demo1", split="train")

print("Downloaded rows:", len(hub_dataset))
print("First downloaded example:", hub_dataset[0])

cached_dataset = load_dataset("lhoestq/demo1", split="train")

assert cached_dataset.to_list() == hub_dataset.to_list()
print("Second load matches the first.")
print("Cache files:", cached_dataset.cache_files)



streamed_dataset = load_dataset(
    "lhoestq/demo1",
    split="train",
    streaming=True,
)

print("Streaming type:", type(streamed_dataset).__name__)

for number, example in enumerate(streamed_dataset.take(2), start=1):
    print(f"Streamed example {number}: {example['id']}")

    



"""
Run:

.venv/bin/python data_practice.py

"""
