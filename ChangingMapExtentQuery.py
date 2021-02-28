import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if (df.name == 'Crime'):
        layers = mapping.ListLayers(mxd, 'Prov_indBuildings', df)
        for layer in layers:
            query = '"CLASS" = \'City\''
            layer.definitionQuery = query
            df.extent = layer.getExtent()
            


