import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
frames = mapping.ListDataFrames(mxd, "L*")
for df in frames:
    print df.name
    

