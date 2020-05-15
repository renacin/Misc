
# Name:                                            Renacin Matadeen
# Date:                                               05/05/2020
# Title                                          Overpass API Research
#
# ----------------------------------------------------------------------------------------------------------------------
import requests
import json
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:

"""
# ----------------------------------------------------------------------------------------------------------------------

# Def Function To Grab Data
def grab_osm_data():
    overpass_url = "http://overpass-api.de/api/interpreter"

    overpass_query = """
    node["amenity"="cafe"]({{bbox}}); out;
    """

    print("Sending Response")
    response = requests.get(overpass_url, params={'data': overpass_query})

    print("Gathering Data")
    data = response.json()

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    grab_osm_data()
