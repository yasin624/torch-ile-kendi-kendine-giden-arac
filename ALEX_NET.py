import torch,cv2,os,time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# GPU kullanımı
device=torch.device(0)


class NET(nn.Module):
    def __init__(self):
        super(). __init__()
        self.conv1=nn.Conv2d(1,64,5)
        self.conv2=nn.Conv2d(64,128,5)
        self.conv3=nn.Conv2d(128,64,5)
        
        x=torch.randn(86,86).view(-1,1,86,86)
        
        self.boyut=None
        self.uzunluk(x)
        
        self.fkl1=nn.Linear(self.boyut,512)
        self.fkl2=nn.Linear(512,3)
    def uzunluk(self,x):
        
        x=F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x=F.max_pool2d(F.relu(self.conv2(x)),(2,2))
        x=F.max_pool2d(F.relu(self.conv3(x)),(2,2))
        
        if self.boyut is None:
            self.boyut=x[0].shape[0]*x[0].shape[1]*x[0].shape[2]
        return x
    def forward(self,x):
        x=self.uzunluk(x)
        x=x.view(-1,self.boyut)
        
        x=F.relu(self.fkl1(x))
        x=F.softmax(self.fkl2(x))
        
        return x

