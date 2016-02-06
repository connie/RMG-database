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
from rmgpy.data.rmg import RMGDatabase
from rmgpy import settings
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('thermoLibraryName', metavar='THERMOLIBRARYNAME', type=str, nargs=1,
        help='Name of the thermo library in your RMG-database thermo libaries folder')   
    
    args = parser.parse_args()
    libraryName = args.thermoLibraryName[0]
    
    database = RMGDatabase()
    database.load(settings['database.directory'], thermoLibraries = [libraryName], kineticsFamilies='none', kineticsDepositories='none', reactionLibraries=[])

    thermoDatabase = database.thermo
    thermoLibrary = database.thermo.libraries[libraryName]
