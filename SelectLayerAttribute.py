import arcpy
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"
try:
    qry = '"CLASS" = \'City\''
    flayer = arcpy.MakeFeatureLayer_management("Prov_indBuildings","Prov_indBuildings_Layer")
    arcpy.SelectLayerByAttribute_management(flayer, "NEW_SELECTION", qry)
    cnt = arcpy.GetCount_management(flayer)
    print "The number of selected records is: " + str(cnt)
except:
    print "An error ocurred during selection"