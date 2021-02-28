import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"
try:
    flayer = arcpy.MakeFeatureLayer_management("RI_Schools","RI_Schools_Layer")
    arcpy.SelectLayerByLocation_management(flayer, "COMPLETELY_WITHIN", r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\Providence")
    cnt = arcpy.GetCount_management(flayer)
    print "The number of selected record is: " + str(cnt)
except:
    print "An error ocurred during selection"