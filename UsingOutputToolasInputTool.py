import arcpy
arcpy.env.workspace = r"C:\SIGS\work\moverte\SHP\Cartografía Rural Censo 2010 INEGI\211560002"
try:
    vias = "211560002E.shp"
    viasBuff = "211560002EBuff.shp"
    distance = "20 Meters"
    equipment = "211560002SIP.shp"
    arcpy.Buffer_analysis(vias,viasBuff,distance,'FULL','ROUND',"ALL")
    arcpy.MakeFeatureLayer_management(equipment,'equipment_lyr')
    arcpy.SelectLayerByLocation_management('equipment_lyr','intersect',viasBuff)
    print "Script complete!"
except:
    print "Error in script!"
    

