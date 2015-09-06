# glue.py
# 
# "glue" a bunch of html files in a directory together
#
# read list of files in a directory: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
# exit with message: http://bytes.com/topic/python/answers/23611-sys-exit

from os import listdir
from os.path import isfile, join
import sys, string

if 1 == len(sys.argv):
    sys.exit("Please pass a directory.")
elif 2 == len(sys.argv):
    outputFileName = "glued-files.html"
else:
    outputFileName = sys.argv[2]

folderPath = sys.argv[1]
outputFile = open(outputFileName, 'w')

# for each file in folder

fileList = [ f for f in listdir(folderPath) if isfile(join(folderPath, f)) ]

fileNumber = 1

for fileName in fileList:
    thisFile = open(folderPath + "\\" + fileName, 'r')
    
    if 1 == fileNumber:
        keepReading = 1
        for line in thisFile:
            if -1 < string.find(line, "</body"):
                keepReading = 0
            if 1 == keepReading:
                outputFile.write(line)
    elif fileNumber < len(fileList):
        # middle files: ignore header and footer
        readLine = 0
        for line in thisFile:
            if -1 < string.find(line, "<body"):
                # start reading
                readLine = 1
            if -1 < string.find(line, "</body"):
                # stop reading
                readLine = 0
            if (1 == readLine) and (1 == lastLineGood):
                outputFile.write(line)
            lastLineGood = readLine
    else:
        # last file in directory
        readLine = 0
        for line in thisFile:
            if -1 < string.find(line, "<body"):
                # start reading
                readLine = 1
            if (1 == readLine) and (1 == lastLineGood):
                outputFile.write(line)
            lastLineGood = readLine
    
    thisFile.close()
    fileNumber = fileNumber + 1

# "stitch it all together" into one file

# run on: a-z.html; Swahili versions
# also: "other files" on both English and Swahili

