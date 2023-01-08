# Name:                                            Renacin Matadeen
# Date:                                               01/07/2023
# Title                                 Computer To Computer Messaging System
#
# ----------------------------------------------------------------------------------------------------------------------
import os, datetime, csv, time
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------

def run_auto_test(list_of_tests):
    for test in list_of_tests:
        time.sleep(test[1])
        print(f"Completed {test[0]}")

# ----------------------------------------------------------------------------------------------------------------------
def main():
    """ This Is The Main Logic Of This Computer To Computer Messaging System"""

    # Step 1) Identify List Of Autotests To Run
    lst_attest = [("Amazon", 5.5), ("SmartCash", 4.5), ("Nordstrom", 2.5), ("AirMiles", 4.5), ("CashBack", 2.5), ("Business", 2.5)]

    # Step 2) Run AutoTests & Print Comletion Status
    run_auto_test(lst_attest)




# ----------------------------------------------------------------------------------------------------------------------


# Main Entry Point
if __name__ == "__main__":

    # Needed Variables
    main()
