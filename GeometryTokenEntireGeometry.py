import arcpy.da, time
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"
start = time.clock()
with arcpy.da.SearchCursor("Prov_indBuildings",("CLASS","SHAPE@")) as cursor:
    for row in cursor:
        print("The shape: {0} has a location of: {1}".format(row[0],row[1]))
        elapsed = (time.clock() - start)
        print "Execution time: " + str(elapsed)
        