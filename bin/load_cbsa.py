#!/usr/bin/env python

# This script downloads the Dec 2009 Core-Based Statistical Area codes
# from the US Census and loads this data into a database.

# You will end up with the following tables.

# cbsa
# cbsa_code - Core Based Statistical Area code
# parent_code - Parent CBSA, if applicable
# name - Area name

import sys
import os
sys.path.append(os.getcwd())

import argparse
import re
import string

from sqlalchemy import *

from hmda_tools import download_file, mkdir_p
from hmda_tools.unicode_csv import UnicodeReader

metadata = MetaData()

cbsa = Table('cbsa', metadata,
             Column('cbsa_code', Integer, primary_key=True),
             Column('parent_code', Integer, nullable=True),
             Column('name', String(255), nullable=False))

def create_database(conn_str):
    metadata.create_all(engine)

def download_cbsa(filename):
    cbsa_url = 'http://www.census.gov/population/metro/files/lists/2009/List4.txt'
    download_file(cbsa_url, filename)

def insert_cbsa_data(engine, cbsa_file):
    conn = engine.connect()
    valid_line = re.compile(r'^\d+')

    with open(cbsa_file, 'r') as cbsa_fh:
        for line in cbsa_fh:
            if valid_line.match(line):
                print line
                cbsa_code = line[0:5].strip()
                div_code = line[8:13].strip()
                fips_code = line[16:21].strip()
                name = unicode(line[24:].strip(), 'iso-8859-2')

                if not fips_code: # a CBSA definition line
                    if cbsa_code and div_code:
                        parent_code = int(cbsa_code)
                        cbsa_code = int(div_code)
                    else:
                        parent_code = None
                        cbsa_code = int(cbsa_code)
                    conn.execute(cbsa.insert(),
                                 cbsa_code=cbsa_code,
                                 parent_code=parent_code,
                                 name=name)

if __name__ == '__main__':
    mkdir_p('tmp')
    cbsa_file = 'tmp/cbsa.txt'
    
    parser = argparse.ArgumentParser(description='Import Dec 2009 Census CBSA data and load it into a database.')
    parser.add_argument('conn_str', help='connection string for the database')
    args = parser.parse_args()
    engine = create_engine(args.conn_str)

    create_database(args.conn_str)
    download_cbsa(cbsa_file)
    insert_cbsa_data(engine, cbsa_file)
    
