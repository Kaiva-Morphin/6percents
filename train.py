import DataModule
import NNModule

import time
import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

net = NNModule.Net()

try:
    net.load_state_dict(torch.load("./backups/NN_MODEL_SAVE_LATEST"))
    net.eval()
except:
    print("cant find neural network save!")



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

batch_size = 8

train_data = DataModule.Train_Data()

net.train()
try:
    while True:
        for epoch in range(300):  # loop over the dataset multiple times
            running_loss = 0.0
            for i in range(5):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = train_data.get_random_batch(batch_size)
                #print(inputs.shape)
                
                #inputs = np.swapaxes(inputs, 1, 2)
                #inputs = np.swapaxes(inputs, 2, 3)
                
                #print(inputs.shape)
                inputs, labels = torch.tensor(inputs), torch.tensor(labels)
                print(inputs.shape)
                # zero the parameter gradients
                optimizer.zero_grad()

                # forward + backward + optimize
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
                
                # print statistics
                running_loss += loss.item()
                if i % 5 == 4: 
                    print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 5}')
                    running_loss = 0.0
        try:
            os.rename("./backups/NN_MODEL_SAVE_LATEST", f"./backups/NN_MODEL_SAVE_{time.time()}")
        except:
            pass
        torch.save(net.state_dict(), "./backups/NN_MODEL_SAVE_LATEST")
        print("saved!")    
except KeyboardInterrupt:
    try:
        os.rename("./backups/NN_MODEL_SAVE_LATEST", f"./backups/NN_MODEL_SAVE_{time.time()}")
    except:
            pass
    torch.save(net.state_dict(), "./backups/NN_MODEL_SAVE_LATEST")
    print("saved!")
print('Finished Training')