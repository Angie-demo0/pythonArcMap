import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for tableView in mapping.ListTableViews(mxd):
    print tableView.name
    

