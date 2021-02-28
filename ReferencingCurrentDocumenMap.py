import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
print mxd.title
mxd.title = "Copy of Crime Project"
mxd.saveACopy(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Crime_Ch3Copy.mxd')


