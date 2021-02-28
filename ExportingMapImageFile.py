import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if df.name == "Microlocalizacion":
        mapping.ExportToJPEG(mxd,r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Micro.jpg',df,world_file=True)
        print "script complete!"
        

