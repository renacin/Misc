# Name:                                            Renacin Matadeen
# Date:                                               01/07/2023
# Title                                 Computer To Computer Messaging System
#
# ----------------------------------------------------------------------------------------------------------------------
import os, datetime, csv, time
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------

def run_auto_test(autotests, log_path, SENTINEL):
    """ This function mimics Zeus. Takes a list of autotests, and runs them """

    # Check To See If LOG Data Exists & What The Last Test Was | Note Logs Are Day Specific
    now = datetime.datetime.now()
    if f"COMP_LOG_{now.year}_{now.month}_{now.day}.txt" in os.listdir(log_path):
        with open(f"{log_path}\\COMP_LOG_{now.year}_{now.month}_{now.day}.txt", "r") as f:
            lines = f.readlines()
            max_idx = int(lines[-1].split(",")[1])
    else:
        max_idx = 0

    # Based On Previous Logs Written (In The Same Day) Focu Only On The AutoTests That Haven't Been Run
    autotests = autotests.iloc[max_idx:]
    with open(f"{log_path}\\COMP_LOG_{now.year}_{now.month}_{now.day}.txt", "a") as f:
        for index, row in autotests.iterrows():
            time.sleep(row["Time"])
            f.write(f"[COMPSTAT], {row['ID']}, {row['TestName']}, {datetime.datetime.now()}, {SENTINEL} \n")
            print(row["TestName"])


# ----------------------------------------------------------------------------------------------------------------------
def main():
    """ This Is The Main Logic Of This Computer To Computer Messaging System"""

    # Step 0) Define Variables & Pull Needed Data
    log_path = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\Comp2CompMessagingSystem\LOGS"
    lst_attest = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\Comp2CompMessagingSystem\MISC\ListOfAutoTests.csv"
    autotests = pd.read_csv(lst_attest)

    # Step 2) Run AutoTests & Print Comletion Status
    run_auto_test(autotests, log_path, "&-99-&")




# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point
if __name__ == "__main__":
    main()
