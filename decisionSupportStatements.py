import arcpy

#Assign variables
fc = r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\Schools'
fcName = "Schools"

#Statement if/elif/else
if fcName == 'Schools':
    arcpy.Buffer_analysis(fc, r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\SchoolsBuffer', 1000)
elif fcName == 'Rail':
    arcpy.Buffer_analysis(fc, r'C:\EsriTraining\PythEveryone\PythonInArcGIS\RhodeIsland.gdb\RailBuffer', 100)
else:
    print "Can't buffer this layer"

print "Scripting ready!"

