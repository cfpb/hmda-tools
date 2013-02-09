#!/usr/bin/env python

import sys
import os
import csv
sys.path.append(os.getcwd())

import argparse
import string

import sqlsoup

from hmda_tools import download_file, mkdir_p
from hmda_tools.unicode_csv import UnicodeReader

HMDA_COLUMNS = (
"year", "respondent", "agency", "loan_type", "property_type", "loan_purpose", "occupancy", 
"loan_amount", "preapproval", "action_type", "msa_md", "state_code", "county_code", 
"census_tract_number", "applicant_ethnicity", "co_applicant_ethnicity", "applicant_race_1",
"applicant_race_2", "applicant_race_3", "applicant_race_4", "applicant_race_5", "co_applicant_race_1",
"co_applicant_race_2", "co_applicant_race_3", "co_applicant_race_4", "co_applicant_race_5", "applicant_sex",
"co_applicant_sex", "applicant_income", "purchaser_type", "denial_reason_1", "denial_reason_2", 
"denial_reason_3", "rate_spread", "hoepa_status", "lien_status", "edit_status", "sequence_number", 
"population", "minority_population", "hud_median_family_income", "tract_to_msa", 
"number_of_owner_occupied_units", "number_of_family_units", "application_date_indicator" )

def clean_filename(name):
    trimmed = name.replace('Metropolitan Statistical Area', 'MSA')
    trimmed = trimmed.replace('Metropolitan Division', 'MD')
    slugified = trimmed.lower().replace(',', '').replace(' ','_').replace('/','+')
    return slugified

def extract_counties(db):
    counties= db.execute('select county_fips_code, state_fips_code, name as county_name, state.abbr as state_abbr from county, state where state_fips_code=fips_code')
    for county in counties:
        county_fips, state_fips, county_name, state_abbr = county
        destination_dir='extracts/county/%s' % state_abbr
        mkdir_p(destination_dir)
        outfile_name = destination_dir +'/' + clean_filename(county_name) + '.csv'
        print "writing county %s(%s) to %s"%  (county_name, state_abbr, outfile_name)
        with open(outfile_name, 'w') as outfile:
            writer=csv.writer(outfile)
            hmda_records=db.execute('select * from hmda where state_code= %s and county_code = %s' % (state_fips, county_fips))
            writer.writerow(HMDA_COLUMNS)
            for row in hmda_records:
                writer.writerow(row)
        

def extract_msas(db):
    for cbsa in db.cbsa.all():
        outfile_name=clean_filename(cbsa.name)
        print "writing MSA %s to %s.csv" % (cbsa.name, outfile_name)
        with open('extracts/msa/%s.csv' % outfile_name, 'w') as outfile:
            writer=csv.writer(outfile)
            hmda_records=db.execute('select * from hmda where msa_md = %s' % cbsa.cbsa_code)
            writer.writerow(HMDA_COLUMNS)
            for row in hmda_records:
                writer.writerow(row)



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='extract CSV for every MSA, county, and State')
    parser.add_argument('conn_str', help='connection string for the database')
    args = parser.parse_args()
    db = sqlsoup.SQLSoup(args.conn_str)
    mkdir_p('extracts/county')
    extract_counties(db)
    mkdir_p('extracts/msa')
    extract_msas(db) 
