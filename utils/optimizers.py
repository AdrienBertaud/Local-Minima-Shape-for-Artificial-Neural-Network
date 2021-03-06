# -*- coding: utf-8 -*-
import torch

def load_optimizer(net, optimizer_name, learning_rate):

    print("optimizer name = ", optimizer_name)
    print("learning rate = ", learning_rate)

    if optimizer_name == 'gd':
        return torch.optim.SGD(net.parameters(), lr=learning_rate)
    elif optimizer_name == 'sgd':
        return torch.optim.SGD(net.parameters(), lr=learning_rate)
    elif optimizer_name == 'adam':
        return torch.optim.Adam(net.parameters(), lr=learning_rate)
    elif optimizer_name == 'adagrad':
         return torch.optim.Adagrad(net.parameters(), lr=learning_rate)
    elif optimizer_name == 'lbfgs':
         return torch.optim.LBFGS(net.parameters(), lr=learning_rate)
    else:
        raise ValueError('optimizer_name %s is not supported'%(optimizer_name))