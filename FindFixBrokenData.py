import arcpy.mapping as mapping
mxd = mapping.MapDocument(r'C:\\EsriTraining\\PythEveryone\\PythonInArcGIS\\Crime_Ch5.mxd')
lstBrokenDS = mapping.ListBrokenDataSources(mxd)
for layer in lstBrokenDS:
    print layer.name

    print layer.name
    