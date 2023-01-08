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

        self.id_name = random.randrange(0, 1000, 1)
        self.log_path = r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\Comp2CompMessagingSystem\LOGS"
        self.main_worker_status = False
        self.SENTINEL = "&-99-&"



    # Worker Should Be Able To Check In Constantly Given It's Own Thread
    def check_in(self):
        """ This Class Method Will Be Used To Update The Workers main_worker_status variable

        Cases:
            Worker Has Just Been Initialized,                  main_worker_status = False
            Worker Checks Log File And Sees Someone Working,   main_worker_status = False
            Worker Checks Log File And Sees No One Working,    main_worker_status = True
        """
        # Check Time
        now = datetime.datetime.now()

        # If Previous Check-In Attempt Changed main_worker_status Worker Is Main Worker
        if self.main_worker_status == True:
            with open(f"{self.log_path}\\WORKER_LOG_{now.year}_{now.month}_{now.day}.txt", "a") as f:
                f.write(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, WORKING, {self.SENTINEL} \n")
            return

        # Check To See If Worker Check-In LOG Exists | Note Logs Are Day Specific
        if f"WORKER_LOG_{now.year}_{now.month}_{now.day}.txt" in os.listdir(self.log_path):
            with open(f"{self.log_path}\\WORKER_LOG_{now.year}_{now.month}_{now.day}.txt", "r") as f:
                lines = f.readlines()

                # If Log Exists Check If Another Worker Has Been Working In The Last 10 Seconds
                lst_log = datetime.datetime.strptime(lines[-1].split(",")[2].strip(), '%Y-%m-%d %H:%M:%S.%f')
                wrk_dif = datetime.datetime.now() - lst_log

                if wrk_dif.seconds > 10:
                    self.main_worker_status = True
                    with open(f"{self.log_path}\\WORKER_LOG_{now.year}_{now.month}_{now.day}.txt", "a") as f:
                        f.write(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, TAKING CONTROL, {self.SENTINEL} \n")

        # If File Doesn't Exist For The Day Then Worker Is Worker Is Main | Write To Text File
        else:
            self.main_worker_status = True
            with open(f"{self.log_path}\\WORKER_LOG_{now.year}_{now.month}_{now.day}.txt", "a") as f:
                f.write(f"[WORKSTAT], {self.id_name}, {datetime.datetime.now()}, FIRST WORKER, {self.SENTINEL} \n")

        return



    # Worker Should Be Able To Check In Constantly Given It's Own Thread
    def work(self):
        """ Based On The Worker's main_worker_status variable, determine if the Worker Should Begin Work

        Cases:
            If main_worker_status = False, Don't Do Work    - Wait For Check-In To Return Different Value
            If main_worker_status = True , Start Doing Work - Either Start At Begining, Or Pick Off Where Other Worker Left Off
         """

        # Based Of main_worker_status Start Working Or Exit To Thread Loop
        if self.main_worker_status == True:
            print(f"Worker {self.id_name}: Working")
        else:
            print(f"Worker {self.id_name}: Not Working")



    # Worker Should Be Able To Check In Constantly Given It's Own Thread
    def main_loop(self):
        """ Continuously Check & Update Workers main_worker_status """

        c_var = True
        while c_var:
            try:
                # Create Thread To Run Check In Process
                t1 = threading.Thread(target=self.check_in)
                t1.start()

                # Create Thread To Run Start Working
                t2 = threading.Thread(target=self.work)
                t2.start()

                # Wait A Couple Of Seconds Before Trying Again
                time.sleep(2)

            except Exception:
                c_var = False


# ----------------------------------------------------------------------------------------------------------------------

""" Script Defines The Main Logic Of A Worker That Can Complete AutoTests """
w1 = Worker()
w1.main_loop()
