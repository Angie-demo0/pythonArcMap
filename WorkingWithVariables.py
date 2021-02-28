import arcpy

path = r'C:\EsriTraining\PythEveryone\HandleErrors\SanDiego.gdb'
arcpy.env.workspace = path

fields = arcpy.ListFields("SD_Stream")
for fld in fields:
    print fld.name
print "Script complete"