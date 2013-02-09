#!/usr/bin/env python

# This script downloads the 2010 county gazetteer data from the US Census
# and loads this data into a database. You will end up with the following
# tables.

# state
# fips_code - integer FIPS code used for lookup from HMDA data
# abbr - state abbreviation used by USPS

# county
# fips_code - integer FIPS code used for lookup from HMDA data
# ansi_code - ANSI code for county
# name - county name
# population - 2010 Census population count
# housing_units - 2010 Census housing unit count
# land_area - land area in square meters
# water_area - water area in square meters

import sys
import os
sys.path.append(os.getcwd())

import argparse
import zipfile
import csv
import string

from sqlalchemy import *

from hmda_tools import download_file
from hmda_tools.unicode_csv import UnicodeReader

parser = argparse.ArgumentParser(description='Import 2010 Census county gazetteer data and load it into a database.')
parser.add_argument('conn_str', help='connection string for the database')

args = parser.parse_args()

engine = create_engine(args.conn_str)

metadata = MetaData()

state = Table('state', metadata,
              Column('fips_code', Integer, primary_key=True),
              Column('abbr', String(2), nullable=False))

county = Table('county', metadata,
               Column('county_fips_code', Integer, nullable=False),
               Column('state_fips_code', Integer, nullable=False),
               UniqueConstraint('county_fips_code', 'state_fips_code'),
               Column('ansi_code', String(8), nullable=False),
               Column('name', String(255), nullable=False),
               Column('population', Integer),
               Column('housing_units', Integer),
               Column('land_area', BigInteger),
               Column('water_area', BigInteger),
               Column('latitude', String(20)),
               Column('longitude', String(20)))

def create_database(conn_str):
    metadata.create_all(engine)

def download_gazetteer(gaz_file):
    gaz_url = 'http://www.census.gov/geo/www/gazetteer/files/Gaz_counties_national.zip'
    download_file(gaz_url, gaz_file)

def insert_data(gaz_file):
    conn = engine.connect()
    
    with open(gaz_file, 'rb') as csvfile:
        reader = UnicodeReader(csvfile, dialect='excel-tab', encoding='iso-8859-2')
        # reader = csv.reader(csvfile, dialect='excel-tab')
        headers = map(string.strip, reader.next())

        states_seen = set()
        
        for row in reader:
            row = dict(zip(headers,
                           map(string.strip, row)))
            geoid = row['GEOID']
            state_fips = int(geoid[0:2])
            county_fips = int(geoid[2:5])


            if state_fips not in states_seen:
                ins = state.insert().values(fips_code=state_fips,
                                            abbr=row['USPS'])
                conn.execute(ins)
                states_seen.add(state_fips)

            ins = county.insert().values(
                state_fips_code=state_fips,
                county_fips_code=county_fips,
                name=row['NAME'],
                ansi_code=row['ANSICODE'],
                population=int(row['POP10']),
                housing_units=int(row['HU10']),
                land_area=int(row['ALAND']),
                water_area=int(row['AWATER']),
                latitude=row['INTPTLAT'],
                longitude=row['INTPTLONG'])
            
            conn.execute(ins)
    
if __name__ == "__main__":
    gaz_zip_file = 'Gaz_counties_national.zip'
    gaz_txt_file = 'Gaz_counties_national.txt'
    create_database(args.conn_str)
    download_gazetteer(gaz_zip_file)
    gaz_zip = zipfile.ZipFile(gaz_zip_file)
    print gaz_zip.extract(gaz_txt_file)
    insert_data(gaz_txt_file)
    
