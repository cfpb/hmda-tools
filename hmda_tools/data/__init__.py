import os
import os.path
import csv
import string

from sqlalchemy import MetaData, create_engine
import sqlsoup

from . import schemas


def csv_row_to_dict(headers, row):
    return dict(zip(headers, map(string.strip, row)))


def create_schemas(db_uri):
    engine = create_engine(db_uri)
    metadata = MetaData()

    schemas.action_taken(metadata)
    schemas.agency(metadata)
    schemas.cbsa(metadata)
    schemas.county(metadata)
    schemas.denial_reason(metadata)
    schemas.edit_status(metadata)
    schemas.ethnicity(metadata)
    schemas.hmda(metadata)
    schemas.hoepa(metadata)
    schemas.lien_status(metadata)
    schemas.loan_purpose(metadata)
    schemas.loan_type(metadata)
    schemas.owner_occupancy(metadata)
    schemas.preapproval(metadata)
    schemas.property_type(metadata)
    schemas.purchaser_type(metadata)
    schemas.race(metadata)
    schemas.sex(metadata)
    schemas.state(metadata)

    metadata.create_all(engine)
    engine.dispose()


def load_code_sheet(db_uri):
    db = sqlsoup.SQLSoup(db_uri)

    tables = [
        'action_taken',
        'agency',
        'denial_reason',
        'edit_status',
        'ethnicity',
        'hoepa',
        'lien_status',
        'loan_purpose',
        'loan_type',
        'owner_occupancy',
        'preapproval',
        'property_type',
        'purchaser_type',
        'race',
        'sex']

    for table_name in tables:
        table = db.entity(table_name)
        table.delete()
        filename = os.path.join(os.path.dirname(__file__),
                                "code_sheet_data/%s.csv" % table_name)
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            headers = map(string.strip, reader.next())
            for row in reader:
                row = csv_row_to_dict(headers, row)
                table.insert(**row)

        db.commit()


def load_hmda(db_uri, year):
    pass
