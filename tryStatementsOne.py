import arcpy
import sys

inFeatureClass = arcpy.GetParameterAsText(0)
outFeatureClass = arcpy.GetParameterAsText(1)

try:
    # If the output feature class exists, raise an error
    if arcpy.Exists(inFeatureClass):
        raise overwriteError(outFeatureClass)
    else:
        # Additional processing steps

except overwriteError as e:
    # Use message ID 12, and provide the output feature class
    # to complete the message
    
    arcpy.AddIDMessage("Error", 12, str(e))

