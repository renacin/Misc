# Name:                                            Renacin Matadeen
# Date:                                               08/03/2020
# Title                               Parallel Processing - Speeding Up Code With GPU
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import random
import numpy as np
from numba import jit, njit, vectorize, cuda, int32
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

@vectorize(['int32(int32)'], target='parallel')
def cpu_scalar_computation(num):
    if (num % 2 == 0):
        return 2
    return 1

@cuda.jit
def gpu_computation(input_list):
    output_list = []
    for val in input_list:
        if (val % 2 == 0):
            output_list.append(2)
        else:
            output_list.append(1)

    return output_list

def main():
    # List Size
    input_list = np.arange(500_000_000)

    # Jitted Function
    start_1 = time.time()
    output_1 = original_computation(input_list)
    print("Jitted Function: {}".format(time.time() - start_1))

    # Vectorized Function Single Core
    start_2 = time.time()
    output_2 = scalar_computation(input_list)
    print("Vectorized Function On Single Thread CPU: {}".format(time.time() - start_2))

    # Vectorized Function Multi-Core
    start_3 = time.time()
    output_3 = cpu_scalar_computation(input_list)
    print("Vectorized Function On Multi-Threaded CPU: {}".format(time.time() - start_3))

    # GPU Function
    start_4 = time.time()
    output_4 = gpu_computation(input_list)
    print("Vectorized Function On GPU: {}".format(time.time() - start_4))

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
