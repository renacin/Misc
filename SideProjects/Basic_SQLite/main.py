# Name:                                            Renacin Matadeen
# Date:                                               12/10/2020
# Title                                          Basics Of SQL Lite
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import sqlite3
# ----------------------------------------------------------------------------------------------------------------------


# Create A Class For Our SQL_Lite Database
class SQL_Database:


    # Initial Function, Run When A WebCrawler Object Is Created
    def __init__(self):
        try:
            # Connect To Database Check If It has Data In It
            self.conn = sqlite3.connect(r"C:\Users\renac\Documents\Programming\Python\Misc\SideProjects\Basic_SQLite\Test.db")
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Test
            (NAME TEXT NOT NULL, AGE INT NOT NULL)
            ;''')

            print("Connected To Database")

        except sqlite3.OperationalError as e:
            print(e)

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    SQL_Connection = SQL_Database()




"""

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

"""
