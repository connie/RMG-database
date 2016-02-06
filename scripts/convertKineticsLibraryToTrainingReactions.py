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

def addAtomLabelsForReaction(fam_rxn, database):
    from rmgpy.species import Species
    # prepare fam_rxts_mol and fam_pdts_mol
    reactants = [rxt.molecule[0] for rxt in fam_rxn.reactants]            
    products = [pdt.molecule[0] for pdt in fam_rxn.products]
    # prepare fam_forward_template always forward for fam_rxn
    # because __createReaction always make sure fam_rxn is in forward style
    family = database.kinetics.families[fam_rxn.family]
    template = family.forwardTemplate
    # Unimolecular reactants: A --> products
    if len(reactants) == 1 and len(template.reactants) == 1:
        labeledReactants, labeledProducts = family.getLabeledReactantsAndProducts(reactants, products)
        labeledProducts_spcs = []
        labeledReactants_spcs = []
        if labeledProducts is not None:
            for labeledProduct in labeledProducts:
                labeledProducts_spcs.append(Species(molecule=[labeledProduct]))
            fam_rxn.products = labeledProducts_spcs
        if labeledReactants is not None:
            for labeledReactant in labeledReactants:
                labeledReactants_spcs.append(Species(molecule=[labeledReactant]))
            fam_rxn.reactants = labeledReactants_spcs


    # Bimolecular reactants: A + B --> products
    elif len(reactants) == 2 and len(template.reactants) == 2:
        # Reactants stored as A + B
        labeledReactants, labeledProducts = family.getLabeledReactantsAndProducts(reactants, products)
        labeledProducts_spcs = []
        labeledReactants_spcs = []
        if labeledProducts is not None:
            for labeledProduct in labeledProducts:
                labeledProducts_spcs.append(Species(molecule=[labeledProduct]))
            fam_rxn.products = labeledProducts_spcs
        if labeledReactants is not None:
            for labeledReactant in labeledReactants:
                labeledReactants_spcs.append(Species(molecule=[labeledReactant]))
            fam_rxn.reactants = labeledReactants_spcs

        # Only check for swapped reactants if they are different
        if reactants[0] is not reactants[1]:

            # Reactants stored as B + A
            reactants_rev = list(reversed(reactants))
            labeledReactants, labeledProducts = family.getLabeledReactantsAndProducts(reactants_rev, products)
            labeledProducts_spcs = []
            labeledReactants_spcs = []
            if labeledProducts is not None:
                for labeledProduct in labeledProducts:
                    labeledProducts_spcs.append(Species(molecule=[labeledProduct]))
                fam_rxn.products = labeledProducts_spcs
            if labeledReactants is not None:
                for labeledReactant in labeledReactants:
                    labeledReactants_spcs.append(Species(molecule=[labeledReactant]))
                fam_rxn.reactants = labeledReactants_spcs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('library', metavar='LIBRARYNAME', type=str, nargs=1,
        help='the name of the kinetic library to be exported')    
    args = parser.parse_args()
    libraryName = args.library[0]

    print 'Loading RMG-Py database...'
    database = RMGDatabase()
    database.load(settings['database.directory'], kineticsFamilies='all', kineticsDepositories='all')
    
    reactionDict = {}
    for libraryName in args.library:
        print 'Loading {0} library'.format(libraryName)
        kineticLibrary = database.kinetics.libraries[libraryName]
        for index, entry in kineticLibrary.entries.iteritems():
            reaction = entry.item
            reaction.kinetics = entry.data
            # Let's make RMG try to generate this reaction from the families!
            rmgReactionList = database.kinetics.generateReactionsFromFamilies(reactants=reaction.reactants, products=reaction.products)
            if len(rmgReactionList) == 1:
                print "Great! We only have one match, lets create a training reaction for this."
                rmgReaction = rmgReactionList[0]
                # kineticFamily = database.kinetics.families[rmgReaction.family]
                # kineticFamily.saveTrainingReaction('stuff.py', reaction)
                if rmgReaction.family in reactionDict:
                    reactionDict[rmgReaction.family].append(rmgReaction)
                else:
                    reactionDict[rmgReaction.family] = [rmgReaction]
            elif len(rmgReactionList) == 0:
                print "Sad :( There are no matches.  This is a magic reaction or has chemistry that should be made into a new reaction family"
            else:
                print "There are multiple RMG matches for this reaction. You have to manually create this training reaction"

    for familyName in reactionDict:
        print 'Adding training reactions for family: ' + familyName
        kineticFamily = database.kinetics.families[familyName]
        reactions = reactionDict[familyName]
        # save training reactions of one family
        kineticFamily.saveTrainingReaction(reactions)
        break

            
    
    

