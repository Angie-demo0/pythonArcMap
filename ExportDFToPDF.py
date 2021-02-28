import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if df.name == "New_Micro":
        mapping.ExportToPDF(mxd,r"C:\\EsriTraining\\PythEveryone\\PythonInArcGIS\\New.pdf",df)
        print "list"
        

