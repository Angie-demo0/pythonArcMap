import arcpy 
arcpy.env.workspace = r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb'
try:
>>> import arcpy 
>>> arcpy.env.workspace = r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb'
>>> try:
...     flayer = arcpy.MakeFeatureLayer_management("RI_Schools","RI_Schools_Layer")
... except:
...     print "An error ocurred during creation"
