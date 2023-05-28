#!/bin/env python

import csv

with open( 'chs2cht.csv','r' ) as csvfile:
    reader = csv.reader( csvfile )
    with open( 'newfile.csv','w' ) as outfile:
        writer = csv.writer( outfile )
        mydict = { rows[0]:rows[1] for rows in reader }

print( mydict )


