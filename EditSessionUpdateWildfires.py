#-------------------------------------------------------------------------------
# Name:         
# Purpose:      
#
# Author:      Angie Torres
#
# Created:     
#-------------------------------------------------------------------------------

import arcpy, os
arcpy.env.workspace = r"D:\SIGS\Programacion\cursoPython.gdb"

try:
    edit = arcpy.da.Editor('D:\SIGS\Programacion\cursoPython.gdb')
    edit.startEditing(True)
    with arcpy.da.UpdateCursor("TestNoise",("NAME_1","PROMEDIO_DB","MINIMO_DB","MAXIMO_DB", "NIVEL_ACUS")) as cursor:
        cntr = 1
        for row in cursor:
            #update the nivel_acus field
            
            #Promedio_db is >= 70 but < 73 = POOR
            #Promedio_db is >= 73 but < 75 = MEDIUM
            #Promedio_db is >= 75 = CRITICAL
            
            if row[1] >= 70 and row[1] < 73.7:
                row[4] = 'POOR'
                cursor.updateRow(row)
            elif row[1] >= 73.7 and row[1] < 75.842857:
                row[4] = 'MEDIUM'
                cursor.updateRow(row)
            else:
                row[1] = 'CRITICAL'
                cursor.updateRow(row)
        print "Record number " + str(cntr) + " updated"
        cntr = cntr + 1
    edit.stopEditing(True)
except Exception as e:
    print e.message 
