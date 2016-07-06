#!/usr/bin/env python
# encoding: utf-8

name = "Leeds Combustion Sulfur Mechanism"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "SH + SH <=> S2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "C + H2S <=> CH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(8.84, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "H2S + CH3 <=> CH4 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(2.34, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "H2S + H <=> SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 'cm^3/(mol*s)'), n=2.1, Ea=(0.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "H2S + O <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+07, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "H2S + OH <=> SH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.35, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "H2S + S <=> HS2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "H2S2 + H <=> HS2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+07, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (0.71, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "H2S2 + O <=> HS2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(2.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "H2S2 + OH <=> HS2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "H2S2 + S <=> HS2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.35, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "HS2 + H <=> S2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+07, 'cm^3/(mol*s)'), n=2.1, Ea=(0.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "HS2 + O <=> S2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(2.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "HS2 + OH <=> S2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "HS2 + S <=> S2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.35, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "HSO + H <=> HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -3.14,
        Ea = (0.91, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 18,
    label = "HSO + H <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (1.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "HSO + H <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+09, 'cm^3/(mol*s)'),
        n = 1.37,
        Ea = (-0.34, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "HSO + H <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+06, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (10.39, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "HSO + H <=> SO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "HSO + O <=> O + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (5.36, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 23,
    label = "HSO + O <=> OH + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "HSO + OH <=> HOSHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+28, 'cm^3/(mol*s)'),
        n = -5.44,
        Ea = (3.18, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 25,
    label = "HSO + OH <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+07, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (3.77, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 26,
    label = "HSO + OH <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (0.47, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "HSOH <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+39, 's^-1'), n=-8.75, Ea=(75.07, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "HSOH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.8e+29, 's^-1'), n=-5.6, Ea=(54.41, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "HSOH <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.8e+16, 's^-1'), n=-3.4, Ea=(86.39, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "O + COS <=> CO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.62, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "O + COS <=> CO2 + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(10.98, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "O + CS <=> CO + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.63e+14, 'cm^3/(mol*s)'), n=0, Ea=(1.51, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "S + CH4 <=> SH + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 'cm^3/(mol*s)'), n=0, Ea=(23.99, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "S + H2 <=> SH + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(19.26, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "S + O2 <=> SO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+06, 'cm^3/(mol*s)'),
        n = 1.81,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 36,
    label = "S + OH <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "S2 + O <=> SO + S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "SH + HO2 <=> HSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "SH + O <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "SH + O <=> S + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "SH + O2 <=> HSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+13, 'cm^3/(mol*s)'), n=0, Ea=(17.87, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "SH + O2 <=> SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9.99, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "SH + OH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "SH + S <=> S2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

