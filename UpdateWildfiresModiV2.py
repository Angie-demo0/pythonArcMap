#-------------------------------------------------------------------------------
# Name:         Updating rows of CONFID_RATING 
# Purpose:      Classifies confidenve value
#
# Author:      Angie Torres
#
# Created:     25/07/2020
#-------------------------------------------------------------------------------

import arcpy, os
arcpy.env.workspace = r"D:\SIGS\Programacion\cursoPython.gdb"
try:
    #create a new field CONFID_RATING to hold the values
    arcpy.AddField_management("TestNoise","NIVEL_ACUS","TEXT","12")
    print "CONFID_RATING field added to Calidad_Ruido"
    with arcpy.da.UpdateCursor("TestNoise",("NAME_1","PROMEDIO_DB","MINIMO_DB","MAXIMO_DB", "NIVEL_ACUS")) as cursor:
        cntr = 1
        for row in cursor:
            #update the nivel_acus field
            
            #Promedio_db is >= 70 = CRITICAL
            #Promedio_db is >= 53 but < 70 = MEDIUM
            #Promedio_db is <53 is GOOD
            if row[1] < 53:
                row[4] = 'GOOD'
                cursor.updateRow(row)
            elif row[1] >= 53 and row[1] < 70:
                row[4] = 'MEDIUM'
                cursor.updateRow(row)
            elif row[1] > 70:
                row[4] = 'CRITICAL'
                cursor.updateRow(row)
            else:
                row[1] = 'CRITICAL'
                cursor.updateRow(row)
        print "Script complete!"
except Exception as e:
    print e.message 
