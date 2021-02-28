#-------------------------------------------------------------------------------
# Name:         Updating rows of CONFID_RATING 
# Purpose:      Classifies confidenve value
#
# Author:      Angie Torres
#
# Created:     25/07/2020
#-------------------------------------------------------------------------------

import arcpy, os
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"
try:
    #create a new field CONFID_RATING to hold the values
    arcpy.AddField_management("FireIncidents3","CONFID_RATING","TEXT","10")
    print "CONFID_RATING field added to FireIncidents"
    with arcpy.da.UpdateCursor("FireIncidents3",("CONFID","CONFID_RATING")) as cursor:
        cntr = 1
        for row in cursor:
            #update the confid_rating field
            
            #Confidence value 1 to 3 = POOR
            #Confidence value 4 to 6 = FAIR
            #Confidence value 7 to 8 = GOOD
            #Confidence value 9 to 10 = EXCELLENT
            if row[0] <= 3:
                row[1] = 'POOR'
                cursor.updateRow(row)
            elif row[0] > 3 and row[0] <= 6:
                row[1] = 'FAIR'
                cursor.updateRow(row)
            elif row[0] > 6 and row[0] <= 8:
                row[1] = 'GOOD'
                cursor.updateRow(row)
            else:
                row[1] = 'EXCELLENT'
                cursor.updateRow(row)
        print "Script complete!"
except Exception as e:
    print e.message 