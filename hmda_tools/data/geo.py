import os, re, string, tempfile, zipfile, csv

import sqlsoup

from .. import download_file
from ..unicode_csv import UnicodeReader

def csv_row_to_dict(headers, row):
    return dict(zip(headers, map(string.strip, row)))

def load_all(db_uri):
    load_gazetteer(db_uri)
    load_crosswalk(db_uri)

def load_gazetteer(db_uri):
    print "Downloading gazetteer..."
    gaz_zip = download_gazetteer()
    print "Unzipping gazetteer..."
    gaz_file = unzip_gazetteer(gaz_zip)
    print "Inserting gazetteer data..."
    insert_gaz_data(db_uri, gaz_file)
    os.remove(gaz_file)

def load_crosswalk(db_uri):
    print "Downloading crosswalk data..."
    filename = download_crosswalk()
    print "Inserting crosswalk data..."
    insert_crosswalk_data(db_uri, filename)

def download_gazetteer():
    gaz_url = 'http://www.census.gov/geo/www/gazetteer/files/Gaz_counties_national.zip'
    return download_file(gaz_url)

def unzip_gazetteer(gaz_zip_file):
    gaz_txt_file = 'Gaz_counties_national.txt'
    gaz_zip = zipfile.ZipFile(gaz_zip_file)
    gaz_zip.extract(gaz_txt_file)
    return gaz_txt_file

def insert_gaz_data(db_uri, gaz_file):
    db = sqlsoup.SQLSoup(db_uri)
    db.state.delete()
    db.county.delete()
    
    with open(gaz_file, 'rb') as csvfile:
        reader = UnicodeReader(csvfile, dialect='excel-tab', encoding='iso-8859-2')
        headers = map(string.strip, reader.next())

        states_seen = set()
        
        for row in reader:
            row = csv_row_to_dict(headers, row)
            geoid = row['GEOID']
            state_fips = int(geoid[0:2])
            county_fips = int(geoid[2:5])

            if state_fips not in states_seen:
                db.state.insert(fips_code=state_fips, abbr=row['USPS'])
                states_seen.add(state_fips)

            db.county.insert(
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
            
    db.commit()

def download_crosswalk():
    crosswalk_url = "http://www.nber.org/cbsa-msa-fips-ssa-county-crosswalk/2011/FY%2011%20NPRM%20County%20to%20CBSA%20Xwalk.txt"
    return download_file(crosswalk_url)

def insert_crosswalk_data(db_uri, filename):
    db = sqlsoup.SQLSoup(db_uri)
    
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, dialect='excel-tab')
        headers = map(string.strip, reader.next())

        for row in reader:
            row = csv_row_to_dict(headers, row)
            geoid = row['fipscd']
            state_fips = int(geoid[0:2])
            county_fips = int(geoid[2:5])

            if row['CBSA']:                
                db.county.filter_by(state_fips_code=state_fips,
                                 county_fips_code=county_fips).update({
                                     'cbsa_code': int(row['CBSA'])})
    db.commit()

