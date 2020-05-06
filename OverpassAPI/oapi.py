
# Name:                                            Renacin Matadeen
# Date:                                               05/05/2020
# Title                                          Overpass API Research
#
# ----------------------------------------------------------------------------------------------------------------------
import requests
import json
# ----------------------------------------------------------------------------------------------------------------------


# Def Function To Grab Data
def grab_osm_data():
    overpass_url = "http://overpass-api.de/api/interpreter"

    overpass_query = """
    [out:json];
    area["ISO3166-1"="DE"][admin_level=2];
    (node["amenity"="biergarten"](area);
     way["amenity"="biergarten"](area);
     rel["amenity"="biergarten"](area);
    );
    out center;
    """

    response = requests.get(overpass_url,
                            params={'data': overpass_query})
    data = response.json()

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    grab_osm_data()
