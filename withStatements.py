import arcpy

fc = r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\SchoolsBuffer'

# For each row print the object ID field, and use the SHAPE@AREA
# Token to access geometry properties

with arcpy.da.SearchCursor(fc, ("OID@", "SHAPE@AREA")) as cursor:
    for row in cursor:
        print ("Feature {0} has an area of {1}".format(row[0], row[1]))
                                