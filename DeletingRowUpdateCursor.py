#-------------------------------------------------------------------------------
# Name:         Deleting rows with an UpdateCursor 
# Purpose:      
#
# Author:      
#
# Created:     07/12/2020
#-------------------------------------------------------------------------------

import arcpy, os
arcpy.env.workspace = r"D:\SIGS\Programacion\cursoPython.gdb"
try:
   with arcpy.da.UpdateCursor("TestNoise", ("NIVEL_ACUS"),""""NIVEL_ACUS" = 'MEDIUM'""") as cursor:
      cntr = 1
      for row in cursor:
         cursor.deleteRow()
         print "Record number " + str(cntr) + " deleted"
         cntr = cntr + 1
         print 'ready'
except Exception as e:
   print e.message
   
         
   
