# Name:                                            Renacin Matadeen
# Date:                                               06/26/2020
# Title                                             Big O Examples
#
# ----------------------------------------------------------------------------------------------------------------------
"""
General:
    - Examples From:
        https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
        https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7

    - Big O In Order Of Time Complexity:
        = O(1) ----------- Constant
        = O(logN) -------- Logarithmic
        = O(logN^C) ------ PolyLogarithmic
        = O(N) ----------- Linear
        = O(N^C) --------- Polynomial
        = O(C^N) --------- Exponential
        = O(N!) ---------- Factorial
"""
# ----------------------------------------------------------------------------------------------------------------------
"""
[EXAMPLE #1 - Constant Complexity]
Ex:
    print("Hello World")

BigO:
    = O(1)

Explanation:
    - In this case the section of code will always take the same amount of time
    - Size of inputs does not influence the time a code takes to run
"""
# ----------------------------------------------------------------------------------------------------------------------
"""

[EXAMPLE #2A - Linear Complexity]
Ex:
    for name in listofnames:
        print(name)

BigO:
    = O(N)

Explanation:
    - The time it takes to run this section of code depends on the number of inputs
    - The larger the number of inputs the longer iit takes to run this section of code


[EXAMPLE #2B - Complex Linear Complexity]
Ex:
    print("Last Names:")
    for last_name in list_of_last_names:
        print(last_name)

    print("First Names:")
    for first_name in list_of_first_names:
        print(first_name)

BigO:
    = O(1) + O(N) + O(1) + O(N)
    = O(2) + O(2N)
    = O(2N)


[EXAMPLE #3A - Polynomial Complexity]
Ex:
    for first_name in list_of_first_names:
        for last_name in list_of_last_names:
            print(first_name, last_name)

BigO:
    = O(N^2)

Explanation:
    - For each item in the outer loop, loop through the values of the inner loop
    - Simply stated, N*N (For the number of nested loops)


[EXAMPLE #3B - Complex Polynomial Complexity]
Ex:
    for first_name in list_of_first_names:
        for last_name in list_of_last_names:
            for nation in nation_list
                print(first_name, last_name, nation)

    print("Hello World")

    for first_name in list_of_first_names:
        print(first_name)

BigO:
    = O(N^3) + O(1) O(N)
    = O(N^3)


[EXAMPLE #4 - Exponential Complexity]
Ex:
    for first_name in list_of_first_names:
        for last_name in list_of_last_names:
            print(first_name, last_name)
"""
