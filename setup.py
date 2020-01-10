#!/usr/bin/env python

from setuptools import setup
setup(
    name="datacoco-redis_tools",
    version="0.1.1",
    author="Equinox",
    description="Data common code for Redis by Equinox",
    long_description=open("README.rst").read(),
    url="https://github.com/equinoxfitness/datacoco-redis_tools",
    keywords = ['helper', 'db', 'common'],
    scripts=[],
    license="MIT",
    packages = ['datacoco_redis_tools'],
    install_requires=["redis==2.10.6", "simplejson==3.14.0", "future==0.18.2"]
)
