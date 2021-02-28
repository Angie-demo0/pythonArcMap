import arcpy

try:
    arcpy.env.workspace = r'C:\EsriTraining\PythEveryone\HandleErrors\SanDiego.gdb'
    fields = arcpy.ListFields("SD_Stream")
    for fld in fields:
        print fld.name
except:
    print arcpy.GetMessages()
    

