hmda_tools
==========

Tools to make analyzing HMDA data much easier.

* `bin/`: Scripts to load data.  
  * `bin/hmda_create_schemas`: Create the schema needed for HMDA data.
  * `bin/hmda_load_code_sheet`: Load all the data from the HMDA code sheet.
  * `bin/hmda_load_cbsa`: Download and load the Dec 2009 CBSA data, allowing you to the `msa_md` column from HMDA with a Metropolitian Statistical Area (MSA).
  * `bin/hmda_load_geo`: Download and load the 2010 Census Gazetteer data, allowing you to associate state and county FIPS codes from HMDA to names and demographic data.

How to download and load HMDA data
----------------------------------
The following commands will load the 2011 HMDA data into MySQL. Please feel free to contribute a better automated way to work with multiple DBs.

```sh
wget http://www.ffiec.gov/hmdarawdata/LAR/National/2011HMDALAR%20-%20National.zip -O hmda11.zip
unzip -p hmda11.zip | sed 's/NA//g' | sed 's/ //g' > hmd11c.csv
mysql -e 'load data local infile 'hmda11c.csv' into table hmda fields terminated by ',' lines terminated by "\n";'
```

Public Domain
--------------

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="http://github.com/crnixon/hmda_tools">
    <span property="dct:title">Clinton Dreisbach</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">hmda_tools</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="US" about="http://github.com/crnixon/hmda_tools">
  United States</span>.
</p>
