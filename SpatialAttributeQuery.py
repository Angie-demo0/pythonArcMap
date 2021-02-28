#-----------------------------------------------------------------------------------------------------------------------------------------------
# Name:         Combining a spatial and attribute query with the Select by Location tool
# Purpose:      
#
# Author:      Angie Torres
#
# Created:     06/07/2020
# Copyright:   (c) Angie 2020
#-----------------------------------------------------------------------------------------------------------------------------------------------

import arcpy

#Set the workspace to the RhodeIsland geodatabase
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"

try:
    #Create a variable for the query and define the where clause
    qry = '"CONFIDENCEVALUE" = \'30\''

    #Create the feature layer
    flayer = arcpy.MakeFeatureLayer_management("RI_Schools","RI_Schools_Layer")

    #Execute the Select by Location tool to find all school within the providence
    arcpy.SelectLayerByLocation_management(flayer, "COMPLETELY_WITHIN", "C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\Providence")

    #Execute the Select by Attributes tool to find all schools that match the query we defined previously in the qry variable
    arcpy.SelectLayerByAttribute_management(flayer, "SUBSET_SELECTION", qry)

    #Print the number of records that were selected
    cnt = arcpy.GetCount_management(flayer)
    print "The total number of selected record is: " + str(cnt)
except:
    print "Error in selectin"