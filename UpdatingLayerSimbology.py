import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
df = mapping.ListDataFrames(mxd, "Crime")[0]
updateLayer = mapping.ListLayers(mxd, "Prov_indBuildings", df)[0]
sourceLayer = mapping.Layer(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\Prov_indBuildingsTwo')
mapping.UpdateLayer(df, updateLayer, sourceLayer, True)




