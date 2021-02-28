#-------------------------------------------------------------------------------
# Name:         SpatialDate
# Purpose:      Show Spatial Dates
#
# Author:      Angie Torres
#
# Created:     09-12-20
#-------------------------------------------------------------------------------

import arcpy, os
arcpy.env.workspace = r"D:\SIGS\Programacion\ShowSpatialDate.gdb"

try:

   #create a list of input clip
   clipList = ["manzana", "equip_edu", "equip_recreacion", "equip_salud", "RUTA", "TP"]

   #Create a buffer of 500 meters in a vial intersection
   arcpy.Buffer_analysis("Point", "D:\SIGS\Programacion\ShowSpatialDate.gdb\pointBuff", "500 Meters", "FULL", "ROUND", "ALL")
   print "buffer ready!"

   #Create a loop for clipList
   for clip in clipList:
      arcpy.Clip_analysis(clip, "pointBuff", "D:\SIGS\Programacion\ShowSpatialDate.gdb\clip" + clip, "#")
   print "clip ready!"

   #Create a table of Total POB
   arcpy.Statistics_analysis("clipmanzana", "D:/SIGS/Programacion/ShowSpatialDate.gdb/clipManzana_Statics", "POB1 SUM", "")
   print "POB SUM ready!"

   #Print TOT equipment and TOT public transport
   equiEdu = arcpy.GetCount_management("clipequip_edu")
   equiRecreacion = arcpy.GetCount_management("clipequip_recreacion")
   equiSalud = arcpy.GetCount_management("clipequip_salud")
   tp = arcpy.GetCount_management("clipTP")
   RUTA = arcpy.GetCount_management("clipRUTA")

   print "El total de equipamiento educativo es de " + str(equiEdu)
   print "El total de equipamiento recreativo es de " + str(equiRecreacion)
   print "El total de equipamiento de salud es de " + str(equiSalud)
   print "El total de transporte público que circula en esta zona es de " + str(tp)
   print "El total de transporte de RUTA que circula en esta zona es de " + str(RUTA)

   print "Script complet!"

except Exception as e:
   print e.message

      