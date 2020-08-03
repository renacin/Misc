# Name:                                            Renacin Matadeen
# Date:                                               08/03/2020
# Title                               Parallel Processing - Speeding Up Code With GPU
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import random
import numpy as np
from numba import jit, njit, vectorize, cuda
# ----------------------------------------------------------------------------------------------------------------------
@jit
def original_computation(input_list):
    output_list = []
    for val in input_list:
        if (val % 2 == 0):
            output_list.append(2)
        else:
            output_list.append(1)

    return output_list

@vectorize
def scalar_computation(num):
    if (num % 2 == 0):
        return 2
    return 1

    return output_list

@vectorize(['int32(int32)'], target='cuda')
def gpu_scalar_computation(num):
    if (num % 2 == 0):
        return 2
    return 1

    return output_list

def main():
    # List Size
    input_list = np.arange(500_000_000)

    # Jitted Function
    start = time.time()
    output_ = original_computation(input_list)
    print("Jitted Function: {}".format(time.time() - start))

    # Vectorized Function
    start = time.time()
    output_ = scalar_computation(input_list)
    print("Vectorized Function On CPU: {}".format(time.time() - start))

    # GPU Vectorized Function
    start = time.time()
    output_ = gpu_scalar_computation(input_list)
    print("Vectorized Function On GPU: {}".format(time.time() - start))

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
