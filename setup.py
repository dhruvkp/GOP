# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='GOP',
    version='0.0.1',
    description='GOP for MLE',
    long_description=readme,
    author='Dhruv Patel',
    author_email='dhruvkumarr.patel51@gmail.com',
    url='https://github.com/dhruvkp/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

