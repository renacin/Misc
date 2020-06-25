# Name:                                            Renacin Matadeen
# Date:                                               06/25/2020
# Title                              Understanding How Recursion Works In Programing
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import random
# ----------------------------------------------------------------------------------------------------------------------

"""
General Note:
    + Recursion isn't bad in-of-itself
    + It creates cleaner code, easier to maintain, and easier to read
    + However, it is extremely slow
    + From a perspective of Big(O), this will take O(2^n)
"""

# MAIN FUNCTION | Returns A Value In Accordance To The Fibbonaci Sequence
def fibo(n):

    # If The Number Is 1 Return 1 | THIS IS THE BASE CASE
    if n <= 1:
        return n

    # If The Number Is Not 1, Use Recursion Until The Base Case Is Found
    else:
        return(fibo(n - 1) + fibo(n - 2))


# MAIN FUNCTION | Creates A List Wih Fib Values
def quick_fib(list_of_xs):

    # Find Max Value In List Of Xs, Calculate Fib Values Up To Max, All While Storing Result
    max_list_of_xs = max(list_of_xs)




# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Create A List Filled With Random Numbers, These Numbers Will Be The Xs For The Fibbonaci Function
    list_len = 10000
    rand_list = [random.randint(0, 20) for x in range(list_len)]

    # Implement Recursion As Solution, How Long Does It Take?
    fibo1_list = [fibo(x) for x in rand_list]
