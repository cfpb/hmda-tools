# This script downloads the Dec 2009 Core-Based Statistical Area codes
# from the US Census and loads this data into a database.

# You will end up with the following tables.

# cbsa
# cbsa_code - Core Based Statistical Area code
# parent_code - Parent CBSA, if applicable
# name - Area name

import os, re, string, tempfile

from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine

from .. import download_file
from ..unicode_csv import UnicodeReader

def load_cbsa(db_uri):
    filename = download_cbsa()

    engine = create_engine(db_uri)
    metadata = MetaData()
    table = Table('cbsa', metadata,
                  Column('cbsa_code', Integer, primary_key=True),
                  Column('parent_code', Integer, nullable=True),
                  Column('name', String(255), nullable=False))
    metadata.create_all(engine)

    insert_cbsa_data(engine, table, filename)
    
def download_cbsa():
    cbsa_url = 'http://www.census.gov/population/metro/files/lists/2009/List4.txt'
    filename = download_file(cbsa_url)
    return filename

def insert_cbsa_data(engine, table, cbsa_file):
    conn = engine.connect()
    valid_line = re.compile(r'^\d+')

    with open(cbsa_file, 'r') as fh:
        for line in fh:
            if valid_line.match(line):
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
                    conn.execute(table.insert(),
                                 cbsa_code=cbsa_code,
                                 parent_code=parent_code,
                                 name=name)
    
    
