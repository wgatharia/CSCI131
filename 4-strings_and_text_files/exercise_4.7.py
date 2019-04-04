"""
    File: exercise_4.7.py
    Author: William Gatharia
    This code demonstrates reading a pipe delimited text file.
"""

#create file object

f = open('data.txt', 'r')

#loop through the lines
linenumber = 0
for line in f:
    #remove new line character
    line = line.strip()
    line_list = line.split('|')
    if linenumber == 0:
        #print header
        print("%12s%12s%30s%10s" % (line_list[0], line_list[1], line_list[2], line_list[3]))
    else:
        #print data
        print("%12s%12s%30s%10s" % (line_list[0], line_list[1], line_list[2], line_list[3]))
    linenumber += 1
f.close()

