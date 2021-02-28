import arcpy.mapping as mapping 
mxd = mapping.MapDocument("CURRENT")
for el in mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "*fil*"):
    print el.name
    

