import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd)[0]
layer = mapping.Layer(r'C:\Users\52222\Documents\03.Other\Work\JUANITO\Infor especifica\SIGS\Cuacnopalan.lyr')
mapping.AddLayer(df, layer, "AUTO_ARRANGE")


