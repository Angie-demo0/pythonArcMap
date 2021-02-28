import arcpy 
arcpy.env.workspace = r'C:\EsriTraining\PythEveryone\HandleErrors\SanDiego.gdb'
arcpy.Buffer_analysis("SD_Stream", "SD_Stream800", "800 Meters")

