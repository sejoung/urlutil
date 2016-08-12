# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

options = {
    "bundle_files": 1,                 # create singlefile exe
    "compressed"  : 1,                 # compress the library archive

}

setup(
    options = {"py2exe": options},
    zipfile = None,
    console = ["urlutil.py"]
)
