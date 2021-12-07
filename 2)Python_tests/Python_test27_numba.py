import matplotlib
import numpy
import time
import random
from numba import jit

def timer(f):
    def wrapper(n):
        start=time.time()
        f(n)        
        total=time.time()-start
        print(total)
    return wrapper

@timer
@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

monte_carlo_pi(100000)
monte_carlo_pi(100000)

print("without")

@timer
def monte_carlo_pi_no_numba(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

monte_carlo_pi_no_numba(100000)
monte_carlo_pi_no_numba(100000)