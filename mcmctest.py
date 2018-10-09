#coding:utf-8
import pymc3 as pm
import matplotlib.pyplot as plt
import numpy as np

observed = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
h = sum(observed)
n = len(observed)
alpha, beta = 1, 1
niter = 10 ** 6
with pm.Model() as model:
    # define priors
    p = pm.Beta('p', alpha=alpha, beta=beta)
    # define likelihood
    y = pm.Binomial('y', n=n, p=p, observed=h)
    # inference
    start = {'p': 0.5}
    step = pm.Metropolis()
    trace = pm.sample(niter, step, start)
pm.traceplot(trace)
plt.show()

N = 10000
p, bins = np.histogram(trace["p"], bins=N, density=True)
theta = np.linspace(np.min(bins), np.max(bins), N)
print("ML:" + str(h / float(n)))
print("MCMC:" + str(np.dot(p, theta) / N))
