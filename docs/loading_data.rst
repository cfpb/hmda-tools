Loading Data
=============

HMDA Code Sheet
----------------
The HMDA data set contains a code sheet that explains what each of the numbers
it uses for sex, race, ethnicity, regulating authority, and other lookup columns
means. ``hmda_tools`` helps you load join tables for each of those columns into
your database by using the script ``hmda_load_code_sheet``.

You can also load these join tables programatically by calling
:py:func:`hmda_tools.data.load_code_sheet`.

CBSA
-----
Individual mortgages in the HMDA data set may be associated with a `Metropolitan
Statistical Area (MSA)`__, using a code in the ``msa_md`` column. You can load a
join table for this column using the ``hmda_load_cbsa`` script.

.. __: http://en.wikipedia.org/wiki/Metropolitan_Statistical_Area

The ``msa_md`` column will only join against the ``cbsa_code`` column in the
``cbsa`` table. The ``parent_code`` column is there only for your use in
determining the child areas of a larger combined statistical area.

This data is taken from the December 2009 Core-Based Statistical Area data from
the US Census. HMDA data from before 2010 may not use this data.

You can also load these join tables programatically by calling
:py:func:`hmda_tools.data.cbsa.load_cbsa`.

State and County Data
----------------------
Individual mortgages in the HMDA data set have a county code and a state code.
You can load a join table for these columns, using data from the 2010 county
gazetteer from the US Census, by running the script `hmda_load_geo`. A crosswalk
file will also be downloaded and used to populate the CBSA each county is in.

You can also load these join tables programatically by calling
:py:func:`hmda_tools.data.geo.load_all`.

Actual HMDA Data
----------------
There is no current functionality to automatically load HMDA data. Given its
size, it is easiest to load using your database's bulk import facilities.

To load the 2011 HMDA data into MySQL, run the following:

.. code-block:: bash

  wget http://www.ffiec.gov/hmdarawdata/LAR/National/2011HMDALAR%20-%20National.zip -O hmda11.zip
  unzip -p hmda11.zip | sed 's/[nN][aA]//gI' | sed 's/ //g' > hmd11c.csv
  mysql -e 'load data local infile 'hmda11c.csv' into table hmda fields terminated by ',' lines terminated by "\n";'
