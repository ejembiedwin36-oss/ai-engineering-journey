import torch
import torch.nn as nn


model = nn.Linear(10, 1)
criterion = nn.MSELoss()

x = torch.randn(100, 10)
y = torch.randn(100, 1)

prediction = model(x)
loss = criterion(prediction, y)

loss.backward()

breakpoint()

print("Training step completed")