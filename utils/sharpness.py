# -*- coding: utf-8 -*-
import utils.linalg
from importlib import reload
reload(utils.linalg)
from utils.linalg import eigen_hessian


def eval_sharpness(net, criterion, optimizer, data_loader):

    n_iters=20
    tol=1e-4

    print('Compute sharpness :')
    sharpness = eigen_hessian(net, criterion, data_loader, \
                      n_iters=n_iters, tol=tol, verbose=True)
    print('Sharpness is %.2e\n'%(sharpness))
    return sharpness


def get_sharpness_theorical_limit(learning_rate):
    '''
    return theorical limit of sharpness depending on given learning rate
    '''
    return 2/learning_rate