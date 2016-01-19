#!/usr/bin/env python
# encoding: utf-8

"""
This script exports an individual RMG-Py kinetics library completely to training reactions.
Thermo is taken from RMG's estimates and libraries.  
In order to use more specific thermo, you must tweak the thermoLibraries and 
estimators in use when loading the database.

The script will save the training reactions to their
appropriate locations by appending to the original files.

usage:
convertKineticsLibrarytoTrainingReactions.py [-h] LIBRARYNAME

positional arguments:
LIBRARYNAME      the libraryname of the RMG-Py format kinetics library
"""
import argparse
import os
from rmgpy.data.rmg import RMGDatabase
from rmgpy.chemkin import saveChemkinFile, saveSpeciesDictionary
from rmgpy.rmg.model import Species
from rmgpy import settings
    
################################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('library', metavar='LIBRARYNAME', type=str, nargs=1,
        help='the name of the kinetic library to be exported')    
    args = parser.parse_args()
    libraryName = args.library[0]

    print 'Loading RMG-Py database...'
    database = RMGDatabase()
    database.load(settings['database.directory'], kineticsFamilies='all', kineticsDepositories='all')
    

    print 'Loading {0} library'.format(libraryName)
    kineticLibrary = database.kinetics.libraries[libraryName]
    
    reactionList = []    
    for index, entry in kineticLibrary.entries.iteritems():
        reaction = entry.item
        reaction.kinetics = entry.data
        # Let's make RMG try to generate this reaction from the families!
        rmgReactionList = database.kinetics.generateReactionsFromFamilies(reactants=reaction.reactants, products=reaction.products):
        if len(rmgReactionList) == 1:
            print "Great! We only have one match, lets create a training reaction for this."
            rmgReaction = rmgReactionList[0]
        elif len(rmgReactionList) == 0:
            print "Sad :( There are no matches.  This is a magic reaction or has chemistry that should be made into a new reaction family"
        else:
            print "There are multiple RMG matches for this reaction. You have to manually create this training reaction"


    #reactions=rdatabase.kinetics.families[reactionFamily].generateReactions(reactantList)
            
    
    

