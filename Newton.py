# -*- coding: utf-8 -*-

import PlotIterations

from importlib import reload
reload(PlotIterations) # Relaod the module, in case it has changed

from PlotIterations import plotIterations

def newton(f, df, x0, N, verbose=True, plot=False, debug=False):

    if verbose:
        print("*** Newton-Raphson method ***")

    # if plot:
    x = []
    y = []

    for i in range(N):

        derivative = df(x0)

        if derivative == 0:
            print("Error in newton : derivative is equal to 0. Stopping at the actual value.")
            break;

        fx0 = f(x0)

        if plot:
            x.append(x0)
            y.append(fx0)

        x0 = x0 - f(x0)/derivative

        if verbose:
            print("Root = ", x0)

        if debug:
            print("Error = ", f(x0))

    if plot:

        x.append(x0)
        y.append(f(x0))

        if debug:
            print("x : ", x)
            print("y : ", y)

        plotIterations(f, x, y)

    return x0