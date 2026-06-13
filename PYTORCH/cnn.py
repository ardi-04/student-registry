import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transform


train_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=True,
    transform=transform.ToTensor(),
    download=True
)

test_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=True,
    transform=transform.ToTensor()
)


train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3) #looks at the small patches of image  # 1 input channel, 32 filters, 3x3 patch
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.pool = nn.MaxPool2d(2) # shrinks the image by taking the maximum value in each 2x2 area.
        self.fc1 = nn.Linear(1600, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1) # flattens from 3D to 2D so Linear layers can process it.
        x = self.relu(self.fc1(x))
        x = self.fc2(x)

        return x

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(f"Using {device}")

model = CNN().to(device) #moves model to GPU. Your RTX 3050 will train this much faster than CPU.
criterion = nn.CrossEntropyLoss() #eplaces MSELoss. Used for classification with multiple classes (digits 0-9). MSELoss was for regression (predicting a number).
optimizer = torch.optim.Adam(model.parameters(), lr=0.001) #smarter version of SGD. Adjusts learning rate automatically. Almost always better than plain SGD.

eporchs = 5

for epoch in range(eporchs):
    model.train()
    running_loss = 0.0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        output = model(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.4f}")


model.eval() #switches to evaluation mode. Opposite of model.train().
correct = 0
total = 0

with torch.no_grad(): # tells PyTorch don't track gradients. We're not training, just predicting. Saves memory and speeds things up.
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _,predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Test Accuracy: {100 * correct / total:.2f}%")