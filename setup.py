import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='safes',
    version='0.0.0',
    description='Computer resources for Barnes\' Statistical Analysis for Engineers and Scientists.',
    long_description=README,
    install_requires=[
    ],
    packages=['safes'],
    #test_suite='safes.tests'
)
