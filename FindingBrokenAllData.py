import arcpy.mapping as mapping, os
path = r'C:\EsriTraining'
f = open('BrokenDataList.txt', 'w')
for root, dirs, files in os.walk(path):
    for filename in files:
        basename, extension = os.path.splitext(filename)
        if extension == ".mxd":
            fullPath = os.path.join(path, filename)
            mxd = mapping.MapDocument(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Crime_DataLinksFixed.mxd')
            f.write("MXD: " + filename + "\n")
            brknList = mapping.ListBrokenDataSources(mxd)
            for brknItem  in brknList:
                f.write("\t" + brknItem.name + "\n")
f.close()
print "script complete!"