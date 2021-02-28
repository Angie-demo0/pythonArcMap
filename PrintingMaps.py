import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if df.name == "Microlocalizacion":
        mapping.PrintMap(mxd, "", df)
        

