import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection

from .. import data
from ..data import schemas


def test_create_schemas(tmpdir):
    db_uri = "sqlite:///%s/test.db" % tmpdir
    print db_uri
    data.create_schemas(db_uri)

    engine = create_engine(db_uri)
    insp = reflection.Inspector.from_engine(engine)

    expected_tables = [
        'action_taken',
        'agency',
        'cbsa',
        'county',
        'denial_reason',
        'edit_status',
        'ethnicity',
        'hmda',
        'hoepa',
        'lien_status',
        'loan_purpose',
        'loan_type',
        'owner_occupancy',
        'preapproval',
        'property_type',
        'purchaser_type',
        'race',
        'sex',
        'state',
    ]

    assert expected_tables == insp.get_table_names()
