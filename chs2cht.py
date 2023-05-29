#!/bin/env python3

import csv
import sys

# convert csv to dictionary
with open( 'chs2cht.csv','r' ) as csvfile:
    reader = csv.reader( csvfile )
    mydict = { rows[0]:rows[1] for rows in reader }

# loop through each .srt file and create output file
for i in range( 1, len( sys.argv )):
    if len( sys.argv ) > 0 and sys.argv[i].endswith( '.srt' ): 
        infile = open( sys.argv[i],'r' )
        outfile = open( sys.argv[i].replace( '.srt','.cht.srt' ),'w' )

        for line in infile:
            for e in line:
                if e in mydict:
                    e = e.replace( e, mydict[e] )
                    print( e,end='' )
                outfile.write( e )

        infile.close()
        outfile.close()

        print( "done" )

    else:
        print( "not an srt file" )




