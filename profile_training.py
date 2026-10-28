import torch
import torch.nn as nn

import cProfile
import pstats


model = nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

x = torch.randn(100, 10)
y = torch.randn(100, 1)


def train():
    for step in range(100):
        optimizer.zero_grad()

        prediction = model(x)
        loss = criterion(prediction, y)

        loss.backward()
        optimizer.step()


profiler = cProfile.Profile()

profiler.enable()
train()
profiler.disable()

pstats.Stats(profiler).sort_stats("cumtime").print_stats(15)