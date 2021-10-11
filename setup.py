#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

import kolibri_auth_plugin


dist_name = "kolibri_auth_plugin"
# Default description of the distributed package
description = """Kolibri plugin for desktop authentication"""


setup(
    name=dist_name,
    description=description,
    version=kolibri_auth_plugin.__version__,
    author="EndlessOS",
    author_email="danigm@endless.org",
    url="https://github.com/endlessm/kolibri-auth-plugin",
    packages=["kolibri_auth_plugin"],
    entry_points={
        "kolibri.plugins": "kolibri_auth_plugin = kolibri_auth_plugin",
    },
    package_dir={"kolibri_auth_plugin": "kolibri_auth_plugin"},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords="kolibri",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
