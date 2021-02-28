import arcpy.mapping as mapping


mxd = mapping.MapDocument("CURRENT")
print mapping.ListLayers(mxd)
