import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(3, 6, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 8, 5),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(26912, 4098),
            nn.ReLU(),
            nn.Linear(4098, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 19),
        )
    
    def __call__(self, x):
        return self.layers(x)


