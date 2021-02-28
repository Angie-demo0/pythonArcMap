import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
layers = mapping.ListLayers(mxd)
for lyr in layers:
    print lyr.name
    

