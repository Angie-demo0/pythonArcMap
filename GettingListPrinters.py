import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for printerName in mapping.ListPrinterNames():
    print printerName
    

