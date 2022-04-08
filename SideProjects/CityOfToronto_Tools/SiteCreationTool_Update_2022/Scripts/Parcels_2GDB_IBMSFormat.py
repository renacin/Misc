# Name:     Site Creation Tool - Parcel 2 GeoDB
# Author:   Harrison Thomas
# Created:  02/01/2016
# Purpose:
#           Give users the ability to select parcels, and automatically have them
#           merged, catalogued, and stored within a common geodatabase.
# CHANGE LOG:
#           [2022-04-08 | Renacin Matadeen]
#           Update codebase, and add aditional functionality
# Copyright:
#           City of Toronto - City Planning; Urban Design - Graphics & Visualization
# Versioning:
#           ArcGIS -->      10.4.1
#           Python -->      2.7

# ----------------------------------------------------------------------------------------------------------------------
# Needed Libraries & Modules
import arcpy, os, string, datetime, time, re, sys, getpass
import pythonaddins
from arcpy import env

# Define Basic ArcMap Setting For Workspace
arcpy.SetLogHistory(False)
arcpy.env.overwriteOutput = True

# ----------------------------------------------------------------------------------------------------------------------



#   PRIVATE FUNCTION
def check_drives():
    """
    Check the available_drives; where should the outlocation be?
    """
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    for drive in available_drives:
    	a = os.path.join(drive,"\pln\Urbandesign\GRAPHICS\zResource\StoredParcels\DevApp.gdb")
    	b = os.path.join(drive,"\Urbandesign\GRAPHICS\zResource\StoredParcels\DevApp.gdb")
    	c = os.path.join(drive,"\pln\urbandesign\GRAPHICS\zResource\StoredParcels\DevApp.gdb")
    	d = os.path.join(drive,"\pln\pln\Urbandesign\GRAPHICS\zResource\StoredParcels\DevApp.gdb")
    	e = os.path.join(drive,"\GRAPHICS\zResource\StoredParcels\DevApp.gdb")

    	if os.path.exists(a):
    		out_location = a
    	elif os.path.exists(b):
    		out_location = b
    	elif os.path.exists(c):
    		out_location = c
    	elif os.path.exists(d):
    		out_location = d
    	elif os.path.exists(e):
    		out_location = e
    	else:
    		continue

# ----------------------------------------------------------------------------------------------------------------------


# Main Entry Point
if __name__ == "__main__":

    # # Get User Entry From Dialogue Box
    # selected_features = arcpy.GetParameterAsText(0)
    # submitDate  = arcpy.GetParameterAsText(1)
    # year = arcpy.GetParameterAsText(2)
    # sequence = arcpy.GetParameterAsText(3)
    # section = arcpy.GetParameterAsText(4)
    # ward = arcpy.GetParameterAsText(5)
    # type_ = arcpy.GetParameterAsText(6)
    # siteAddress = arcpy.GetParameterAsText(7)
    # status = arcpy.GetParameterAsText(8)
    # desc = arcpy.GetParameterAsText(9)
    # tlab_section = arcpy.GetParameterAsText(10)

    # Any Errors Arise Safely Shutdown Process
    try:
        # Check Drives
        check_drives()

    except:
        pass
