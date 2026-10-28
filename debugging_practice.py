import torch

def debug_print(name, tensor):

    print(
    f"{name}: shape={tensor.shape} dtype={tensor.dtype}, "
    f"device={tensor.device}, "
    f"min={tensor.min().item():.4f}, max={tensor.max().item():.4f}, "
    f"mean={tensor.mean().item():.4f}, "
    f"has_nan={tensor.isnan().any().item()}"
    )

numbers = torch.tensor([1.0, 2.0, 3.0])
debug_print("numbers", numbers)

x = torch.tensor([10.0, 20.0, 30.0])

breakpoint()

print("program continued")


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"

)

logger = logging.getLogger(__name__)

logger.info("training started")
logger.warning("Loss is increasing")
logger.error("NaN detected")

import time
class Timer:

    def __init__(self, name=""):
        self.name = name 

    def __enter__(self):
            self.start = time.perf_counter()
            return self

    def __exit__(self, *args):
        elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] {elapsed:.4f}s")

with Timer("test"):
    time.sleep(2)


import tracemalloc

tracemalloc.start()
data = [i for i in range(100000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:5]:
    print(stat)

import torch 

bad_numbers = torch.tensor([1.0, float("nan"), 3.0])

debug_print("bad_numbers", bad_numbers)


def check_data_leakage(train_ids, test_ids):
    overlap = set(train_ids) & set(test_ids)

    if overlap:
        print(f"DATA LEAKAGE: {len(overlap)} samples overlap")
        print("Overlapping IDs:", overlap)
        return True

    print("No data leakage")
    return False

train_ids = [1, 2, 3, 4]
test_ids = [4, 5, 6]

check_data_leakage(train_ids, test_ids)

def check_devices(model, *tensors):
    model_device = next(model.parameters()).device
    print(f"Model device: {model_device}")

    for i, tensor in enumerate(tensors):
        print(f"Tensor {i} device: {tensor.device}")

        if tensor.device != model_device:
            print(
                f"WARNING: tensor {i} is on {tensor.device}, "
                f"but model is on {model_device}"
            )

model = torch.nn.Linear(3, 1)
sample = torch.tensor([[1.0, 2.0, 3.0]])

check_devices(model, sample)