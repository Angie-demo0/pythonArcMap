import arcpy.mapping as mapping 
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if (df.name == 'Crime'):
        layers = mapping.ListLayers(mxd, 'Prov*', df)
        for layer in layers:
            print layer.name
            

