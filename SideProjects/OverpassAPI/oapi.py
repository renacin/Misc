
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
    + Open Street Map's Data Model Is Sturctured Into Three Main Types
        - Nodes
            + A node is a simple point on a map. Think lat, long. Ex "This bench is her XXXX, YYYY"

        - Ways
            + A way is an ordered list of nodes. They can be used for the outline of a house, path of a river,
            or a flow of a street. Ex "This river starts here, curves here, and ends here"

        - Relations
            + A relation is also an ordered list; however it can contain anything from nodes, to ways, and even
            other relations. This can be used to model large detailed structures. Ex "All the dimensions of a mall"

    + Queries
        - Open Street Maps Uses A Unique Querying Methodology

        EXAMPLE LAYOUT
        - node["k"="v"] (bounding box);  out;

            + node["k"="v"] --> Looking for a node with Key, and Value Pair

            + (bounding box); --> Bounding Box (Lat, Long, Lat, Long)

    + WHEN IN DOUBT
        - If access through requets, or json is too shitty just use
            + http://overpass-turbo.eu/

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


# <tag k="landuse" v="cemetery"/>
# way["landuse"="cemetery"] (43.8637, -79.6516, 43.5819, -79.1126); out;
