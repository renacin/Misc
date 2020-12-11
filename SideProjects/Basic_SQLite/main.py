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
            CREATE TABLE IF NOT EXISTS IdentifierTable
            (ID INT NOT NULL, AGE INT NOT NULL)
            ;''')

            print("Connected To Database")

        except sqlite3.OperationalError as e:
            print(e)


    # Function To Insert Data Into Database
    def addtoDB(self, data_):
        cursor = self.conn.cursor()
        for row in data_:
            sqlite_insert_str = """INSERT INTO IdentifierTable
                                    (ID, AGE)
                                    VALUES
                                    ({}, {});"""

            sqlite_insert_query = sqlite_insert_str.format(row[0], row[1])
            count = cursor.execute(sqlite_insert_query)
            self.conn.commit()
        cursor.close()


    # Function To Return Number Of Rows In Database
    def rowsinDB(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM IdentifierTable;")
        print(len(cursor.fetchall()))
        cursor.close()



# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    SQL_Connection = SQL_Database()
    SQL_Connection.addtoDB([[123, 21], [123, 21], [123, 21], [123, 21], [123, 21], [123, 21], [123, 21], [123, 21]])
    SQL_Connection.rowsinDB()
