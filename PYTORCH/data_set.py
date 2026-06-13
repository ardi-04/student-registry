import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# Download MNIST dataset
train_dataset = torchvision.datasets.MNIST(
    root='./data', 
    train=True,
    transform=transforms.ToTensor(),
    download=True
)

test_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=False,
    transform=transforms.ToTensor()
)

# Data loaders
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)