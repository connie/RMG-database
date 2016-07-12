#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_Aromatics"
shortDesc = u"Radical addition reactions to aromatics"
longDesc = u"""
Calculated at the G3(MP2,CC)/B3LYP level
Citation:
Kislov, V.V., Mebel, A.M., 2007. 

Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion Flames. I. Pathways Involving Benzene and Phenyl Radical. 
J. Phys. Chem. A 111, 3922–3931. doi:10.1021/jp067135x
"""
entry(
    index = 1,
    label = "BZ + CH3 <=> T1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.195e+03, 'cm^3/(mol*s)'),
        n = 2.878,
        Ea = (10.912, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "TOL + H <=> T1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.741e+06, 'cm^3/(mol*s)'),
        n = 1.768,
        Ea = (5.815, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "Indene + H <=> T5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.186e+08, 'cm^3/(mol*s)'),
        n = 1.554,
        Ea = (7.801, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "Indene + H <=> B4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.54e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)