import torch.nn as nn
import torch.nn.functional as F

class purple_teletubbies(nn.Module):
    def __init__(self):
        super(purple_teletubbies, self).__init__()
        self.fc1 = nn.Linear(307, 400)
        self.bn1 = nn.BatchNorm1d(400)
        self.fc2 = nn.Linear(707, 300)
        self.bn2 = nn.BatchNorm1d(300)
        self.fc3 = nn.Linear(1007, 200)
        self.bn3 = nn.BatchNorm1d(200)
        self.fc4 = nn.Linear(1207, 1)
    
    def forward(self, x, is_train=False):
        x1 = self.bn1(F.relu(self.fc1(x)))
        if is_train:
            x1 = F.dropout(x1, 0.3)
        x2 = self.bn2(F.relu(self.fc2(torch.cat([x, x1], 1))))
        if is_train:
            x2 = F.dropout(x2, 0.3)
        x3 = self.bn3(F.relu(self.fc3(torch.cat([x, x1, x2], 1))))
        if is_train:
            x3 = F.dropout(x3, 0.3)
        x4 = self.fc4(torch.cat([x, x1, x2, x3], 1))
        return x4