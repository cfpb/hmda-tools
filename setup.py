#!/usr/bin/env python

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hmda_tools',
      version='0.1',
      description='Tools to make working with HMDA data easier.',
      long_description=readme(),
      url='http://github.com/crnixon/hmda_tools',
      author='Clinton Dreisbach and others',
      author_email='clinton@dreisbach.us',
      license='Public domain',
      packages=['hmda_tools'],
      install_requires=[
        'sqlalchemy',
        'sqlsoup',
        'requests',
        'argparse',
        'sh',
      ],
      scripts=[
        'bin/hmda_create_schemas',
        'bin/hmda_load_code_sheet',
        'bin/hmda_load_cbsa',
        'bin/hmda_load_geo',
      ],
      zip_safe=False)
