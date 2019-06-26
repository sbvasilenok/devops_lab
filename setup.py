#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# include_package_data=True,
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="svsyslogger",
    version="1.3",
    author="Sergey Vasilenok",
    description="System paramrters logging application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6.*",
    install_requires=['psutil>=5.6.3'],
    entry_points={
        'console_scripts': [
            'svsyslogger = svsyslogger:main',
        ],
    }
)
