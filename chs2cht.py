#!/bin/env python

import csv

# convert csv to dictionary
with open( 'chs2cht.csv','r' ) as csvfile:
    reader = csv.reader( csvfile )
    mydict = { rows[0]:rows[1] for rows in reader }

infile = open( 'subtitles.chs.srt','r' )
outfile = open( 'subtitles.cht.srt','w' )

for line in infile:
    outfile.write( line )

infile.close()
outfile.close()


