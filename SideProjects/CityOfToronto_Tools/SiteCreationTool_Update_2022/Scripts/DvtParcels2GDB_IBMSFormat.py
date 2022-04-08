#
#-------------------------------------------------------------
# Name:       DvtParcels2GDB_IBMSFormat.py
# Purpose:    To store parcel information into a GDB
# Author:     Harrison Thomas
# Created:    02/01/2016
# Copyright:   (c) City of Toronto - City Planning
# ArcGIS Version:   10.4.1
# Python Version:   2.7
# CTRL + F '# [FieldEdit]' to find places to add code
# Located in "V:\pln\Urbandesign\GRAPHICS\zResource\StoredParcels"
# 44 Ward Format Name: Parcels2GDB
# 25 Ward Format Name: Parcels2GDB2
#-------------------------------------------------------------

import arcpy, os, string, datetime, time, re, sys, getpass
import pythonaddins
from arcpy import env

def findField(fc, fi):
  fieldnames = [field.name for field in arcpy.ListFields(fc)]
  if fi in fieldnames:
    return True
  else:
    return False


# Turn off geoprocessing logging history
arcpy.SetLogHistory(False)

arcpy.env.overwriteOutput = True

selected_features = arcpy.GetParameterAsText (0) # selected features from parcel

# Parcel count check
# TO DO: AddWarning if pcount >100 and pcount <1499:
# Check if pcount = count of target database
# https://gis.stackexchange.com/questions/108036/using-get-count-with-if-statment
arcpy.AddMessage('\n\n\n')
pCount = int(arcpy.GetCount_management(selected_features).getOutput(0))

# File path check
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

# [FieldEdit]
submitDate  = arcpy.GetParameterAsText(1) # Date Submitted
year = arcpy.GetParameterAsText(2)  # Year
year = year[:2]
if len(year)<2:
	year = str(year.zfill(2))

sequence = arcpy.GetParameterAsText(3)  # 6 number file
if len(sequence) <6:
	sequence = str(sequence.zfill(6)) # Adds a 0 to older file numbers

section = arcpy.GetParameterAsText(4) # Section, 3 letter string
section = section.upper()

ward = arcpy.GetParameterAsText(5)  # Ward number 05, 06, etc.
if len(ward) <2:
	ward = str(ward.zfill(2))[:2] # Adds leading zeros

type = arcpy.GetParameterAsText(6)
type =type.upper()[:4] # Drop Down list corresponding with GDB domains
siteAddress = arcpy.GetParameterAsText(7)  # Complex address field
status = arcpy.GetParameterAsText(8) # Current status of the development application
desc = arcpy.GetParameterAsText(9) # Folder description in IBMS
desc = desc.replace("'", "\\'")
tlab_section = arcpy.GetParameterAsText(10) # TLAB section

# FeatureClass Allocation, no longer storing in the 'DevelopmentApplications' fc

if section == 'ESC':
	out_location = os.path.join(out_location,'ScarboroughParcels_citymtm')
	arcpy.AddMessage("Your " + str(pCount) + " parcel (s) will be saved in \n---> " + out_location )
elif section == 'NNY':
	out_location = os.path.join(out_location,'NorthYorkParcels_citymtm')
	arcpy.AddMessage("Your " + str(pCount) + " parcel (s) will be saved in \n---> " + out_location )
elif section == 'STE':
	out_location = os.path.join(out_location,'TorontoEastYorkParcels_citymtm')
	arcpy.AddMessage("Your " + str(pCount) + " parcel (s) will be saved in \n---> " + out_location )
elif section == 'WET':
	out_location = os.path.join(out_location,'EtobicokeParcels_citymtm')
	arcpy.AddMessage("Your " + str(pCount) + " parcel (s) will be saved in \n---> " + out_location )

if type == 'TLAB':
	combined = str(year) + ' ' + str(sequence) + ' ' + str(tlab_section) + ' ' + str(ward) + ' ' + type
elif year != 'PL':
	combined = str(year) + ' ' + str(sequence) + ' ' + str(section) + ' ' + str(ward) + ' ' + type
else:
	combined = str(year) + str(sequence)
ward = int(ward)
arcpy.AddMessage("Ward is: " + str(ward))

destCount = int(arcpy.GetCount_management(out_location).getOutput(0))
arcpy.AddMessage("\n" * 2)
ward44dict = {01: "Etobicoke North", 02: "Etobicoke North", 03: "Etobicoke Centre", 04: "Etobicoke Centre", 05: "Etobicoke-Lakeshore", 06: "Etobicoke-Lakeshore", 07: "York West", 8: "York West", 9: "York Centre", 10: "York Centre", 11: "York South-Weston", 12: "York South-Weston", 13: "Parkdale-High Park", 14: "Parkdale-High Park", 15: "Eglinton-Lawrence", 16: "Eglinton-Lawrence", 17: "Davenport", 18: "Davenport", 19: "Trinity-Spadina", 20: "Trinity-Spadina", 21: "St. Paul's", 22: "St. Paul's", 23: "Willowdale",  24: "Willowdale", 25: "Don Valley West", 26: "Don Valley West", 27: "Toronto Centre-Rosedale", 28: "Toronto Centre-Rosedale", 29: "Toronto-Danforth", 30: "Toronto-Danforth", 31: "Beaches-East York", 32: "Beaches-East York", 33: "Don Valley East", 34: "Don Valley East", 35: "Scarborough Southwest", 36: "Scarborough Southwest", 37: "Scarborough Centre", 38: "Scarborough Centre", 39: "Scarborough Agincourt", 40: "Scarborough Agincourt", 41: "Scarborough-Rouge River", 42: "Scarborough-Rouge River", 43: "Scarborough East", 44: "Scarborough East"}

ward25dict = {
01: "Etobicoke North", 02: "Etobicoke Centre", 03: "Etobicoke-Lakeshore", 04: "Parkdale-High Park", 05: "York South-Weston", 06: "York Centre", 07: "Humber River-Black Creek", 8: "Eglinton-Lawrence", 9: "Davenport", 10: "Spadina-Fort York", 11: "University-Rosedale", 12: "Toronto-St. Paul’s", 13: "Toronto Centre", 14: "Toronto-Danforth", 15: "Don Valley West", 16: "Don Valley East", 17: "Don Valley North", 18: "Willowdale", 19: "Beaches-East York", 20: "Scarborough Southwest", 21: "Scarborough Centre", 22: "Scarborough-Agincourt", 23: "Scarborough North", 24: "Scarborough-Guildwood", 25: "Scarborough-Rouge Park"}

arcpy.AddMessage("Ward is " + str(ward))
arcpy.AddMessage("Year is " + str(year))

if year >18 and ward <25:
	wardName = ward25dict.get(ward)
elif year <=18 and ward >=25:
	wardName = ward44dict.get(ward)
elif year >18 and ward ==25:
	wardName = ward25dict.get(ward)
else:
	wardName = ward44dict.get(ward)

#arcpy.AddMessage ("Ward Neigbhourhood is " + wardName)
# Check selected input layer
arcpy.AddMessage("Attempting to save " + str(pCount) + " parcel(s) in \n---> " + out_location )
arcpy.AddMessage("There are currently " + str(destCount) + " parcels in the target location")
print "Attempting to save" + str(pCount) + " parcel(s) in \n---> " + out_location
print "There are currently " + str(destCount) + " parcels in the target location"

if pCount == destCount:   # Selecting the fc without a selection
	arcpy.AddMessage("Detected that you have not made a selection. Please check your input layer to see if a selection has been made and try again.")
	arcpy.AddMessage("Program Terminated")
	print pythonaddins.MessageBox("Detected that you have not made a selection. Please check your input layer to see if a selection has been made and try again.", 0)
	sys.exit()
elif pCount >1500:  # Too large of a selection
	arcpy.AddMessage("Too many parcels have been selected, please check your input layer to see if a selection has been made and try again.")
	arcpy.AddMessage("Program Terminated")
	print pythonaddins.MessageBox("Detected that too many parcels have been selected. Please ensure you have selected less than 1500 parcels", "ERROR - Too many parcels selected", 0)
	sys.exit()
else:
	arcpy.AddMessage("Number of parcel(s) selected: " + str(pCount))
	print 'Success'

try:



	# MakeFeatureLayer + CopyFeatures to remove joins from SDE
	# tempLayer = arcpy.MakeFeatureLayer_management(selected_features, r"in_memory\tempLayer")
	arcpy.AddMessage("---" * 3)
	arcpy.AddMessage("Preprocessing data")
	arcpy.AddMessage("---" * 3)
	table = arcpy.CopyFeatures_management(selected_features,r"in_memory\tableLayer" )
	arcpy.AddMessage("\tParcels copied into memory...")
	dtable = r"in_memory\dissLayer"
	tempTable = r"in_memory\tempTable"
	# Field testing
	# dsc = arcpy.Describe(table)
	# fields = dsc.fields
	# #arcpy.AddMessage('Name,\t Type,\t\t Editable?')
	# for f in fields:
		# arcpy.AddMessage("{0} is a type of {1} with a length of {2}".format(f.name, f.type, f.length))
	# del dsc
	# del fields



	# Delete unwanted fields
		# Manually enter field names to keep here
		# Include mandatory fields name such as OBJECTID (or FID...), and Shape in keepfields
		# Not keeping AROLL, as there could be multiple parcels being used for selection
	fields = arcpy.ListFields(table)
	keepFields = ["OBJECTID","Shape","FID","AROLL","SHAPE", "Shape" "SHAPE_Length", "SHAPE_Area", "Shape_Length", "Shape_Area","SHAPE.AREA","SHAPE.LEN"]
	dropFields = [x.name for x in fields if x.name not in keepFields]
	arcpy.DeleteField_management(table, dropFields)
	del dropFields
	arcpy.AddMessage("\tUnecessary fields removed...")


	# Add Fields
		# Domains attached to DISTRICT, STATUS and TYPE fields (domain name = field name)
		# Make sure filter list in script matches current domains
		# [FieldEdit]
	fields = [
		("FILE_NUMBER", "TEXT", "40", "", "", "", "NULLABLE", "NON_REQUIRED",""),
		("DISTRICT", "TEXT", "20", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
		("WARD", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
		("AREA_WARD", "TEXT", "256", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
		("TYPE", "TEXT", "50", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
		("PARCEL_COUNT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
		("IMPORT_DATE", "DATE", "", "", "","", "NULLABLE","NON_REQUIRED", ""),
		("DATE_SUBMITTED", "TEXT", "50", "", "","", "NULLABLE","NON_REQUIRED", ""),
		("SITE_ADDRESS", "TEXT", "4000", "", "","", "NULLABLE","NON_REQUIRED", ""),
		("STATUS", "TEXT", "50", "", "","", "NULLABLE","NON_REQUIRED", ""),
		("TRUE_DATE", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "" ),
		("DESCRIPTION", "TEXT", "4000", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
		("CREATED_BY", "TEXT", "255", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	]

	arcpy.AddMessage("\tAdding new fields...")
	for f in fields:
		arcpy.AddField_management(*(table,) + f)

	# arcpy.AddField_management(table,"FILE_NUMBER", "TEXT", "40", "", "", "", "NULLABLE", "NON_REQUIRED","")
	# arcpy.AddField_management(table,"DISTRICT", "TEXT", "20", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	# arcpy.AddField_management(table,"WARD", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""),
	# arcpy.AddField_management(table,"AREA_WARD", "TEXT", "256", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	# arcpy.AddField_management(table,"TYPE", "TEXT", "50", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	# arcpy.AddField_management(table,"PARCEL_COUNT", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	# arcpy.AddField_management(table,"IMPORT_DATE", "DATE", "", "", "","", "NULLABLE","NON_REQUIRED", "")
	# arcpy.AddField_management(table,"DATE_SUBMITTED", "TEXT", "50", "", "","", "NULLABLE","NON_REQUIRED", "")
	# arcpy.AddField_management(table,"SITE_ADDRESS", "TEXT", "4000", "", "","", "NULLABLE","NON_REQUIRED", "")
	# arcpy.AddField_management(table,"STATUS", "TEXT", "50", "", "","", "NULLABLE","NON_REQUIRED", "")
	# arcpy.AddField_management(table,"TRUE_DATE", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "" )
	# arcpy.AddField_management(table,"DESCRIPTION", "TEXT", "4000", "", "", "", "NULLABLE", "NON_REQUIRED", "")
	# arcpy.AddField_management(table,"CREATED_BY", "TEXT", "255", "", "", "", "NULLABLE", "NON_REQUIRED", "")


	# zDsc = arcpy.Describe(table)
	# fields = zDsc.fields
	# for field_test in fields:
		# arcpy.AddMessage("{0} is a type of {1} with a length of {2}".format(f.name, f.type, f.length))
	# del zDsc
	# del fields

	arcpy.AddMessage("\tChecking for AROLL field...")
	if findField(table, "AROLL") == False:
		arcpy.AddField_management(table, "AROLL", "TEXT", "20", "","","","NULLABLE", "NON_REQUIRED","")

	# listFields = arcpy.ListFields(table)
	# for field in listFields:
		# if field.name == "AROLL":
			# xField = True
			# if xField <> True:
				# arcpy.AddField_management(table, "AROLL", "TEXT", "20", "","","","NULLABLE", "NON_REQUIRED","")
	# arcpy.AddMessage("\tFields created")
	# arcpy.AddMessage("\n" * 2)
	# Calculate Fields
		# Updating new fields with user inputs
		# [FieldEdit]

	calcFields = [
		("FILE_NUMBER", '"' + combined + '"', "PYTHON_9.3", ""),
		("SITE_ADDRESS", '"' + siteAddress + '"', "PYTHON_9.3", ""),
		("DISTRICT", '"' + section + '"', "PYTHON_9.3", ""),
		("WARD",  ward, "PYTHON_9.3", ""),
		("AREA_WARD", '"' + wardName +'"', "PYTHON_9.3", ""),
		("TYPE", '"' + type + '"', "PYTHON_9.3", ""),
		("PARCEL_COUNT", pCount, "PYTHON_9.3", ""),
		("DATE_SUBMITTED", '"' + submitDate + '"', "PYTHON_9.3",""),
		("STATUS", '"' + status + '"', "PYTHON_9.3",""),
		("TRUE_DATE", '"' + submitDate + '"', "PYTHON_9.3", ""),
		("DESCRIPTION", '"""' + desc + '"""', "PYTHON_9.3", "")
	]
	arcpy.AddMessage("---" * 3)
	arcpy.AddMessage("Processing Data")
	arcpy.AddMessage("---" * 3)
	arcpy.AddMessage("\tCalculating fields...")

	for field in calcFields:
		arcpy.CalculateField_management(*(table,) + field)
	arcpy.AddMessage("\tFields calculated")

	with arcpy.da.UpdateCursor(table,["IMPORT_DATE","CREATED_BY"]) as rows:  # Updating string time field
		for row in rows:
			row[0] = datetime.date.today().strftime("%m/%d/%Y")
			row[1] = getpass.getuser()
			rows.updateRow(row)
			#row[1] = arcpy.ConvertTimeField_management(table, "DATE_SUBMITTED", "MM/dd/yyyy HH:mm:ss","TRUE_DATE")




	# Dissolving parcels into one row
	# [FieldEdit]
	arcpy.AddMessage("\tDissolving fields...") #TRUE_DATE FIRST;
	arcpy.Dissolve_management(table,dtable,"", "DATE_SUBMITTED FIRST; FILE_NUMBER FIRST; DISTRICT FIRST; WARD FIRST; TYPE FIRST; PARCEL_COUNT MEAN; IMPORT_DATE FIRST; AROLL FIRST; SITE_ADDRESS FIRST; STATUS FIRST; TRUE_DATE FIRST; DESCRIPTION FIRST; CREATED_BY FIRST; AREA_WARD FIRST", "MULTI_PART","DISSOLVE_LINES")
	arcpy.AddMessage("\tDissolve Complete")
	arcpy.AddMessage("---" * 3)

	#-- Updating table in GDB using Append_management --#
	# File--> Reload cache if you are in table view, to see updated rows
	# Update cursor does not work (won't bring shape fields from sde)
	# Listing names of dissolved fields
	dsc = arcpy.Describe(dtable)
	fields = dsc.fields
	# Field mapping
	field_mappings = arcpy.FieldMappings()
	#for field_test in fields:
		#arcpy.AddMessage("{0} is a type of {1} with a length of {2}".format(field_test.name, field_test.type, field_test.length))
	for field in fields:
		# if not field.name == "OBJECTID" and not field.name == "SHAPE" and not field.name == "Shape":
		# ERROR 000224 occurs here
		if  not field.name == "OID" and not field.name == "SHAPE":
			old_name = field.name

			# Rename if necessary
			if old_name.startswith("FIRST_"):
				new_name = old_name.split('_', 1)[-1]
				#arcpy.AddMessage("new name of First: " + str(new_name))

			elif old_name.startswith("MEAN_"):
				new_name = old_name.split('_',1)[-1]
				#arcpy.AddMessage("new name of Mean: " + str(new_name))
			else:
				new_name = old_name
				#arcpy.AddMessage("new name of Existing: " + str(new_name))

			# Create new FieldMap object
			new_f = arcpy.FieldMap()
			new_f.addInputField(dtable,old_name) # Specify the input field to use
			# Rename output field
			new_f_name = new_f.outputField
			new_f_name.name = new_name
			new_f_name.aliasName = new_name
			new_f.outputField = new_f_name
		# Add field to FieldMappings object
		field_mappings.addFieldMap(new_f)
	arcpy.AddMessage("Updating geodatabase...")
	arcpy.Append_management(dtable, out_location, "NO_TEST", field_mappings, "")
	arcpy.AddMessage("Your parcel has successfully been saved into the location: \n\t" + str(out_location))



	# Add updated parcel to the map (in memory), focus and zoom on its extent
	mxd = arcpy.mapping.MapDocument("CURRENT")
	df = arcpy.mapping.ListDataFrames(mxd)[0] # change if Data Frame name changes
	arcpy.AddMessage("Zooming to processed parcels...")
	arcpy.MakeFeatureLayer_management(out_location, r"in_memory\def_lyr",'"FILE_NUMBER" = ' + "'%s'" %combined )
	player = arcpy.mapping.Layer(r"in_memory\def_lyr")
	player.name = str(siteAddress) # Site Address
	arcpy.mapping.AddLayer(df, player, "TOP") # Add to map
	updateLayer = arcpy.mapping.ListLayers(mxd, player, df)[0]
	sourceLayer = arcpy.mapping.Layer(r"\\VS-173-PLNGRA02\PLNGRA02\PLN\pln\Urbandesign\GRAPHICS\zResource\StoredParcels\zData\Site.lyr") # Site.lyr symbology layer
	arcpy.ApplySymbologyFromLayer_management(updateLayer, sourceLayer) # Apply symbology from Site.lyr
	arcpy.RefreshActiveView()
	ext = player.getExtent() # Zoom to extent
	df.extent = ext
	del mxd, df, player, ext


# TO DO: Raise exception if pcount of target = count of selected parcels

except Exception as e:
	print e.message
	arcpy.AddError(e.message)
finally:
	arcpy.AddMessage("Clearing memory...")
	if arcpy.Exists("in_memory\tempLayer"):
		arcpy.Delete_management("in_memory\tempLayer")
	if arcpy.Exists("in_memory\tableLayer"):
		arcpy.Delete_management("in_memory\tableLayer")
	arcpy.RefreshActiveView()
