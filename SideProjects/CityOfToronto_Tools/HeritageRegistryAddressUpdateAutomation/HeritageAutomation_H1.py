# Credits:                      City Of Toronto: Urban Design - Graphics & Visualization Dept.
# Author:                                          Renacin Matadeen
# Date:                                               01/14/2021
# Title             Heritage Register Automation: IBMS Data To 3 Streams [Portal, Opendata, ArcGIS Online Maps]
#                               TASK #1 - Clean Data & Prepare To Add To Data Streams
#
# ----------------------------------------------------------------------------------------------------------------------
# Modules Needed:
import os
import arcpy
from arcpy import metadata as md
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------
# GUI Input Parameters:
inExcelFile = arcpy.GetParameterAsText(0)
outFileFolder = arcpy.GetParameterAsText(1)

# File locations & Projection Files:
rows_no_xy_file = r"V:\pln\Urbandesign\GRAPHICS\G&V_Citywide\GIS_Heritage\ArcGIS_Toolboxes\HeritageRegistry_AutomatedUpdate\Outputs\HeritageRegisterRowsNoXY.xlsx"
auth_HRAP_geodb_file = r"V:\pln\Urbandesign\GRAPHICS\G&V_Citywide\GIS_Heritage\DATA\00_Authoritative\HeritagePlanningData.gdb\Heritage_Register_Address_Points"
sr = arcpy.SpatialReference(r"V:\pln\Urbandesign\GRAPHICS\G&V_Citywide\GIS_Heritage\ArcGIS_Toolboxes\HeritageRegistry_AutomatedUpdate\Projections\MTM10.prj")

# Expected Text Lenght
text_len = 250

# ----------------------------------------------------------------------------------------------------------------------

"""
[AUTOMATION - STEP #1]
	- Import IBMS data; drop unneeded columns, filter by status, and rename remaining columns
	- Be mindful of data practices set out by authoritative geodatabase
"""

# Clean Up Path Provided By ArcGIS Pro
list_of_path_elements = inExcelFile.split("\\")
inExcelFile = inExcelFile.replace("\\" + list_of_path_elements[-1], "")


# Drop Columns
df = pd.read_excel(inExcelFile)
columns_to_keep = ["ID", "PROPX", "PROPY", "status", "STATUSCODE", "address", "bylaw", "details"]
for col in df.columns:
	if (col not in columns_to_keep):
		df.drop(col, axis = 1, inplace = True)


# Filter By Status
status_to_keep = ["Listed", "Part IV", "Part V", "Status"]
df = df[df['status'].isin(status_to_keep)]


# Rename Columns For Consistency With Authoritative Geodatabase
list_of_fieldnames = ["IBMS_ID", "X", "Y", "StatusCode", "Status", "Address", "ByLaw", "Details"]
rename_col = {
			  "ID":list_of_fieldnames[0],
			  "PROPX":list_of_fieldnames[1], "PROPY":list_of_fieldnames[2],
			  "STATUSCODE":list_of_fieldnames[3], "status":list_of_fieldnames[4],
			  "address":list_of_fieldnames[5], "bylaw":list_of_fieldnames[6],
			  "details":list_of_fieldnames[7]
			  }


# Rename Columns & Make Sure That Fields Are The Appropriate Types
df.rename(columns = rename_col, inplace = True)
df.drop(['IBMS_ID'], axis=1, inplace = True)


# Covert Certain Fields To String
for column in list_of_fieldnames[3:]:
	df[column] = df[column].astype(str)


# Strip Whitespace Before
for column in list_of_fieldnames[3:]:
	df[column] = df[column].str.strip()

# Text Stored In ArcGIS Is Only 254 Char Long Match
details_list = df["Details"].tolist()
short_detail_list = []
for detail in details_list:
	if len(detail) > text_len:
		short_detail_list.append(detail[0:text_len])
	else:
		short_detail_list.append(detail)

df["Details"] = short_detail_list


# Strip Whitespace After
df.fillna("")
df.replace("nan", "", inplace=True)
for column in list_of_fieldnames[3:]:
	df[column] = df[column].str.strip()

df = df.replace(" ", "")

excel_df = df
num_rows_IBMS_data = len(excel_df)		# For Logging Purposes


# ----------------------------------------------------------------------------------------------------------------------

"""
[AUTOMATION - STEP #2]
	- Import data from authoritative geodatabase; compare records in database with the data from the excel file
	- Find common rows, rows found only in auth geoDB, and new rows In excel sheet
	- Filter out rows with inoperable X, Y coordinates, these will be added to the RowsWithNo_XY masterfile
"""

# Split Into Two DFs, One With Operatble MTM10_X, MTM10_Y Values, And One Without, Make Sure MTM Are Float
excel_df['X'] = excel_df['X'].round(decimals=5)
excel_df['Y'] = excel_df['Y'].round(decimals=5)

excel_df = excel_df.fillna(-0.123456789)
excel_df_gxy = excel_df[excel_df["X"] != -0.123456789]
excel_df_bxy = excel_df[excel_df["X"] == -0.123456789]

excel_df_gxy.replace(-0.123456789, "", inplace=True)
excel_df_bxy.replace(-0.123456789, "", inplace=True)


# Remove Nan Values & Strip Whitespace
excel_df_gxy.replace("nan", "", inplace=True)
for column in list_of_fieldnames[3:]:
	excel_df_gxy[column] = excel_df_gxy[column].str.strip()

excel_df_gxy.drop_duplicates(inplace=True)


num_rows_badxy_IBMS = len(excel_df_bxy)		# For Logging Purposes


# Open Authoritative Heritage Register Address Points Geodatabase & Copy Data And Turn Into Dataframe
data_dump = {}
for field in list_of_fieldnames[1:]:
	data_dump[field] = []

with arcpy.da.SearchCursor(auth_HRAP_geodb_file, list_of_fieldnames[1:]) as cursor:
	for row in cursor:
		idx = 0
		for field in list_of_fieldnames[1:]:
			data_dump[field].append(row[idx])
			idx += 1


# Clean Up Authoritative Geodatabase; Just Incase
geobd_df = pd.DataFrame.from_dict(data_dump)
geobd_df['X'] = geobd_df['X'].round(decimals=5)
geobd_df['Y'] = geobd_df['Y'].round(decimals=5)


# Covert Certain Fields To String
for column in list_of_fieldnames[3:]:
	geobd_df[column] = geobd_df[column].astype(str)

geobd_df.fillna("", inplace=True)
geobd_df.replace(" ", "", inplace=True)
geobd_df.replace("None", "", inplace=True)


# Strip Whitespace Before Just Incase
for column in list_of_fieldnames[3:]:
	geobd_df[column] = geobd_df[column].str.strip()


# Text Stored In ArcGIS Is Only 254 Char Long Match
geobd_df_details_list = geobd_df["Details"].tolist()
geobd_df_short_detail_list = []
for detail in geobd_df_details_list:
	if len(detail) > text_len:
		geobd_df_short_detail_list.append(detail[0:text_len])
	else:
		geobd_df_short_detail_list.append(detail)

geobd_df["Details"] = geobd_df_short_detail_list


# Strip Whitespace After Just Incase
geobd_df.fillna("")
for column in list_of_fieldnames[3:]:
	geobd_df[column] = geobd_df[column].str.strip()


num_rows_authDB_data = len(geobd_df)		# For Logging Purposes


# Merge Both Files, Keep Note Of What Is Common, And What Is New
cr_df = geobd_df.merge(excel_df_gxy, on=list_of_fieldnames[1:], how='outer', indicator=True)


# Sort Delete Duplicate Rows
cr_df.sort_values(by="X", inplace=True)
cr_df.drop_duplicates(inplace=True)
num_output_with_duplicates = len(cr_df)		# For Logging Purposes


# For Logging Purposes
num_unique_rows_IBMS = len(cr_df[cr_df["_merge"] == "right_only"])
num_unique_rows_AuthGeoDB = len(cr_df[cr_df["_merge"] == "left_only"])
num_common_rows = len(cr_df[cr_df["_merge"] == "both"])


# Ensure NoXY Rows Haven't Been Corrected For And Appended To The AuthGeoDB, Before Adding To Master NoXY
noxy_cr_df = geobd_df.merge(excel_df_bxy.drop_duplicates(), on=list_of_fieldnames[3:],
                   how='outer', indicator=True)

noxy_rows_df = noxy_cr_df[noxy_cr_df["_merge"] == "right_only"]
noxy_rows_df.drop(["_merge", "X_y", "Y_y"], axis=1, inplace = True)
badxy_rename_col = {"X_x":"X", "Y_x":"Y"}
noxy_rows_df.rename(columns = badxy_rename_col, inplace = True)


# Add Rows With No XY Into The RowsWithNoXY Master File In V:/ Drive
num_rows_badxy_MasterFile = len(noxy_rows_df)
noxy_rows_df.to_excel(rows_no_xy_file, index=False)


# Dropped Merged Column & Then Drop Duplicates
cr_df = cr_df.drop(["_merge"], axis=1)
cr_df = pd.DataFrame.drop_duplicates(cr_df)
num_output_without_duplicates = len(cr_df)		# For Logging Purposes


# ----------------------------------------------------------------------------------------------------------------------

"""
[AUTOMATION - STEP #3]
	- Create a shapefile based on the cleaned data; map the XY data provided
	- Add metadata and write to a location on the user's desktop; don't write to NAS as it will take a lot longer
	- Be cautious of final projection
"""

# Write Cleaned Data To Desktop Location As Provided By User, Add Metadata As Well
temp_csv = outFileFolder + "\\" + "TempCSV.csv"
cr_df["ElevTemp"] = 0.00
cr_df.to_csv(temp_csv, index=False)
output_shp = outFileFolder + "\\" + "Heritage_Register_Address_Points.shp"
arcpy.management.XYTableToPoint(temp_csv, output_shp, "X", "Y", "ElevTemp", sr)


# Add Metadata To New Shapefile
new_md = md.Metadata()
new_md.title = "Heritage Registry Address Points"
new_md.tags = "Heritage Inventory"
new_md.summary = "Location of heritage properties in City of Toronto"

s1 = "Listed, Part IV, Part V & Intention properties are included.\n"
s2 = "Please note, some properties indicated as \"designated\" may be subject to an intention to designate by City Council, and should be considered fully designated for the purposes of alterations and permitting.\n"
s3 = "For more information, please contact Yasmina Shamji at 416-392-1975."
new_md.description =  s1 + s2 + s3

new_md.credits = "City of Toronto: City Planning; Graphics & Visualization Section"


# Assign the Metadata object's content to a target item
tgt_item_md = md.Metadata(output_shp)
if not tgt_item_md.isReadOnly:
    tgt_item_md.copy(new_md)
    tgt_item_md.save()


# Delete Unneeded Columns In Newly Created Shapefile | Remember Keep Fields Consistent Across Data Streams
arcpy.DeleteField_management(output_shp, ["ElevTemp"])


# ----------------------------------------------------------------------------------------------------------------------

"""
[AUTOMATION - STEP #4]
	- Provide simple logging outputs for both archival, and user usage
	- Logging Should Include:
		+ Total Number Of Rows, New File Vs. Authoritative DB
		+ Number Of Unique Rows In Auth DB, Unique Rows In New IBMS Data, Common Rows Between Files
		+ How Many new Rows Don't Have XY Coordinates, In Comparison To Masterfile
"""

# Logging Stage
arcpy.AddMessage("--General--")
arcpy.AddMessage("Rows In New IBMS Data: " + str(num_rows_IBMS_data))
arcpy.AddMessage("Rows In Old AuthGeoDB Data: " + str(num_rows_authDB_data))
arcpy.AddMessage(".")

arcpy.AddMessage("--Common/Unique--")
arcpy.AddMessage("Common Rows In Old AuthGeoDB & New IBMS Data: " + str(num_common_rows))
arcpy.AddMessage("Unique Rows In Old AuthGeoDB: " + str(num_unique_rows_AuthGeoDB))
arcpy.AddMessage("Unique Rows In New IBMS Data: " + str(num_unique_rows_IBMS))
arcpy.AddMessage(".")

arcpy.AddMessage("--MissingCoordinates--")
arcpy.AddMessage("Rows In New IBMS Data With No XY: " + str(num_rows_badxy_IBMS))
arcpy.AddMessage("Rows In No XY Masterfile: " + str(num_rows_badxy_MasterFile))
arcpy.AddMessage("Rows In Old AuthGeoDB That Have User Corrected XYs: " + str(num_rows_badxy_IBMS - num_rows_badxy_MasterFile))
arcpy.AddMessage(".")

arcpy.AddMessage("--FinalOutput--")
arcpy.AddMessage("Rows In Final Output File: " + str(num_output_without_duplicates))
arcpy.AddMessage(".")


# ----------------------------------------------------------------------------------------------------------------------

"""
[AUTOMATION - STEP #5]
	- Clean up and temporary files
"""

# Remove TempCSV File
os.remove(temp_csv)
