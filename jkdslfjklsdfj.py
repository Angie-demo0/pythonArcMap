import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"
try:
    flayer = arcpy.MakeFeatureLayer_management("RI_Schools","RI_Schools_Layer")
    arcpy.SelectLayerByLocation_management(flayer, "WITHIN_A_DISTANCE", "C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\Providence", "1 MILES")
    cnt = arcpy.GetCount_management(flayer)
    print "The number of selected records is: " + str(cnt)
except:
    print "An error ocurred during selection"

