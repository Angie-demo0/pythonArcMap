import arcpy.mapping as mapping
mxd = mapping.MapDocument(r'C:\EsriTraining\PythEveryone\CreatingScripts\test1.mxd')
mxd.replaceWorkspaces(r'C:\EsriTraining\PythEveryone\CreatingScripts\RhodeIsland.gdb', "FILEGDB_WORKSPACE", r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.mdb', "ACCESS_WORKSPACE")
mxd.saveACopy(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Test2.mxd')
print "Scrip complete!"