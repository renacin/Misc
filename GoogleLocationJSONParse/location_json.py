
# Name:                                            Renacin Matadeen
# Date:                                               05/05/2020
# Title                                          Overpass API Research
#
# ----------------------------------------------------------------------------------------------------------------------
import json
import time
import pandas as pd
from datetime import datetime
# ----------------------------------------------------------------------------------------------------------------------

# Def Function To Grab Data
def grablocationdata(path):

    json_file = open(path)
    json_file_str = json_file.read()
    json_data = json.loads(json_file_str)

    storage_dict = {"Date": [],
                    "Time": [],
                    "Latitude": [],
                    "Longitude": [],
                    "LatLongAcc": [],
                    "Altitude": [],
                    "Activity_Type": [],
                    "Activity_Conf": []
                    }


    for raw_data in json_data["locations"]:

        # Capture Time Data
        try:
            time_data = int(raw_data["timestampMs"][0: 10])
            time_raw = str(datetime.fromtimestamp(time_data))
            time_split = time_raw.split(" ")

            date_ = time_split[0]
            time_ = time_split[1]
        except KeyError as e:
            date_ = ""
            time_ = ""

        # Capture Location
        try:
            latitude_ = raw_data["latitudeE7"] / 10**7
            longitude_ = raw_data["longitudeE7"] / 10**7
            acc_ = raw_data["accuracy"]
        except KeyError as e:
            latitude_ = ""
            longitude_ = ""
            acc_ = ""

        # Additional Not Mission Critical | Capture Altitude Data
        try:
            altitude_ = raw_data["altitude"]
        except KeyError as e:
            altitude_ = ""

        # Additional Not Mission Critical | Capture Activity Data
        try:
            act_raw = raw_data["activity"]
            act_elem = act_raw[0]
            act_list = act_elem["activity"]
            act_dict = act_list[0]

            act_type = act_dict["type"]
            act_conf = act_dict["confidence"]

        except KeyError as e:
            act_type = ""
            act_conf = ""

        # Append Data
        storage_dict["Date"].append(date_)
        storage_dict["Time"].append(time_)
        storage_dict["Latitude"].append(latitude_)
        storage_dict["Longitude"].append(longitude_)
        storage_dict["LatLongAcc"].append(acc_)
        storage_dict["Altitude"].append(altitude_)
        storage_dict["Activity_Type"].append(act_type)
        storage_dict["Activity_Conf"].append(act_conf)

    # Dictionary To Pandas DF
    print("Writing Data To DF")
    df = pd.DataFrame.from_dict(storage_dict)

    # Write To CSV
    df.to_csv(r"C:\Users\renac\Desktop\LocationData.csv", index=False)
    print("Finished Writting")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    path = r"C:\Users\renac\Desktop\LocationHistory.json"

    grablocationdata(path)
