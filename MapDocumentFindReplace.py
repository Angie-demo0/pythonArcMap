#-------------------------------------------------------------------------------
# Name:         Fixing broken data sources
# Purpose:      Fixing broken data sources, repalace the paths to multiple workspace
#
# Author:      Angie Torres
#
# Created:     08/06/2020
# Copyright:   (c) Angie 2020
#-------------------------------------------------------------------------------
import arcpy.mapping as mapping
mxd = mapping.MapDocument(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Crime_DataLinksFixed.mxd')
mxd.findAndReplaceWorkspacePaths(r'C:\EsriTraining\PythEveryone\HandleErrors\SanDiego.gdb',
r'C:\EsriTraining\PythEveryone\CreatingScripts\SanDiego.gdb')
mxd.saveACopy(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Crime_DataLinksFixedNew.mxd')
print "Script complete!"


