# Name:                                            Renacin Matadeen
# Date:                                               08/03/2020
# Title                               Parallel Processing - Speeding Up Code With GPU
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import numpy as np
from numba import vectorize
# ----------------------------------------------------------------------------------------------------------------------

@vectorize(['float32(float32, float32)'], target='cuda')
def pow(a, b):
    return a ** b

def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)
    
    start = time.time()
    c = pow(a, b)
    duration = time.time() - start

    print(duration)

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
