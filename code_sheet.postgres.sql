--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: action_taken; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE action_taken (
    id integer NOT NULL,
    action_taken character varying(255) NOT NULL
);


--
-- Name: agency; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE agency (
    id integer NOT NULL,
    agency_abbr character varying(10) NOT NULL,
    agency character varying(255) NOT NULL
);


--
-- Name: denial_reason; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE denial_reason (
    id integer NOT NULL,
    denial_reason character varying(255) NOT NULL
);


--
-- Name: edit_status; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE edit_status (
    id integer NOT NULL,
    edit_status character varying(255) NOT NULL
);


--
-- Name: ethnicity; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE ethnicity (
    id integer NOT NULL,
    ethnicity character varying(255) NOT NULL
);


--
-- Name: hoepa; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE hoepa (
    id integer NOT NULL,
    hoepa character varying(255) NOT NULL
);


--
-- Name: lien_status; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE lien_status (
    id integer NOT NULL,
    lien_status character varying(255) NOT NULL
);


--
-- Name: loan_purpose; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE loan_purpose (
    id integer NOT NULL,
    loan_purpose character varying(255) NOT NULL
);


--
-- Name: loan_type; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE loan_type (
    id integer NOT NULL,
    loan_type character varying(255) NOT NULL
);


--
-- Name: owner_occupancy; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE owner_occupancy (
    id integer NOT NULL,
    owner_occupancy character varying(255) NOT NULL
);


--
-- Name: preapproval; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE preapproval (
    id integer NOT NULL,
    preapproval character varying(255) NOT NULL
);


--
-- Name: property_type; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE property_type (
    id integer NOT NULL,
    property_type character varying(255) NOT NULL
);


--
-- Name: purchaser_type; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE purchaser_type (
    id integer NOT NULL,
    purchaser_type character varying(255) NOT NULL
);


--
-- Name: race; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE race (
    id integer NOT NULL,
    race character varying(255) NOT NULL
);


--
-- Name: sex; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE sex (
    id integer NOT NULL,
    sex character varying(255) NOT NULL
);


--
-- Data for Name: action_taken; Type: TABLE DATA; Schema: public; Owner: -
--

COPY action_taken (id, action_taken) FROM stdin;
1	Loan originated
2	Application approved but not accepted
3	Application denied by financial institution
4	Application withdrawn by applicant
5	File closed for incompleteness
6	Loan purchased by the institution
7	Preapproval request denied by financial institution
8	Preapproval request approved but not accepted
\.


--
-- Data for Name: agency; Type: TABLE DATA; Schema: public; Owner: -
--

COPY agency (id, agency_abbr, agency) FROM stdin;
1	OCC	Office of the Comptroller of the Currency
2	FRS	Federal Reserve System
3	FDIC	Federal Deposit Insurance Corporation
4	OTS	Office of Thrift Supervision
5	NCUA	National Credit Union Administration
7	HUD	Department of Housing and Urban Development
9	CFPB	Consumer Financial Protection Bureau
\.


--
-- Data for Name: denial_reason; Type: TABLE DATA; Schema: public; Owner: -
--

COPY denial_reason (id, denial_reason) FROM stdin;
1	Debt-to-income ratio
2	Employment history
3	Credit history
4	Collateral
5	Insufficient cash (downpayment, closing costs)
6	Unverifiable information
7	Credit application incomplete
8	Mortgage insurance denied
9	Other
\.


--
-- Data for Name: edit_status; Type: TABLE DATA; Schema: public; Owner: -
--

COPY edit_status (id, edit_status) FROM stdin;
5	Validity edit failure only
6	Quality edit failure only
7	Validity and quality edit failures
\.


--
-- Data for Name: ethnicity; Type: TABLE DATA; Schema: public; Owner: -
--

COPY ethnicity (id, ethnicity) FROM stdin;
1	Hispanic or Latino
2	Not Hispanic or Latino
3	Information not provided by applicant in mail, Internet, or telephone application
4	Not applicable
5	No co-applicant
\.


--
-- Data for Name: hoepa; Type: TABLE DATA; Schema: public; Owner: -
--

COPY hoepa (id, hoepa) FROM stdin;
1	HOEPA loan
2	Not a HOEPA loan
\.


--
-- Data for Name: lien_status; Type: TABLE DATA; Schema: public; Owner: -
--

COPY lien_status (id, lien_status) FROM stdin;
1	Secured by a first lien
2	Secured by a subordinate lien
3	Not secured by a lien
4	Not applicable
\.


--
-- Data for Name: loan_purpose; Type: TABLE DATA; Schema: public; Owner: -
--

COPY loan_purpose (id, loan_purpose) FROM stdin;
1	Home purchase
2	Home improvement
3	Refinancing
\.


--
-- Data for Name: loan_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY loan_type (id, loan_type) FROM stdin;
1	Conventional
2	FHA-insured
3	VA-guaranteed
4	FSA/RHS
\.


--
-- Data for Name: owner_occupancy; Type: TABLE DATA; Schema: public; Owner: -
--

COPY owner_occupancy (id, owner_occupancy) FROM stdin;
1	Owner-occupied
2	Not owner-occupied
3	Not applicable
\.


--
-- Data for Name: preapproval; Type: TABLE DATA; Schema: public; Owner: -
--

COPY preapproval (id, preapproval) FROM stdin;
1	Preapproval was requested
2	Preapproval was not requested
3	Not applicable
\.


--
-- Data for Name: property_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY property_type (id, property_type) FROM stdin;
1	One to four-family
2	Manufactured housing
3	Multifamily
\.


--
-- Data for Name: purchaser_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY purchaser_type (id, purchaser_type) FROM stdin;
0	Loan was not originated or was not sold in calendar year covered by register
1	Fannie Mae (FNMA)
2	Ginnie Mae (GNMA)
3	Freddie Mac (FHLMC)
4	Farmer Mac (FAMC)
5	Private securitization
6	Commercial bank, savings bank or savings association
7	Life insurance company, credit union, mortgage bank, or finance company
8	Affiliate institution
9	Other type of purchaser
\.


--
-- Data for Name: race; Type: TABLE DATA; Schema: public; Owner: -
--

COPY race (id, race) FROM stdin;
1	American Indian or Alaska Native
2	Asian
3	Black or African American
4	Native Hawaiian or Other Pacific Islander
5	White
6	Information not provided by applicant in mail, Internet, or telephone application
7	Not applicable
8	No co-applicant
\.


--
-- Data for Name: sex; Type: TABLE DATA; Schema: public; Owner: -
--

COPY sex (id, sex) FROM stdin;
1	Male
2	Female
3	Information not provided by applicant in mail, Internet, or telephone application
4	Not applicable
5	No co-applicant
\.


--
-- Name: action_taken_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY action_taken
    ADD CONSTRAINT action_taken_pkey PRIMARY KEY (id);


--
-- Name: agency_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY agency
    ADD CONSTRAINT agency_pkey PRIMARY KEY (id);


--
-- Name: denial_reason_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY denial_reason
    ADD CONSTRAINT denial_reason_pkey PRIMARY KEY (id);


--
-- Name: edit_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY edit_status
    ADD CONSTRAINT edit_status_pkey PRIMARY KEY (id);


--
-- Name: ethnicity_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY ethnicity
    ADD CONSTRAINT ethnicity_pkey PRIMARY KEY (id);


--
-- Name: hoepa_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY hoepa
    ADD CONSTRAINT hoepa_pkey PRIMARY KEY (id);


--
-- Name: lien_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY lien_status
    ADD CONSTRAINT lien_status_pkey PRIMARY KEY (id);


--
-- Name: loan_purpose_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY loan_purpose
    ADD CONSTRAINT loan_purpose_pkey PRIMARY KEY (id);


--
-- Name: loan_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY loan_type
    ADD CONSTRAINT loan_type_pkey PRIMARY KEY (id);


--
-- Name: owner_occupancy_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY owner_occupancy
    ADD CONSTRAINT owner_occupancy_pkey PRIMARY KEY (id);


--
-- Name: preapproval_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY preapproval
    ADD CONSTRAINT preapproval_pkey PRIMARY KEY (id);


--
-- Name: property_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY property_type
    ADD CONSTRAINT property_type_pkey PRIMARY KEY (id);


--
-- Name: purchaser_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY purchaser_type
    ADD CONSTRAINT purchaser_type_pkey PRIMARY KEY (id);


--
-- Name: race_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY race
    ADD CONSTRAINT race_pkey PRIMARY KEY (id);


--
-- Name: sex_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY sex
    ADD CONSTRAINT sex_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM dreisbachc;
GRANT ALL ON SCHEMA public TO dreisbachc;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

