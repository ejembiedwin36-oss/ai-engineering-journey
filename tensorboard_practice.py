from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("runs/overfitting")

train_losses = [10, 8, 6, 4, 3, 2, 1]
val_losses = [10, 8, 7, 6, 7, 8, 9]

for epoch in range(len(train_losses)):
    writer.add_scalar("loss/train", train_losses[epoch], epoch)
    writer.add_scalar("loss/validation", val_losses[epoch], epoch)

writer.close()

print("Overfitting example created")