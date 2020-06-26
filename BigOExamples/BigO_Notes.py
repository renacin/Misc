# Name:                                            Renacin Matadeen
# Date:                                               06/26/2020
# Title                                             Big O Examples
#
# ----------------------------------------------------------------------------------------------------------------------
"""
General:
    - Examples From:
        https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
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


"""
