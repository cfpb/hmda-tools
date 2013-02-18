#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def readme():
    with open('README.rst') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as f:
        return map(lambda x: x.strip(), f.readlines())

setup(name='hmda_tools',
      version='0.1.3',
      description='Tools to make working with HMDA data easier.',
      long_description=readme(),
      url='http://github.com/cfpb/hmda-tools',
      author='Clinton Dreisbach and others',
      author_email='clinton.dreisbach@cfpb.gov',
      license='Public domain',
      packages=[
        'hmda_tools',
        'hmda_tools.data',
      ],
      install_requires=requirements(),
      scripts=[
        'bin/hmda_create_schemas',
        'bin/hmda_load_code_sheet',
        'bin/hmda_load_cbsa',
        'bin/hmda_load_geo',
        'bin/hmda_extract_geo_data'
      ],
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      zip_safe=False,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python'
      ])
