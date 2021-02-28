import arcpy.mapping as mapping
mxd = mapping.MapDocument(r'C:\EsriTraining\PythEveryone\CreatingScripts\replaceLayer.mxd')
df = mapping.ListDataFrames(mxd, "Crime")[0]
lyr = mapping.ListLayers(mxd, "SD_Stream", df)[0]
lyr.replaceDataSource(r'C:\EsriTraining\PythEveryone\CreatingScripts', "SHAPEFILE_WORKSPACE", "SD_STREAM")
mxd.saveACopy(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\replaceLayers2.mxd')
print "script complete!"