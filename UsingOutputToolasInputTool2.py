import arcpy
arcpy.env.workspace = r"C:\SIGS\work\moverte\SHP\Cartografía Rural Censo 2010 INEGI\211560002"
try:
    vias = "211560002E.shp"
    viasBuffer = "211560002EBuffer.shp"
    distance = "50 Meters"
    equipamientos = "211560002SIP.shp"
    arcpy.Buffer_analysis(vias,viasBuffer,distance,'FULL','ROUND','ALL')
    arcpy.MakeFeatureLayer_management(equipamientos, 'equipamientos_lyr')
    arcpy.SelectLayerByLocation_management('equipamientos_lyr','intersect',viasBuffer)
    print "script complete!"
except:
    print "Error in script!"
    


