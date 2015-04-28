# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

PACKAGE = "nagios-nsca"
NAME = "nagios-nsca"
DESCRIPTION = "Nagios passive checks support"
AUTHOR = "Jan Češpivo, COEX CZ s.r.o (http://www.coex.cz)"
AUTHOR_EMAIL = "jan.cespivo@gmail.com"
URL = "https://github.com/COEXCZ/nagios-nsca"
VERSION = '1.1.1'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="LICENSE",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
