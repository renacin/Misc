# Name:                                            Renacin Matadeen
# Date:                                               01/07/2023
# Title                                 Computer To Computer Messaging System
#
# ----------------------------------------------------------------------------------------------------------------------
import os, datetime, csv, time, threading, random
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------


# Create A Worker Class That Can Run AutoTests
class Worker:


    # Initialize An Instance, When Called
    def __init__(self):
        """ Once Called A Worker Will Generate It's Own Name Randomly, And Load Needed Paths & Variables
        In The Future A Worker Should Check The Worker Check-In File & Choose A Name Not Choosen

        If Something Happens And This Worker Fails While Its main_worker_status == True, Program End Should Get Rid Of That
        Will There Be A Case Where We Have Two Workers With main_worker_status == True, Hopefully Not
        """

        # Worker Attributes
        self.id_name = random.randrange(0, 100_000, 1)
        self.main_worker_status = False
        self.check_in_delay = 3
        self.take_over_delay = 10
        self.SENTINEL = "&-99-&"

        # File Variables
        self.log_path = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\Comp2CompMessagingSystem\LOGS"
        lst_attest = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\Comp2CompMessagingSystem\MISC\ListOfAutoTests.csv"
        self.autotests = pd.read_csv(lst_attest)

        now = datetime.datetime.now()
        self.workerlog = f"WORKER_LOG_{now.year}_{now.month}_{now.day}.txt"
        self.logginglog = f"COMP_LOG_{now.year}_{now.month}_{now.day}.txt"



    # Worker Should Be Able To Check In Constantly Given It's Own Thread
    def check_in(self):
        """ This Class Method Will Be Used To Update The Workers main_worker_status variable & Worker Log File

        Cases:
            IF main_worker_status == TRUE , THEN WRITE TO WORKER LOG FILE
            IF main_worker_status == FALSE,
                AND WORKER LOG FILE EXISTS,
                AND LAST UPDATE GREATER THAN 10 SEC,
                THEN WRITE TO WORKER LOG FILE,
                AND main_worker_status == TRUE
            IF main_worker_status == FALSE,
                AND WORKER LOG FILE NOT EXISTS,
                THEN WRITE TO WORKER LOG FILE,
        """

        # Try To Check-In
        try:

            while True:
                # Check Time
                now = datetime.datetime.now()

                # If Previous Check-In Attempt Changed main_worker_status Worker Becomes Main Worker
                if self.main_worker_status == True:
                    with open(f"{self.log_path}\\{self.workerlog}", "a") as f:
                        f.write(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, WORKING, {self.SENTINEL} \n")
                        print(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, WORKING, {self.SENTINEL}")

                # If Previous Did Not Change main_worker_status
                else:

                    # And Check-In LOG Exists
                    if f"{self.workerlog}" in os.listdir(self.log_path):
                        with open(f"{self.log_path}\\{self.workerlog}", "r") as f:
                            lines = f.readlines()

                            # If Log Exists Check If Another Worker Has Been Working In The Last 10 Seconds
                            lst_log = datetime.datetime.strptime(lines[-1].split(",")[2].strip(), '%Y-%m-%d %H:%M:%S.%f')
                            wrk_dif = datetime.datetime.now() - lst_log

                            if wrk_dif.seconds > self.take_over_delay:
                                self.main_worker_status = True
                                with open(f"{self.log_path}\\{self.workerlog}", "a") as f:
                                    f.write(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, TAKING CONTROL, {self.SENTINEL} \n")
                                    print(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, TAKING CONTROL, {self.SENTINEL}")

                    # And Check-In LOG Doesn't Exist For The Day Then Worker Is Worker Is Main | Write To Text File
                    else:
                        self.main_worker_status = True
                        with open(f"{self.log_path}\\{self.workerlog}", "a") as f:
                            f.write(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, TAKING CONTROL, {self.SENTINEL} \n")
                            print(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, TAKING CONTROL, {self.SENTINEL}")

                # Before Checking In Again Wait A Few Seconds
                time.sleep(self.check_in_delay)

        # If Error Detected Stop
        except (KeyboardInterrupt, SystemExit):
            raise Exception


    # Worker Should Be Able To Check In Constantly Given It's Own Thread
    def main_loop(self):
        """ Continuously Check & Update Workers main_worker_status """

        # Create For Check-In & Work Process
        t1 = threading.Thread(target=self.check_in)
        t1.start()


# ----------------------------------------------------------------------------------------------------------------------

""" Script Defines The Main Logic Of A Worker That Can Complete AutoTests """
w1 = Worker()
w1.main_loop()
