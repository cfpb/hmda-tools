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

from hmda_tools.cbsa import load_cbsa

parser = argparse.ArgumentParser(description='Import Dec 2009 Census CBSA data and load it into a database.')
parser.add_argument('db_uri', help='connection string for the database')
args = parser.parse_args()
load_cbsa(args.db_uri)
    
