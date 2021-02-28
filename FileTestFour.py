import os

#variable path text
path = r'D:\Estudio Digital\15.0 Videotutoriales - Cursos\Python Arcpy\Script\songs.txt'

file = open(path, 'r')

#Repeat for each song in the text file
for line in file:
    #Let's split the line intro an array called "fields" using the ";" as a separator:
    fields = line.split(",")

    #and let's extract the data:
    songTitle = fields[0]
    artist = fields[1]
    duration = fields[2]

    #print the song
    print(songTitle + " by " + artist + " Duration: " + duration)

#It is good practice to close the file at the end to free up resources
file.close()