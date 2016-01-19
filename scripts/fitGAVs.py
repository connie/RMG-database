#!/usr/bin/env python
# encoding: utf-8

"""
This script fit GAV values.

usage:
fitGAVs.py [-h] THERMOLIBRARYNAME

positional arguments:
THERMOLIBRARYNAME      the thermo library's name in your RMG-database thermo libraries folder
"""

import argparse
import os
from rmgpy.data.thermo import ThermoLibrary
from rmgpy import settings
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('thermoLibraryName', metavar='THERMOLIBRARYNAME', type=str, nargs=1,
        help='Name of the thermo library in your RMG-database thermo libaries folder')   
    
    args = parser.parse_args()
    libraryName = args.thermoLibraryName[0]
    
    library = ThermoLibrary()
    library.loadOld(
        dictstr = os.path.join(inputPath, 'Dictionary.txt'),
        treestr = '',
        libstr = os.path.join(inputPath, 'Library.txt'),
        numParameters = 12,
        numLabels = 1,
        pattern = False,
    )
    library.name = libraryName

    # Save in Py format    
    library.save(os.path.join(settings['database.directory'], 'thermo', 'libraries', libraryName+'.py'))
