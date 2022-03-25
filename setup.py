#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from setuptools import setup

import kolibri_desktop_auth_plugin


def read_file(fname):
    """
    Read file and decode in py2k
    """
    if sys.version_info < (3,):
        return open(fname).read().decode("utf-8")
    return open(fname).read()


dist_name = "kolibri_desktop_auth_plugin"
plugin_name = "kolibri_desktop_auth_plugin"
repo_url = "https://github.com/endlessm/kolibri-desktop-auth-plugin"

readme = read_file("README.md")

# Default description of the distributed package
description = """Kolibri plugin for desktop authentication"""


setup(
    name=dist_name,
    version=kolibri_desktop_auth_plugin.__version__,
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    author="EndlessOS",
    author_email="danigm@endless.org",
    url="https://github.com/endlessm/kolibri-desktop-auth-plugin",
    packages=["kolibri_desktop_auth_plugin"],
    entry_points={
        "kolibri.plugins": (
            "kolibri_desktop_auth_plugin = kolibri_desktop_auth_plugin"
        ),
    },
    package_dir={
        "kolibri_desktop_auth_plugin": "kolibri_desktop_auth_plugin",
    },
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
