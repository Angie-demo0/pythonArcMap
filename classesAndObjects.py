import arcpy
fc = "D:\SIGS\work\moverte\SHP\Microlocalizacion.gdb\ANP"

#Fetch each feature from the cursor and examine the extent properties
#and spatial reference
for row in arcpy.da.SearchCursor(fc, ["SHAPE@"]):
    #get the extent of the country boundary
    ext = row[0].extent
    #print out the bounding coordinates and spatial reference
    print ("XMin: " + str(ext.XMin))
    print ("XMax: " + str(ext.XMax))
    print ("YMin: " + str(ext.YMin))
    print ("YMax: " + str(ext.YMax))
    print ("Spatial Reference: " + ext.spatialReference.name)


print ("scripting complet")



