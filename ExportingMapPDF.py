import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
mapping.ExportToPDF(mxd,r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Map_PageLayout.pdf' )

