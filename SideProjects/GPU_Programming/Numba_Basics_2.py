# Name:                                            Renacin Matadeen
# Date:                                               08/03/2020
# Title                               Parallel Processing - Speeding Up Code With GPU
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import random
import numpy as np
import pandas as pd
from numba import vectorize, int32
# ----------------------------------------------------------------------------------------------------------------------

def create_data():
    """ Create Test Data For Functions """
    list_lenght = 5_000_000
    input_list = [random.randint(0, 10) for i in range(list_lenght)]
    d = {'RandomNumbers': input_list}
    df = pd.DataFrame(data = d)
    return df

def pandas_vect(num):
    """ Pandas Implementation Of Vectorization """
    if (num % 2 == 0):
        return 2
    return 1

@vectorize(['int32(int32)'], target='parallel')
def numba_vect(num):
    if (num % 2 == 0):
        return 2
    return 1

# ----------------------------------------------------------------------------------------------------------------------

def main():
    # Create A Pandas Dataframe, First Column Should Be Random Numbers Of N Lenght
    df = create_data()

    # Test Function Speed As Pandas Vectorized
    start_1 = time.time()
    output_list_1 = [pandas_vect(x) for x in df["RandomNumbers"]]
    print("Pandas Vectorized Function: {}".format(time.time() - start_1))

    # Test Function Speed As Numba Vectorized With Parallel Compute
    data_ = list(df["RandomNumbers"])
    array_data_ = np.array(data_)
    start_2 = time.time()
    output_list_2 = numba_vect(array_data_)
    print("Parallel Numba Vectorized Function: {}".format(time.time() - start_2))

    print(output_list_1[:5])
    print(output_list_2[:5])

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
