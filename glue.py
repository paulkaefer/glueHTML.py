# glue.py
# 
# "glue" a bunch of html files in a directory together
#
# read list of files in a directory: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python

# get folder path from sys/argv

from os import listdir
from os.path import isfile, join
from sys import argv

folderPath = argv[1]

# for each file in folder

fileList = [ f for f in listdir(folderPath) if isfile(join(folderPath, f)) ]

fileNumber = 1

for fileName in fileList:
    thisFile = open(fileName, 'r')
    
    if 1 == fileNumber:
        keepReading = 1
        for line in thisFile:
            if -1 < string.find(line, "</body"):
                keepReading = 0
            
    
    thisFile.close()
    fileNumber = fileNumber + 1

# first one: read up until
#   </body>
# (discard rest)

# for next files,
# read between <body *> ... </body>
# throw out "header" and "footer"

# for LAST file (you know the count: len(dir) or something like it)
# read from end of <body *>
# until end of file (include "footer")

# "stitch it all together" into one file

# run on: a-z.html; Swahili versions
# also: "other files" on both English and Swahili

