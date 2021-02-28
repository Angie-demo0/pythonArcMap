import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for el in mapping.ListLayoutElements(mxd):
    if el.name != '':
        print el.name 
        

