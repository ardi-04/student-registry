import torch
import torch.nn as nn

X = torch.tensor([1,2,3,4,5,6,7,8,9,10], dtype=torch.float32).unsqueeze(1)
y = torch.tensor([0,0,0,0,1,1,1,1,1,1], dtype=torch.float32).unsqueeze(1)

class SimpleNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(1,8)
        self.layer2 = nn.Linear(8,4)
        self.layer3 = nn.Linear(4,1)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)  # no activation on output layer
        return x



model = SimpleNetwork()
#loss function
criterion =  nn.MSELoss()
#Optimezer
Optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


for i in range(1000):
    predictions = model(X)

    loss = criterion(predictions, y)

    Optimizer.zero_grad() #clears old gradients before calculating new ones
    loss.backward() #calculates all gradients automatically

    Optimizer.step() #updates all weights

    if i  % 100 == 0:
        print(f"Step {i}:  Loss {loss.item():.4f}")
    

test_input = torch.tensor([[11.0]])
prediction = model(test_input)
print(f"Prediction for 11 hours studied: {prediction.item():.2f}")