hmda_tools
==========

Tools to make analyzing HMDA data much easier.

HMDA
----

"HMDA" refers to the `Home Mortgage Disclosure Act`_, a law that requires
financial institutions to maintain and annually disclose data about home
purchases, home purchase pre-approvals, home improvement, and refinance applications. This data is made public and is available from the US Government at the `FFIEC HMDA Products`_ site.

.. _Home Mortgage Disclosure Act:  http://en.wikipedia.org/wiki/Home_Mortgage_Disclosure_Act
.. _FFIEC HMDA Products: http://www.ffiec.gov/hmda/hmdaproducts.htm

Included scripts
----------------

-  ``bin/hmda_create_schemas``: Create the schema needed for HMDA data.
-  ``bin/hmda_load_code_sheet``: Load all the data from the HMDA code
   sheet.
-  ``bin/hmda_load_cbsa``: Download and load the Dec 2009 CBSA data,
   allowing you to the ``msa_md`` column from HMDA with a Metropolitian
   Statistical Area (MSA).
-  ``bin/hmda_load_geo``: Download and load the 2010 Census Gazetteer
   data, allowing you to associate state and county FIPS codes from HMDA
   to names and demographic data.

How to download and load HMDA data
----------------------------------

The following commands will load the 2011 HMDA data into MySQL. Please
feel free to contribute a better automated way to work with multiple
DBs.

::

    wget http://www.ffiec.gov/hmdarawdata/LAR/National/2011HMDALAR%20-%20National.zip -O hmda11.zip
    unzip -p hmda11.zip | sed 's/NA//g' | sed 's/ //g' > hmd11c.csv
    mysql -e 'load data local infile 'hmda11c.csv' into table hmda fields terminated by ',' lines terminated by "\n";'

