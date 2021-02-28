import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if df.name == "New_Micro":
        mapping.ExportToJPEG(mxd,r'C:\EsriTraining\PythEveryone\PythonInArcGIS\New_Micro.jpg',df)
        print "Script complete!"
        

