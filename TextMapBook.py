#-------------------------------------------------------------------------------
# Name:         Create a map book 
# Purpose:      Create a map book with PDFDocumentCreate() and PDFDocumentOpen()
#
# Author:      Angie Torres
#
# Created:     12/06/2020
# Copyright:   (c) Angie 2020
#-------------------------------------------------------------------------------
import arcpy.mapping as mapping
import os

#Set the path and filename for the map book. Remove the file if it already exists
pdfPath = r'C:\EsriTraining\PythEveryone\PythonInArcGIS\TestMapBook.pdf'
if os.path.exists(pdfPath):
    os.remove(pdfPath)
    
#Create the PDF document
pdfDoc = mapping.PDFDocumentCreate(pdfPath)

#Append existing PDF pages to the document
pdfDoc.appendPages(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\Microlocalizacion.pdf')
pdfDoc.appendPages(r'C:\EsriTraining\PythEveryone\PythonInArcGIS\New_Micro.pdf')

#Commit changes to the map book
pdfDoc.saveAndClose()

print "Script complete!"