#!/usr/bin/python

import os
import sys
import getopt
import argparse
import csv

# get command line args
argp = argparse.ArgumentParser(description='script to merge directory of csv files to a single csv file')
argp.add_argument('-d', '--directory', help='input directory', required=True)
argp.add_argument('-o', '--ofilename', help='output filename', default='dump.csv')
args = argp.parse_args()

# parse the headers
# ...

# parse the files
with open(ofilename, 'w') as ofile:
    dict_writer = None
    for f in os.listdir(directory):
        if f.endswith('.csv'):
            print('Parsing: '+f)
            with open(directory+'/'+f, 'r') as ifile:
                dict_reader = csv.DictReader(ifile, fieldnames=headers)
                if not dict_writer:
                    dict_writer = csv.DictWriter(ofile, lineterminator='\n', fieldnames=headers)
                    dict_writer.writeheader()
                for row in dict_reader:
                    dict_writer.writerow(row)

