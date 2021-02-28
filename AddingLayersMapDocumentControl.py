import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd, "Crime")[0]
refLayer = mapping.ListLayers(mxd, "SD_Stream", df)[0]
insertLayer = mapping.Layer(r'C:\SIGS\work\moverte\SHP\Tehuacan_Cuicatlan.gdb\Linea_transmision')
mapping.InsertLayer(df, refLayer, insertLayer, "BEFORE")


