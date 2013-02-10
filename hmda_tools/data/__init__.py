from sqlalchemy import MetaData, create_engine

from . import schemas

def create_schemas(db_uri):
    metadata = MetaData(create_engine(db_uri))
    
    schemas.hmda(metadata)
    schemas.state(metadata)
    schemas.county(metadata)
    schemas.cbsa(metadata)
    schemas.action_taken(metadata)
    schemas.agency(metadata)
    schemas.denial_reason(metadata)
    schemas.edit_status(metadata)
    schemas.ethnicity(metadata)
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
    
    metadata.create_all()

def load_hmda(db_uri, year):
    pass
