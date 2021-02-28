import arcpy.da
arcpy.env.workspace = r"C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb"
with arcpy.da.SearchCursor("Prov_indBuildings", ("OBJECTID","Shape","CLASS","AREALAND","COORX","COORY"),'"CLASS"= \'City\'') as cursor:
    for row in sorted(cursor):
        print ("Prov Building name: " + row[2])
