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

# def traininh_step(model, batch, criterion, optimizer):
#     inputs, lebels = batch
#     otuputs = model(input)
#     loss = criterion(outputs, lebel)

#     if loss.item() > 100 or torch .isnan(loss):
#         breakponi()

#     loss.backward()
#     optimizee.step()
# print()



















































































