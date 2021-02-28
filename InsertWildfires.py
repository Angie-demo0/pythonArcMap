import arcpy, os
try:
    outputFC = arcpy.GetParameterAsText(0)
    fClassTemplate = arcpy.GetParameterAsText(1)
    f = open(arcpy.GetParameterAsText(2),'r')
    arcpy.CreateFeatureclass_management(os.path.split(outputFC)[0],os.path.split(outputFC[1]),"Point",fClassTemplate)
    lstFires = f.readlines()
    cur = arcpy.InsertCursor(outputFC)
    cntr = 1
    for fire in lstFires:
        if 'Latitude' in fire:
            continue
        vals = fire.split(",")
        latitude = float(vals[0])
        longitude = float(vals[1])
        confid = int(vals[2])
        pnt = arcpy.Point(longitude, latitude)
        feat = cur.newRow()
        feat.shape = pnt
        feat.setValue("CONFIDENCEVALUE", confid)
        cur.insertRow(feat)
        arcpy.AddMessage("Record number: " + str(cntr) + " written to feature class")
        cntr = cntr + 1
    except:
        print arcpy.GetMessages()
    finally:
        del cur
        f.close()
        