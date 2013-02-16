Creating Databases
==================

To create a database to hold HMDA data, run the script ``hmda_create_schemas``
with a database URL as your argument. The database URL should be specified `as
it would be in SQLAlchemy`__.

.. __: http://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine

Examples:

.. code-block:: bash

    hmda_create_schemas sqlite://hmda.db
    hmda_create_schemas mysql://root@localhost/hmda
    hmda_create_schemas postgresql://peter:rabbit@10.0.0.34/hmda

You will need to install the Python libraries for your database separately.
``hmda_tools`` does not require any DB libraries, as it tries to stay agnostic.

You can also create these schemas programatically using
:py:func:`hmda_tools.data.create_schemas`.

The created schema will look like the following (dependent on database):

.. generate by running "mysqldump -u root --skip-opt --compact --no-data --compatible=ansi hmda | grep -v '^/\*\!'"

.. code-block:: sql

    CREATE TABLE "action_taken" (
      "id" int(11) NOT NULL,
      "action_taken" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "agency" (
      "id" int(11) NOT NULL,
      "agency_abbr" varchar(10) NOT NULL,
      "agency" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "cbsa" (
      "cbsa_code" int(11) NOT NULL,
      "parent_code" int(11) DEFAULT NULL,
      "name" varchar(255) NOT NULL,
      PRIMARY KEY ("cbsa_code")
    );
    CREATE TABLE "county" (
      "county_fips_code" int(11) NOT NULL,
      "state_fips_code" int(11) NOT NULL,
      "ansi_code" varchar(8) NOT NULL,
      "cbsa_code" int(11) DEFAULT NULL,
      "name" varchar(255) NOT NULL,
      "population" int(11) DEFAULT NULL,
      "housing_units" int(11) DEFAULT NULL,
      "land_area" bigint(20) DEFAULT NULL,
      "water_area" bigint(20) DEFAULT NULL,
      "latitude" varchar(20) DEFAULT NULL,
      "longitude" varchar(20) DEFAULT NULL,
      PRIMARY KEY ("county_fips_code","state_fips_code")
    );
    CREATE TABLE "denial_reason" (
      "id" int(11) NOT NULL,
      "denial_reason" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "edit_status" (
      "id" int(11) NOT NULL,
      "edit_status" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "ethnicity" (
      "id" int(11) NOT NULL,
      "ethnicity" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "hmda" (
      "year" int(11) NOT NULL,
      "respondent" varchar(10) DEFAULT NULL,
      "agency" int(11) DEFAULT NULL,
      "loan_type" int(11) DEFAULT NULL,
      "property_type" int(11) DEFAULT NULL,
      "loan_purpose" int(11) DEFAULT NULL,
      "occupancy" int(11) DEFAULT NULL,
      "loan_amount" int(11) DEFAULT NULL,
      "preapproval" int(11) DEFAULT NULL,
      "action_type" int(11) DEFAULT NULL,
      "msa_md" int(11) DEFAULT NULL,
      "state_code" int(11) DEFAULT NULL,
      "county_code" int(11) DEFAULT NULL,
      "census_tract_number" varchar(8) DEFAULT NULL,
      "applicant_ethnicity" int(11) DEFAULT NULL,
      "co_applicant_ethnicity" int(11) DEFAULT NULL,
      "applicant_race_1" int(11) DEFAULT NULL,
      "applicant_race_2" int(11) DEFAULT NULL,
      "applicant_race_3" int(11) DEFAULT NULL,
      "applicant_race_4" int(11) DEFAULT NULL,
      "applicant_race_5" int(11) DEFAULT NULL,
      "co_applicant_race_1" int(11) DEFAULT NULL,
      "co_applicant_race_2" int(11) DEFAULT NULL,
      "co_applicant_race_3" int(11) DEFAULT NULL,
      "co_applicant_race_4" int(11) DEFAULT NULL,
      "co_applicant_race_5" int(11) DEFAULT NULL,
      "applicant_sex" int(11) DEFAULT NULL,
      "co_applicant_sex" int(11) DEFAULT NULL,
      "applicant_income" int(11) DEFAULT NULL,
      "purchaser_type" int(11) DEFAULT NULL,
      "denial_reason_1" int(11) DEFAULT NULL,
      "denial_reason_2" int(11) DEFAULT NULL,
      "denial_reason_3" int(11) DEFAULT NULL,
      "rate_spread" varchar(10) DEFAULT NULL,
      "hoepa_status" int(11) DEFAULT NULL,
      "lien_status" int(11) DEFAULT NULL,
      "edit_status" int(11) DEFAULT NULL,
      "sequence_number" int(11) DEFAULT NULL,
      "population" int(11) DEFAULT NULL,
      "minority_population" float DEFAULT NULL,
      "hud_median_family_income" int(11) DEFAULT NULL,
      "tract_to_msa" float DEFAULT NULL,
      "number_of_owner_occupied_units" int(11) DEFAULT NULL,
      "number_of_family_units" int(11) DEFAULT NULL,
      "application_date_indicator" int(11) DEFAULT NULL,
      KEY "state_code" ("county_code"),
      KEY "ix_hmda_occupancy" ("occupancy"),
      KEY "ix_hmda_state_code" ("state_code"),
      KEY "ix_hmda_year" ("year"),
      KEY "ix_hmda_msa_md" ("msa_md"),
      KEY "ix_hmda_applicant_ethnicity" ("applicant_ethnicity"),
      KEY "ix_hmda_loan_amount" ("loan_amount"),
      KEY "ix_hmda_census_tract_number" ("census_tract_number")
    );
    CREATE TABLE "hoepa" (
      "id" int(11) NOT NULL,
      "hoepa" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "lien_status" (
      "id" int(11) NOT NULL,
      "lien_status" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "loan_purpose" (
      "id" int(11) NOT NULL,
      "loan_purpose" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "loan_type" (
      "id" int(11) NOT NULL,
      "loan_type" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "owner_occupancy" (
      "id" int(11) NOT NULL,
      "owner_occupancy" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "preapproval" (
      "id" int(11) NOT NULL,
      "preapproval" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "property_type" (
      "id" int(11) NOT NULL,
      "property_type" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "purchaser_type" (
      "id" int(11) NOT NULL,
      "purchaser_type" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "race" (
      "id" int(11) NOT NULL,
      "race" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "sex" (
      "id" int(11) NOT NULL,
      "sex" varchar(255) NOT NULL,
      PRIMARY KEY ("id")
    );
    CREATE TABLE "state" (
      "fips_code" int(11) NOT NULL,
      "abbr" varchar(2) NOT NULL,
      PRIMARY KEY ("fips_code")
    );
