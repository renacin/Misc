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

@vectorize(['int32(int32)'], target='parallel')
def cpu_scalar_computation(num):
    if (num % 2 == 0):
        return 2
    return 1


def main():
    # List Size
    input_list = np.arange(100_000)

    # Jitted Function
    start_1 = time.time()
    output_1 = original_computation(input_list)
    print("Jitted Function: {}".format(time.time() - start_1))

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
