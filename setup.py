#!/usr/bin/env python

from setuptools import setup
setup(
    name="datacoco-redis_tools",
    version="0.1.0",
    author="Equinox",
    description="",
    long_description=open("README.rst").read(),
    url="https://github.com/equinoxfitness/datacoco-redis_tools",
    download_url = 'https://github.com/equinoxfitness/datacoco-redis_tools/archive/v-0.1.0.tar.gz',
    keywords = ['helper', 'db', 'common'],
    scripts=[],
    license="MIT",
    packages = ['datacoco_redis_tools'],
    install_requires=["redis==2.10.6", "simplejson==3.14.0", "future==0.18.2"]
)
