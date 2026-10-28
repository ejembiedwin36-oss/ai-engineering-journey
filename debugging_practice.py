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