import torch
a = torch.tensor([[1.,1.,1.,0.],
                  [1.,1.,0.,0.],
                  [1.,0.,1.,1.],
                  [0.,0.,1.,1.]])
b = torch.tensor([[0.8,0.1,0.1],
                  [0.8, 0.1,0.1],
                  [0.1,0.8,0.1],
                  [0.1,0.8,0.1]])
print(torch.mm(a, b))