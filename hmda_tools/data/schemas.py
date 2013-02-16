from sqlalchemy import *


def hmda(metadata):
    return Table('hmda', metadata,
                 Column('year', Integer, nullable=False, index=True),
                 Column('respondent', String(10)),
                 Column('agency', Integer),
                 Column('loan_type', Integer),
                 Column('property_type', Integer),
                 Column('loan_purpose', Integer),
                 Column('occupancy', Integer, index=True),
                 Column('loan_amount', Integer, index=True),
                 Column('preapproval', Integer),
                 Column('action_type', Integer),
                 Column('msa_md', Integer, index=True),
                 Column('state_code', Integer, index=True),
                 Column('county_code', Integer),
                 Index('state_code', 'county_code'),
                 Column('census_tract_number', String(8), index=True),
                 Column('applicant_ethnicity', Integer, index=True),
                 Column('co_applicant_ethnicity', Integer),
                 Column('applicant_race_1', Integer),
                 Column('applicant_race_2', Integer),
                 Column('applicant_race_3', Integer),
                 Column('applicant_race_4', Integer),
                 Column('applicant_race_5', Integer),
                 Column('co_applicant_race_1', Integer),
                 Column('co_applicant_race_2', Integer),
                 Column('co_applicant_race_3', Integer),
                 Column('co_applicant_race_4', Integer),
                 Column('co_applicant_race_5', Integer),
                 Column('applicant_sex', Integer),
                 Column('co_applicant_sex', Integer),
                 Column('applicant_income', Integer),
                 Column('purchaser_type', Integer),
                 Column('denial_reason_1', Integer),
                 Column('denial_reason_2', Integer),
                 Column('denial_reason_3', Integer),
                 Column('rate_spread', String(10)),
                 Column('hoepa_status', Integer),
                 Column('lien_status', Integer),
                 Column('edit_status', Integer),
                 Column('sequence_number', Integer),
                 Column('population', Integer),
                 Column('minority_population', Float),
                 Column('hud_median_family_income', Integer),
                 Column('tract_to_msa', Float),
                 Column('number_of_owner_occupied_units', Integer),
                 Column('number_of_family_units', Integer),
                 Column('application_date_indicator', Integer))


def CodeTable(name, metadata):
    return Table(name, metadata,
                 Column('id', Integer, primary_key=True),
                 Column(name, String(255), nullable=False))


def action_taken(metadata):
    return CodeTable('action_taken', metadata)


def agency(metadata):
    return Table('agency', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('agency_abbr', String(10), nullable=False),
                 Column('agency', String(255), nullable=False))


def denial_reason(metadata):
    return CodeTable('denial_reason', metadata)


def edit_status(metadata):
    return CodeTable('edit_status', metadata)


def ethnicity(metadata):
    return CodeTable('ethnicity', metadata)


def hoepa(metadata):
    return CodeTable('hoepa', metadata)


def lien_status(metadata):
    return CodeTable('lien_status', metadata)


def loan_purpose(metadata):
    return CodeTable('loan_purpose', metadata)


def loan_type(metadata):
    return CodeTable('loan_type', metadata)


def owner_occupancy(metadata):
    return CodeTable('owner_occupancy', metadata)


def preapproval(metadata):
    return CodeTable('preapproval', metadata)


def property_type(metadata):
    return CodeTable('property_type', metadata)


def purchaser_type(metadata):
    return CodeTable('purchaser_type', metadata)


def race(metadata):
    return CodeTable('race', metadata)


def sex(metadata):
    return CodeTable('sex', metadata)


def state(metadata):
    return Table('state', metadata,
                 Column('fips_code', Integer, primary_key=True),
                 Column('abbr', String(2), nullable=False))


def county(metadata):
    return Table('county', metadata,
                 Column('county_fips_code', Integer, nullable=False),
                 Column('state_fips_code', Integer, nullable=False),
                 PrimaryKeyConstraint('county_fips_code', 'state_fips_code'),
                 Column('ansi_code', String(8), nullable=False),
                 Column('cbsa_code', Integer, nullable=True),
                 Column('name', String(255), nullable=False),
                 Column('population', Integer),
                 Column('housing_units', Integer),
                 Column('land_area', BigInteger),
                 Column('water_area', BigInteger),
                 Column('latitude', String(20)),
                 Column('longitude', String(20)))


def cbsa(metadata):
    return Table('cbsa', metadata,
                 Column('cbsa_code', Integer, primary_key=True),
                 Column('parent_code', Integer, nullable=True),
                 Column('name', String(255), nullable=False))
