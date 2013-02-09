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


import csv, codecs, cStringIO

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


import argparse
import zipfile
import csv
import string

import requests
from sqlalchemy import *

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
    gazetteer_url = 'http://www.census.gov/geo/www/gazetteer/files/Gaz_counties_national.zip'
    r = requests.get(gazetteer_url)
    if r.status_code == 200:
        with open(gaz_file, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)

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
    
