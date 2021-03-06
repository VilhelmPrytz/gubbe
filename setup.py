#################################################################
#                                                               #
# Gubbe                                                         #
# Copyright (C) 2020, Vilhelm Prytz, <vilhelm@prytznet.se>      #
#                                                               #
# Licensed under the terms of the MIT license, see LICENSE.     #
# https://github.com/VilhelmPrytz/gubbe                         #
#                                                               #
#################################################################

import sys
from setuptools import setup, find_packages
from gubbe.version import version

assert sys.version_info >= (3, 6, 0), "Gubbe requires Python 3.6+"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gubbe",
    version=version,
    author="Vilhelm Prytz",
    author_email="vlhelm@prytznet.se",
    description="Manage Minecraft Plugins with ease!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VilhelmPrytz/gubbe",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
    install_requires=["click",],
    entry_points={"console_scripts": ["gubbe=gubbe.gubbe:main"]},
)
