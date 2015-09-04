# glue.py
# 
# "glue" a bunch of html files in a directory together

# get folder path from sys/argv

# for each file in folder

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

