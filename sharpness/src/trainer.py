import time
import torch

def train(model, criterion, optimizer, optimizerName, dataloader, batch_size, n_iters=50000, verbose=True, logFrequency=200):

    print("optimizer.type = ", optimizerName)

    model.train()
    acc_avg, loss_avg = 0, 0

    since = time.time()
    for iter_now in range(n_iters):

        if optimizerName == 'lbfgs':

            batch_size_used = 0

            def closure():
                if torch.is_grad_enabled():
                    optimizer.zero_grad()
                loss,acc = compute_minibatch_gradient(model, criterion, dataloader, batch_size)
                return loss

            optimizer.step(closure)
            loss,acc = compute_minibatch_gradient(model, criterion, dataloader, dataloader.batch_size)
        else:
            optimizer.zero_grad()

            # if optimizerName == 'gd':
            #     batch_size_used = dataloader.n_samples
            # else:
            #     batch_size_used = batch_size

            loss,acc = compute_minibatch_gradient(model, criterion, dataloader, batch_size)
            optimizer.step()

        acc_avg = 0.9 * acc_avg + 0.1 * acc if acc_avg > 0 else acc
        loss_avg = 0.9 * loss_avg + 0.1 * loss if loss_avg > 0 else loss

        if iter_now%logFrequency == 0 and verbose:
            now = time.time()
            print('%d/%d, took %.0f seconds, train_loss: %.1e, train_acc: %.2f'%(
                    iter_now+1, n_iters, now-since, loss_avg, acc_avg))
            since = time.time()

def compute_minibatch_gradient(model, criterion, dataloader, batch_size):
    loss,acc = 0,0

    #inputs, targets = inputs.cuda(), targets.cuda()
    inputs,targets = next(dataloader)

    logits = model(inputs)
    E = criterion(logits,targets)
    E.backward()

    loss = E.item()
    acc = accuracy(logits.data,targets)

    # TODO: ?
    # for p in model.parameters():
    #     p.grad.data /= batch_size

    return loss, acc

def accuracy(logits, targets):
    n = logits.shape[0]
    if targets.ndimension() == 2:
        _, y_trues = torch.max(targets,1)
    else:
        y_trues = targets
    _, y_preds = torch.max(logits,1)

    acc = (y_trues==y_preds).float().sum()*100.0/n
    return acc











