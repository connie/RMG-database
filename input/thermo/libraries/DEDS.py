#!/usr/bin/env python
# encoding: utf-8

name = "DEDS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 6/88
The first four sets of polynomial coefficients (Ar, N2, Ne, He) are from
THIRD MILLENIUM IDEAL GAS AND CONDENSED PHASE THERMOCHEMICAL DATABASE FOR
COMBUSTION WITH UPDATES FROM ACTIVE THERMOCHENICAL TABLES
Authors: Alexander Burcat and Branko Ruscic

The rest of the species are estimated by RMG (http://rmg.mit.edu/)""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""G 8/02""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Ne",
    molecule = 
"""
1 Ne u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L10/90""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "He",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,0.928724], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""REF ELEMENT""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "DEDS(1)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  S u0 p2 c0 {1,S} {6,S}
6  S u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52385,0.0495621,-1.29312e-05,-1.72343e-08,9.90101e-12,-11312.4,16.2439], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.3742,0.0266989,-9.75211e-06,1.59737e-09,-9.68631e-14,-14499.1,-41.2115], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs
-CsHHH, Gauche:Cs(CsRRR)""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C2H5S(30)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 S u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63721,0.00266527,4.71945e-05,-5.87732e-08,2.12019e-11,10473,11.1044], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.60754,0.0116165,-3.85283e-06,5.88411e-10,-3.3902e-14,8449.6,-14.2275], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsH, Gau
che:Ss(Cs(CsHH)H), Radical:SJ-Cs""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C2H5S(31)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 S u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76675,0.0144354,9.48775e-06,-2.01099e-08,8.10084e-12,17279.6,11.33], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.24782,0.0119593,-4.14184e-06,6.54271e-10,-3.86971e-14,16016.7,-8.31193], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsH, Gau
che:Ss(Cs(CsHH)H), Radical:CsCsJ""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C2H4(32)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80813,-0.00707639,5.20038e-05,-5.6865e-08,1.95238e-11,5123.16,4.96672], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[4.84789,0.0090479,-2.91089e-06,4.34059e-10,-2.4551e-14,3911.08,-5.09518], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsHH, Gauche:CsOsCdSs""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "SH(26)",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52811,-4.4394e-05,-3.76495e-07,1.40332e-09,-6.85704e-13,16236.6,3.01499], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[2.84191,0.00135244,-4.29574e-07,6.3649e-11,-3.59907e-15,16440.5,6.66081], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-HH, Gauche:Ss(RR), Radical:SJ-H""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "S2(25)",
    molecule = 
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 S u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39789,0.00146436,1.12744e-06,-2.54435e-09,1.07277e-12,14385.4,7.61949], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[4.03999,0.000585174,-1.12903e-07,5.65014e-12,2.06809e-16,14173.4,4.10156], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: RMG_Default (Species ID: S2JJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "S(24)",
    molecule = 
"""
multiplicity 3
1 S u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99082e-15,-5.27321e-18,5.25871e-21,-1.77745e-24,32894.9,5.13], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[2.5,5.5486e-16,-3.24916e-19,7.84093e-23,-7.35115e-27,32894.9,5.13], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-HH, Gauche:Ss(RR), Radical:SJ2""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C2H5J(35)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6091,-0.00237331,4.38349e-05,-4.84959e-08,1.66111e-11,13122.3,8.7194], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[4.2788,0.0119981,-3.55251e-06,4.87152e-10,-2.56198e-14,12144.2,1.24707], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:CCJ""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C2H5S2(36)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 S u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 S u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69991,0.019546,8.53318e-06,-2.32669e-08,9.79408e-12,4420.21,13.5524], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.96544,0.0133647,-4.73926e-06,7.60881e-10,-4.55036e-14,2630.44,-15.5524], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-SsH, Gauche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs
(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:SJ-Ss-Cs""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C4H10S(66)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  C u0 p0 c0 {9,S} {11,S} {12,S} {13,S}
9  C u0 p0 c0 {8,S} {10,S} {14,S} {15,S}
10 S u0 p2 c0 {2,S} {9,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57545,0.0331232,1.76255e-05,-4.15176e-08,1.69894e-11,-12115.7,13.9066], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.4273,0.0262762,-9.31322e-06,1.49499e-09,-8.94135e-14,-14901.9,-30.0838], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, G
auche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsCs, Gauche:Ss(CsCs), Ot
her:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C4H9S2(37)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {3,S} {6,S} {15,S}
5  S u0 p2 c0 {1,S} {6,S}
6  S u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4933,0.0523202,-2.69937e-05,-2.9816e-09,5.21177e-12,9188.73,17.7583], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.7348,0.0236475,-8.67008e-06,1.42417e-09,-8.65386e-14,6133.87,-40.5285], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs
-CsHHH, Gauche:Cs(CsRRR), Radical:CsJ-CsSsH""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C2H6S(41)",
    molecule = 
"""
1 H u0 p0 c0 {4,S}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 S u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73229,0.0135118,2.0164e-05,-3.20799e-08,1.22419e-11,-7399.49,9.70598], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.50292,0.0142492,-4.90888e-06,7.72438e-10,-4.55528e-14,-8936.77,-12.4205], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsH, Gau
che:Ss(Cs(CsHH)H)""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C2H4S(44)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 S u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84141,0.00572197,2.45087e-05,-3.21477e-08,1.16639e-11,7031.83,8.6792], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.99999,0.010739,-3.69827e-06,5.8184e-10,-3.43031e-14,5924.3,-5.13062], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsH, Gauche:CsOsCdSs, Group:Sd-Cd, Other:
R""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "H2S(13)",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04393,-0.00135522,6.93783e-06,-5.8646e-09,1.66735e-12,-3898.25,1.83318], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[3.03031,0.00335323,-1.11542e-06,1.71075e-10,-9.91199e-15,-3727.9,6.56062], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-HH, Gauche:Ss(RR)""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C4H9S2(84)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26688,0.0560809,-3.51917e-05,3.87579e-09,3.20491e-12,8258.21,14.7072], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.4863,0.022472,-7.91134e-06,1.26539e-09,-7.55363e-14,5058.5,-48.0424], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Ss-CsCs, Gauche:Ss(CsCs), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group
:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:SJ-Cs, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "S2(29)",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40756,0.00125483,2.31541e-06,-4.33697e-09,1.79297e-12,22627.3,7.20604], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[4.41909,-2.9529e-05,5.79085e-08,-1.47876e-11,1.12142e-15,22288.3,1.63901], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Primary Thermo Library: RMG_Default (Species ID: S2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "S(96)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36196,0.0669275,-6.22222e-05,3.0569e-08,-5.75508e-12,-9614.28,13.3088], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.3817,0.0251047,-8.96739e-06,1.44941e-09,-8.71871e-14,-12327.9,-46.2354], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Gro
up:Ss-CsCs, Gauche:Ss(CsCs), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C2H3SJ(87)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 S u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69627,0.0034055,3.02892e-05,-3.95041e-08,1.45104e-11,21955,10.0712], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.15511,0.0072934,-2.39297e-06,3.62475e-10,-2.07505e-14,20385.8,-11.0246], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-CdH, Ga
uche:Ss(RR), Radical:SJ-Cd, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "S(129)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {5,S} {10,S}
3  C u0 p0 c0 {4,D} {6,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  S u0 p2 c0 {2,S} {6,S}
6  S u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4081,0.0507913,-3.44901e-05,5.25858e-09,2.53831e-12,24882.8,17.3816], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.1891,0.0178372,-6.52736e-06,1.07244e-09,-6.51947e-14,21825.2,-42.9797], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Gro
up:Ss-SsCd, Gauche:Ss(RR), Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "S(141)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  S u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 S u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88738,0.0593767,-5.47094e-05,2.25844e-08,-2.61354e-12,26242.5,16.9292], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.8901,0.0146225,-4.63328e-06,6.84866e-10,-3.85873e-14,22884.8,-53.4257], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsCs, Ga
uche:Ss(CsCs), Group:Cs-C=SSsHH, Gauche:Cs(RRRR), Group:C=S-CsH, Gauche:CsOsCdSs, Gro
up:Sd-Cd, Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C2H4S(49)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 S u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62951,0.0103759,1.75919e-05,-2.85297e-08,1.10827e-11,8074.63,9.74824], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.76118,0.00886224,-2.88212e-06,4.33816e-10,-2.47394e-14,6505.09,-13.9193], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-CdH, Ga
uche:Ss(RR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "S(128)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10625,0.0589742,-5.35084e-05,2.1961e-08,-2.57597e-12,22743.7,12.7197], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.4596,0.0162273,-5.54913e-06,8.70547e-10,-5.12898e-14,19545.1,-54.3556], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Gr
oup:Ss-CsCd, Gauche:Ss(CsR), Radical:SJ-Cs, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "S(186)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,D} {5,S} {10,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2358,0.0707444,-9.12152e-05,6.06242e-08,-1.5677e-11,29550.3,12.9454], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.0999,0.0165701,-5.83813e-06,9.36407e-10,-5.6085e-14,27112.1,-48.4401], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Gr
oup:Ss-CsCd, Gauche:Ss(CsR), Radical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "S(185)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {6,S} {9,S}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u0 p2 c0 {2,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29704,0.0569082,-5.2461e-05,2.29916e-08,-3.31473e-12,27065.2,17.1628], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.4045,0.0171975,-6.10547e-06,9.83613e-10,-5.90391e-14,24212.2,-43.4173], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsH, Gau
che:Ss(Cs(CsHH)H), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCd
Ss, Group:Ss-CsCd, Gauche:Ss(CsR), Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "S(176)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {6,S} {13,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1411,0.0258526,4.65765e-05,-7.75983e-08,3.05319e-11,18117.9,16.0598], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.6777,0.0181931,-6.30165e-06,9.93196e-10,-5.85414e-14,13507.3,-54.9912], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsSsSsH, Group:Ss-CsCs, Group:Cs-CsSsHH, Group:Cs-CsSsHH, Gr
oup:Ss-CsCs, Radical:CsJ-CsSsH, !Ring:1,3-dithiolane, , Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C2H6S2(40)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  S u0 p2 c0 {1,S} {4,S}
4  S u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64274,0.0271,-1.282e-06,-1.70847e-08,8.28975e-12,-5359.32,12.866], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.4957,0.0146569,-5.29517e-06,8.60159e-10,-5.18467e-14,-7470.9,-23.9189], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-SsH, Gauche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs
(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR)""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "S(246)",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {8,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17166,0.0230945,6.06391e-05,-9.1851e-08,3.52212e-11,-2383.22,14.5454], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.3171,0.0212445,-7.38368e-06,1.16639e-09,-6.88659e-14,-7125.73,-55.6742], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsSsSsH, Group:Ss-CsCs, Group:Cs-CsSsHH, Group:Cs-CsSsHH, Gr
oup:Ss-CsCs, !Ring:1,3-dithiolane""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C4H7S(121)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,D} {5,S} {10,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {11,S} {12,S}
5  S u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44928,0.03694,-1.13675e-05,-1.14624e-08,7.06744e-12,27048.9,14.2362], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.1455,0.0177416,-6.18396e-06,9.81987e-10,-5.83113e-14,24538.1,-31.5954], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cds-CdsHH
Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-CsCd, Gauche:Ss(CsR), Ra
dical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C2H5SJ(48)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 S u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70173,0.0162699,6.10149e-06,-1.78273e-08,7.55267e-12,13101.6,10.5273], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[7.86357,0.0111978,-3.82685e-06,5.99243e-10,-3.52284e-14,11696.2,-12.4306], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsH, Gau
che:Ss(Cs(CsHH)H), Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C4H9S2(34)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  S u0 p2 c0 {1,S} {6,S}
6  S u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55832,0.0504857,-2.36075e-05,-5.26426e-09,5.75994e-12,13366.7,18.5611], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.1191,0.024409,-8.98506e-06,1.4792e-09,-9.00074e-14,10454.3,-36.4098], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs
-CsHHH, Gauche:Cs(CsRRR), Radical:CsCsJ""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "S(110)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {14,S}
5  S u0 p2 c0 {1,S} {4,S}
6  S u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33141,0.0696855,-7.62848e-05,4.48217e-08,-1.04443e-11,10886.8,14.1301], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.7423,0.0220533,-7.88536e-06,1.27622e-09,-7.68627e-14,8305.14,-46.2456], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Ss-CsCs, Gauche:Ss(CsCs), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group
:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C4H9SJ(58)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  S u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60991,0.0340468,6.94923e-06,-2.95476e-08,1.28483e-11,12563.4,16.2237], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.1722,0.0239863,-8.54617e-06,1.37683e-09,-8.25578e-14,10051.5,-25.2822], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsHHH, G
auche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsCs, Gauche:Ss(CsCs), Ra
dical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C2H5S2(91)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 S u0 p2 c0 {1,S} {9,S}
4 S u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61397,0.0357938,-3.44715e-05,1.71613e-08,-3.2364e-12,13445.1,9.48955], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.4454,0.0120498,-4.28235e-06,6.89802e-10,-4.13976e-14,11901.6,-24.3589], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Ss-CsH, Gauche:Ss(CsH), Radical:SJ-Cs, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C4H9SJ(73)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {14,S}
5  S u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54489,0.0358812,3.56297e-06,-2.72649e-08,1.23002e-11,8385.41,15.421], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.788,0.0232248,-8.23119e-06,1.3218e-09,-7.9089e-14,5731.08,-29.4009], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, G
auche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsCs, Gauche:Ss(CsCs), Ra
dical:CsJ-CsSsH""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C2H3SJ(88)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 S u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95352,0.00447274,1.94439e-05,-2.53246e-08,9.14127e-12,27134.7,8.90979], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.46563,0.00895081,-3.22046e-06,5.2234e-10,-3.14545e-14,26311.2,-1.00381], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsH, Gauche:CsOsCdSs, Group:Sd-Cd, Radica
l:C=SJ-Cs""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C2H5S2(72)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {8,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61218,0.029858,-1.53446e-05,-2.83203e-09,3.60051e-12,15141.8,13.6873], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.8563,0.0116055,-4.21314e-06,6.86965e-10,-4.15223e-14,13162.1,-23.929], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-SsH, Gauche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs
(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C4H8S2(78)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,D} {6,S} {12,S}
4  C u0 p0 c0 {3,D} {13,S} {14,S}
5  S u0 p2 c0 {1,S} {6,S}
6  S u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43865,0.0480332,-2.04275e-05,-8.9941e-09,7.22755e-12,4381.7,16.5603], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.8284,0.0208886,-7.60939e-06,1.24563e-09,-7.55191e-14,1192.17,-42.9696], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-SsCd, G
auche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:C
s-CsHHH, Gauche:Cs(CsRRR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C2H6S2(97)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  S u0 p2 c0 {1,S} {9,S}
4  S u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70905,0.0466404,-6.1502e-05,4.38546e-08,-1.21964e-11,-4427.36,8.09113], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.3408,0.0146825,-5.3384e-06,8.73828e-10,-5.30484e-14,-5484.8,-22.5519], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Ss-CsH, Gauche:Ss(CsH), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "HS2(18)",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88468,0.00205489,4.9852e-06,-7.72943e-09,2.99498e-12,11708.4,7.756], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[5.02337,0.00157592,-4.71098e-07,6.56245e-11,-3.50203e-15,11278.9,1.24862], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-SsH, Gauche:Ss(RR), Group:Ss-SsH, Gauche:Ss(RR), Radical:SJ-Ss-H""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "S(109)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {13,S} {14,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39643,0.0678511,-7.28985e-05,4.25391e-08,-9.89615e-12,15064.8,14.9329], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.1266,0.0228148,-8.20034e-06,1.33125e-09,-8.03314e-14,12625.6,-42.1269], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Ss-CsCs, Gauche:Ss(CsCs), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group
:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "H2S2(28)",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76163,0.00463786,1.03672e-05,-1.69351e-08,6.67849e-12,593.742,8.10192], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[6.61717,0.00261495,-8.38225e-07,1.22949e-10,-6.83037e-15,-442.667,-8.01253], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-SsH, Gauche:Ss(RR), Group:Ss-SsH, Gauche:Ss(RR)""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C2H5S2(62)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {7,S} {8,S}
3 S u0 p2 c0 {1,S} {4,S}
4 S u0 p2 c0 {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67721,0.0280236,-1.19583e-05,-5.11469e-09,4.14867e-12,19319.8,14.49], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.2406,0.012367,-4.52812e-06,7.41992e-10,-4.4991e-14,17482.5,-19.8104], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Ss-SsH, Gauche:Ss(RR), Radical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "S(199)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u0 p2 c0 {1,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20133,0.0698207,-8.05389e-05,4.86542e-08,-1.1536e-11,4871.23,11.3213], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.355,0.01886,-6.60518e-06,1.05457e-09,-6.29407e-14,2158.7,-52.5486], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Gr
oup:Ss-CsCd, Gauche:Ss(CsR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C2H6(64)",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81951,-0.0046219,5.78714e-05,-6.42513e-08,2.20759e-11,-11593.8,5.2836], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[4.85974,0.0140318,-4.67239e-06,7.15784e-10,-4.13563e-14,-12931.3,-5.41029], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR)""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C4H9S2(95)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39643,0.0678511,-7.28985e-05,4.25391e-08,-9.89615e-12,15064.8,14.9329], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.1266,0.0228148,-8.20034e-06,1.33125e-09,-8.03314e-14,12625.6,-42.1269], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Gro
up:Ss-CsCs, Gauche:Ss(CsCs), Radical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "S(253)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {3,S} {5,S} {6,S}
5  S u0 p2 c0 {1,S} {4,S}
6  S u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20612,0.0240181,4.99628e-05,-7.9881e-08,3.10801e-11,22295.9,15.764], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.062,0.0189546,-6.61663e-06,1.04822e-09,-6.20102e-14,17827.7,-51.971], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsSsSsH, Group:Ss-CsCs, Group:Cs-CsSsHH, Group:Cs-CsSsHH, Gr
oup:Ss-CsCs, Radical:CsJ-S, Radical:CsJ, !Ring:1,3-dithiolane, , Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C2H4S2(63)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 S u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 S u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73437,0.0204696,-2.14312e-06,-1.12969e-08,5.65301e-12,29099.3,15.1765], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.71034,0.0110748,-3.97221e-06,6.42715e-10,-3.86479e-14,27583.9,-11.4439], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Ss-SsH, Gauche:Ss(RR), Radical:CsCsJ, Radical:SJ-Ss-Cs, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C2H4S2(69)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 S u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 S u1 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66935,0.0223041,-5.52937e-06,-9.01424e-09,5.10485e-12,24921.3,14.3737], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.32609,0.0103133,-3.65723e-06,5.87687e-10,-3.51791e-14,23263.5,-15.5625], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Ss-SsH, Gauche:Ss(RR), Group:Ss-SsCs, Gauche:Ss(RR), Group:Cs-CsSsHH, Gauche:Cs
(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Radical:SJ-Ss-Cs, Radical:CsJ-CsSsH""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "S(291)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63419,0.00899571,3.73239e-05,-5.22095e-08,1.95533e-11,12144.6,9.65625], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.17707,0.011586,-4.07517e-06,6.48176e-10,-3.84414e-14,9810.16,-23.2446], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsHH, Group:Cs-CsSsHH, Group:Ss-SsCs, Group:Ss-SsCs, !Ring:1,2-dithietane
Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C2H4S2(83)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 S u0 p2 c0 {1,S} {4,S}
4 S u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36073,0.0118536,3.37013e-05,-5.18488e-08,2.01075e-11,9261.73,11.066], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.0912,0.00837848,-2.66721e-06,3.93959e-10,-2.20897e-14,6356.92,-33.0565], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsSsSsH, Group:Ss-SsCs, Group:Ss-SsCs, !Ring:dithiirane, Oth
er:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "S(145)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 S u0 p2 c0 {1,S} {4,S}
4 S u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55754,0.0255711,-8.77836e-06,-8.84453e-09,5.61629e-12,10334.8,12.4893], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.9499,0.00884662,-3.15245e-06,5.08421e-10,-3.05028e-14,8220.41,-26.3701], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-SsCd, G
auche:Ss(RR), Group:Ss-SsH, Gauche:Ss(RR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C2H4S2(92)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 S u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 S u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51889,0.0249473,-7.44102e-06,-9.53194e-09,5.72359e-12,31317.6,10.888], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.55,0.00941706,-3.2263e-06,5.05775e-10,-2.97467e-14,29287.9,-26.1659], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsSsH, Gauche:Cs(RRRR), Group:Ss-CsH, Ga
uche:Ss(CsH), Group:Ss-CsH, Gauche:Ss(CsH), Radical:SJ-Cs, Radical:SJ-Cs, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "S(325)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61471,0.0180171,1.03682e-06,-1.50267e-08,7.12062e-12,20114.3,13.1757], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[9.41973,0.00755435,-2.59654e-06,4.09143e-10,-2.41596e-14,18321.8,-18.0036], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-SsCd, G
auche:Ss(RR), Group:Ss-SsH, Gauche:Ss(RR), Radical:SJ-Ss-Cs""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "S(159)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {6,S} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  S u0 p2 c0 {1,S} {6,S}
6  S u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47312,0.0489568,-3.11038e-05,2.97592e-09,3.08648e-12,29060.8,18.1843], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.5733,0.0185987,-6.84234e-06,1.12746e-09,-6.86634e-14,26145.6,-38.861], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-SsCs, Ga
uche:Ss(RR), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Gro
up:Ss-SsCd, Gauche:Ss(RR), Radical:CsCsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "S(249)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,D} {5,S} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.70346,0.0447133,-1.45444e-05,-1.66984e-08,1.04154e-11,12560.4,10.9478], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.4381,0.0135929,-3.94889e-06,5.35163e-10,-2.78893e-14,8634.45,-61.2387], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsSsSsH, Group:Ss-CsCd, Group:Cds-CdsSsH, Group:Cds-CdsSsH
Group:Ss-CsCd, !Ring:FiveMember, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C4H8S(115)",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {8,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {2,S}
6  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {6,S} {8,S} {12,S} {13,S}
8  S u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41482,0.0360164,-6.91168e-07,-2.34324e-08,1.12085e-11,2369.8,12.6122], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.4006,0.0200315,-6.95101e-06,1.10015e-09,-6.5167e-14,-415.366,-35.704], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Cs-CsHHH
Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsCd, Gauche:Ss(CsR), Ot
her:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C2H2S(143)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 S u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60501,0.0284025,-3.79095e-05,2.5521e-08,-6.64667e-12,27137.2,9.79983], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[8.93835,0.00579304,-2.06279e-06,3.2254e-10,-1.88225e-14,26133.7,-15.613], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-(Cdd-Sd)HH, Group:Cds-CddHH, Gauche:CsOsCdSs, Group:Cdd-CdsSd, Group:Cdd-C
dSd, Group:Sd, Group:S, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C4H7S(268)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {5,S} {9,S}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  S u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38426,0.0387745,-1.47537e-05,-9.17976e-09,6.51927e-12,22870.9,13.4335], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.7613,0.0169801,-5.86898e-06,9.2696e-10,-5.48425e-14,20217.6,-35.7141], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cds-CdsHH
Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-CsCd, Gauche:Ss(CsR), Ra
dical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "S(401)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {7,S}
2  C u0 p0 c0 {1,D} {8,S} {9,S}
3  C u0 p0 c0 {5,D} {10,S} {11,S}
4  S u0 p2 c0 {1,S} {6,S}
5  C u1 p0 c0 {3,D} {6,S}
6  S u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36596,0.0513534,-4.86471e-05,2.0504e-08,-2.55181e-12,46485.5,15.6], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.4498,0.0124529,-4.59163e-06,7.59787e-10,-4.64336e-14,43601.7,-45.0445], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-SsCd, G
auche:Ss(RR), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Gr
oup:Ss-SsCd, Gauche:Ss(RR), Radical:CdsJ-Ss, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C4H7S(414)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  S u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.01474,0.0205328,5.01472e-05,-7.8623e-08,3.05779e-11,24994.9,14.549], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.898,0.0148707,-4.79364e-06,7.15008e-10,-4.04193e-14,20545.5,-53.1965], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsCsSsH, Group:Cs-CsHHH, Group:Cs-CsHHH, Group:Cs-CsCsSsH, Group:Ss-CsCs, Ra
dical:CsCsJ, !Ring:thiirane, , Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "S(168)",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {5,S} {9,S}
3  C u1 p0 c0 {4,S} {5,S} {10,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  S u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 S u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81795,0.0400894,4.27843e-06,-3.83577e-08,1.81378e-11,36477.5,19.0336], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.8724,0.012604,-4.08364e-06,6.0724e-10,-3.41943e-14,31846.2,-61.7381], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-CsCs, Ga
uche:Ss(CsCs), Group:Cs-C=SSsHH, Gauche:Cs(RRRR), Group:C=S-CsH, Gauche:CsOsCdSs, Gro
up:Sd-Cd, Radical:CsJ-CsSsH, Radical:CsJ-C=SSsH""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "S(455)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {11,D} {12,S}
5  S u0 p2 c0 {1,S} {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 S u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28577,0.0394624,1.45798e-05,-5.32658e-08,2.40801e-11,18101.3,15.4081], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[20.4669,0.00837648,-1.87426e-06,1.78629e-10,-5.55475e-15,12403.8,-82.6631], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsCsSsH, Group:Ss-CsCs, Group:Cs-C=SCsSsH, Group:C=S-CsH, Gr
oup:Sd-Cd, !Ring:thiirane, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "S(463)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {10,D} {11,S}
5  S u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 S u0 p2 c0 {4,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64605,0.0227132,5.62145e-05,-9.19101e-08,3.64051e-11,27031,15.8243], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.8166,0.00984793,-2.98995e-06,4.161e-10,-2.2017e-14,21231.7,-75.0791], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsCsSsH, Group:Ss-CsCs, Group:Cs-C=SCsSsH, Group:C=S-CsH, Gr
oup:Sd-Cd, Radical:CsJ-CsC=SSs, !Ring:thiirane""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "S(474)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u0 p2 c0 {4,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22705,0.0513054,-2.03592e-05,-1.84778e-08,1.24975e-11,16886.7,13.2587], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[20.6541,0.00806371,-1.65448e-06,1.31879e-10,-2.33125e-15,11693.1,-83.2197], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-(Cds-Cds)CsSsH, Group:Cs-(Cds-Cd)CsSsH, Group:Cs-CdsCsSsH
Group:Ss-CsCd, Group:Cds-CdsCsSs, Group:Cds-CdsSsH, Group:Ss-CdH, !Ring:thiirane""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "S(503)",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {5,S} {11,S}
5  S u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 S u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9805,0.0294391,3.32471e-05,-6.53849e-08,2.67585e-11,29801.7,17.4945], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.6268,0.014703,-5.02021e-06,7.75558e-10,-4.49326e-14,25099.7,-58.2537], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-C=SCsHH, Gauche:Cs(CsRRR), Group:Sd-Cd, Gr
oup:C=S-CsCs, Gauche:CsOsCdSs, Group:Cs-C=SSsHH, Gauche:Cs(RRRR), Group:Ss-CsH, Gauch
e:Ss(CsH), Radical:Allyl_S, Radical:CsJ-C=SSsH""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "S(532)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33154,0.0405518,-8.18e-06,-2.28517e-08,1.2429e-11,18561.8,0.465512], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.7592,0.0123595,-4.55226e-06,7.61183e-10,-4.6906e-14,14613.1,-70.6629], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Group:Cds-CdsCsH, Group:Ss-CsCd, Group:Cds-CdsCsSs, Group:Cs-
(Cds-Cds)SsSsH, Group:Cs-(Cds-Cd)SsSsH, Group:Cs-CdsSsSsH, Group:Cs-CSsSsH, Group:Cs
Group:Ss-CsH, !Ring:thiirane, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "S(533)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,D}
5  S u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 S u0 p2 c0 {4,D}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58669,0.0346915,2.09004e-05,-5.59185e-08,2.4259e-11,20402.2,17.0064], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.521,0.0105693,-2.93305e-06,3.80866e-10,-1.90022e-14,15254.2,-69.7217], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-C=SCsCsH, Group:Sd-Cd, Group:C=S-CsCs, Group:Cs-C=SCsSsH, Gr
oup:Ss-CsH, !Ring:ThreeMember, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "S(555)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  C u0 p0 c0 {1,S} {3,S} {10,D}
5  S u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 S u0 p2 c0 {4,D}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94697,0.0179423,6.25351e-05,-9.45629e-08,3.65841e-11,29331.9,17.4226], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.8707,0.0120407,-4.04874e-06,6.18337e-10,-3.54645e-14,24082.2,-62.1377], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-C=SCsCsH, Group:Sd-Cd, Group:C=S-CsCs, Group:Cs-C=SCsSsH, Gr
oup:Ss-CsH, Radical:CsJ-CsC=SSs, !Ring:ThreeMember""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "S(573)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {4,S} {5,S}
4  C u0 p0 c0 {2,S} {3,S} {9,D}
5  S u0 p2 c0 {3,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  S u0 p2 c0 {4,D}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42274,0.0249268,3.07649e-06,-2.21546e-08,1.02416e-11,24322.6,0.981755], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[11.2546,0.0114366,-3.71151e-06,5.66175e-10,-3.27473e-14,21873.2,-41.2393], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Group:Cds-CdsC=SCs, Group:Sd-Cd, Group:C=S-(Cds-Cds)(Cds-Cds
), Group:C=S-(Cds-Cd)(Cds-Cd), Group:C=S-CdsCds, Group:C=S-CC, Group:Cds, Group:Cds-C
dsC=SSs, Group:Cds-CdsCdsSs, Group:Cds-CdCS, Group:Cds, Group:Ss-CdH, !Ring:ThreeMemb
er, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "S(486)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {3,D} {6,S} {10,S}
5  S u0 p2 c0 {2,S} {3,S}
6  S u0 p2 c0 {4,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.78268,0.0378371,2.64641e-06,-3.49438e-08,1.67772e-11,31222,14.4962], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.3258,0.0105432,-3.19407e-06,4.48786e-10,-2.41028e-14,26784.8,-63.3469], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-(Cds-Cds)CsSsH, Group:Cs-(Cds-Cd)CsSsH, Group:Cs-CdsCsSsH
Group:Ss-CsCd, Group:Cds-CdsCsSs, Group:Cds-CdsSsH, Group:Ss-CdH, Radical:CsJ-CsCdSs
!Ring:thiirane, , Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "S(592)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 C u0 p0 c0 {2,S} {4,S} {8,D}
4 C u0 p0 c0 {2,D} {3,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 S u0 p2 c0 {3,D}
9 S u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4895,0.0179564,1.57738e-05,-3.3129e-08,1.36693e-11,38202.9,1.30469], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.6485,0.00986773,-3.22237e-06,4.94834e-10,-2.87584e-14,35754,-38.3446], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Group:Cds-CdsC=SCs, Group:Sd-Cd, Group:C=S-(Cds-Cds)(Cds-Cds
), Group:C=S-(Cds-Cd)(Cds-Cd), Group:C=S-CdsCds, Group:C=S-CC, Group:Cds, Group:Cds-C
dsC=SSs, Group:Cds-CdsCdsSs, Group:Cds-CdCS, Group:Cds, Group:Ss-CdH, Radical:SJ-Cd, !
Ring:ThreeMember""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "S(400)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,D}
2  C u0 p0 c0 {4,D} {5,S} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96597,0.0349428,9.64746e-06,-4.12208e-08,1.87062e-11,32830.8,16.2069], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.8951,0.0114093,-3.81026e-06,5.80776e-10,-3.33362e-14,28451.8,-58.9991], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsSs, Gauche:CsOsCdSs, Group:Sd-Cd, Group
:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-C=SCd, Gauch
e:Ss(RR), Radical:Allyl_P, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "S(219)",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {4,D} {5,S} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  S u0 p2 c0 {1,S} {2,S}
6  S u0 p2 c0 {1,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08413,0.0504458,-3.73707e-05,7.50235e-09,2.0669e-12,20542.4,16.7136], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.9839,0.0136299,-4.545e-06,7.00277e-10,-4.07148e-14,17230.6,-49.1979], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsSs, Group:Cds-CdSsSs, Group:Cds, Gau
che:CsOsCdSs, Group:Ss-CdH, Gauche:Ss(RR), Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cd
s-CdsSsH, Gauche:CsOsCdSs, Group:Ss-CdCd, Gauche:Ss(RR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "S(591)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,D}
4 C u1 p0 c0 {1,S} {7,S} {8,S}
5 S u0 p2 c0 {2,S} {9,S}
6 S u0 p2 c0 {3,D}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28348,0.0194052,1.46238e-05,-3.25263e-08,1.35565e-11,38566.3,2.61875], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[10.7444,0.0102901,-3.10769e-06,4.39538e-10,-2.38263e-14,36047.9,-38.5325], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Group:Cds-CdsC=SCs, Group:Sd-Cd, Group:C=S-(Cds-Cds)(Cds-Cds
), Group:C=S-(Cds-Cd)(Cds-Cd), Group:C=S-CdsCds, Group:C=S-CC, Group:Cds, Group:Cds-C
dsC=SSs, Group:Cds-CdsCdsSs, Group:Cds-CdCS, Group:Cds, Group:Ss-CdH, Radical:C=CC=CC
J, !Ring:ThreeMember""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "S(575)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,D}
4  C u0 p0 c0 {1,S} {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  S u0 p2 c0 {3,D}
10 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27153,0.0174476,4.28534e-05,-6.80372e-08,2.65783e-11,33816.7,14.5507], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.8932,0.0116455,-4.02021e-06,6.32403e-10,-3.72007e-14,29876.3,-45.8184], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-C=SC=SCsH, Group:Cs-CdsCdsCsH, Group:Sd-Cd, Group:C=S-C=SCs
Group:C=S-C=SCs, Group:Sd-Cd, !Ring:ThreeMember, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "S(686)",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u1 p0 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  S u1 p2 c0 {3,S}
10 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46031,0.0296396,5.59083e-06,-3.04677e-08,1.39379e-11,42909.8,16.11], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.8296,0.0121535,-4.52676e-06,7.5045e-10,-4.58199e-14,39648.3,-39.8839], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Gauche:Cs(RRRR), Group:Cds-CdsCsH, Gauche:CsOsCdSs, Group:Ss-
CdH, Gauche:Ss(RR), Group:Cds-CdsC=SSs, Group:Cds-CdsCdsSs, Group:Cds-CdCS, Group:Cds
Gauche:CsOsCdSs, Group:C=S-(Cds-Cds)H, Group:C=S-(Cds-Cd)H, Group:C=S-CdsH, Gauche:
CsOsCdSs, Group:Sd-Cd, Radical:SJ-Cd, Radical:C=SJ-Cd, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "S(477)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  S u0 p2 c0 {1,S} {3,S}
5  C u0 p0 c0 {3,D} {10,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 S u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.1557,0.0686089,-7.29892e-05,3.22164e-08,-4.00828e-12,35830.1,14.4157], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[22.1105,0.00449107,-6.02097e-07,-2.23851e-11,6.38479e-15,31062,-85.7601], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-(Cds-Cdd-Sd)CsSsH, Group:Cs-(Cds-Cdd)CsSsH, Group:Cs-(Cds-
Cd)CsSsH, Group:Cs-CdsCsSsH, Group:Ss-CsCd, Group:Cds-(Cdd-Sd)CsSs, Group:Cds-CddCsS
s, Group:Cds-CdCS, Group:Cds, Group:Cdd-CdsSd, Group:Cdd-CdSd, Group:Sd, Group:S, !Ring
:thiirane, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "S(703)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,D} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,D}
5  S u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16683,0.0235208,3.21985e-05,-6.02995e-08,2.45018e-11,25852.8,12.6531], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.3268,0.0110334,-3.84133e-06,6.05221e-10,-3.56004e-14,21631.1,-55.0051], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Group:Cds-CdsCsH, Group:Ss-C=SCd, Group:Cds-CdsC=SSs, Group:C
ds-CdsCdsSs, Group:Cds-CdCS, Group:Cds, Group:C=S-(Cds-Cds)Ss, Group:C=S-(Cds-Cd)Ss
Group:C=S-CdsSs, Group:C=S-CSs, Group:Sd-Cd, !Ring:thiirane, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "S(717)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {5,S} {11,D}
5  S u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76677,0.0125896,8.86511e-05,-1.24587e-07,4.7298e-11,20444.5,15.1486], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.6563,0.0113133,-3.79068e-06,5.71537e-10,-3.23269e-14,14183.3,-77.0025], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsCsHH, Group:Ss-C=SCs, Group:Cs-C=SCsSsH, Group:C=S-CsSs, G
roup:Sd-Cd, Radical:CsJ-CsC=SSs, !Ring:thiirane""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "S(728)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,D}
5  S u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40649,0.0293388,4.70165e-05,-8.5943e-08,3.49729e-11,11514.7,14.7324], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[20.3066,0.00984186,-2.67498e-06,3.34066e-10,-1.58646e-14,5355.38,-84.5866], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsCsHH, Group:Ss-C=SCs, Group:Cs-C=SCsSsH, Group:C=S-CsSs, G
roup:Sd-Cd, !Ring:thiirane""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "S(747)",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 S u1 p2 c0 {4,S}
12 S u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23457,0.0332468,1.10314e-05,-3.90069e-08,1.72151e-11,31109.3,18.8703], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.7449,0.0155535,-5.37604e-06,8.48723e-10,-5.01502e-14,27403.9,-43.7122], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-(Cds-Cds)CsHH, Gauche:Cs(CsRRR), Group:Ss
-CdH, Gauche:Ss(RR), Group:Cds-CdsCsH, Gauche:CsOsCdSs, Group:Cds-CdsSsSs, Group:Cds-
CdSsSs, Group:Cds, Gauche:CsOsCdSs, Group:Ss-CdH, Gauche:Ss(RR), Radical:SJ-Cd, Radica
l:SJ-Cd""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "S(769)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {5,S} {6,S}
5  S u0 p2 c0 {4,S} {6,S}
6  S u0 p2 c0 {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16837,0.0142635,6.73551e-05,-9.56859e-08,3.62474e-11,18419,19.7133], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.8665,0.0147501,-5.00192e-06,7.79244e-10,-4.55522e-14,13738.8,-48.4845], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-(Cds-Cds)CsHH, Group:Ss-SsCd, Group:Cds-CdsCsH, Group:Cds-C
dsSsSs, Group:Cds-CdSsSs, Group:Cds, Group:Ss-SsCd, !Ring:dithiirane, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "S(736)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {5,S} {6,S}
5  S u0 p2 c0 {1,S} {4,S}
6  S u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6856,0.0777848,-0.000100726,6.17668e-08,-1.43659e-11,22709.3,-26.9499], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[20.9493,0.00859033,-2.78586e-06,4.14539e-10,-2.34213e-14,18865.5,-116.022], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Group:Cs-CsCsHH, Group:Ss-CsCs, Group:Cs-CsCsSsSs, Group:Cs-CsSsSsH
Group:Ss-CsCs, Radical:CsJ-S, Radical:CsJ, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "S(714)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 C u0 p0 c0 {1,S} {5,S} {7,D}
4 C u1 p0 c0 {2,S} {8,S} {9,S}
5 S u0 p2 c0 {1,S} {3,S}
6 H u0 p0 c0 {2,S}
7 S u0 p2 c0 {3,D}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02757,0.0179992,4.37458e-05,-7.06712e-08,2.78167e-11,40096.5,14.2901], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.8167,0.00988697,-3.23752e-06,4.78583e-10,-2.66794e-14,35805.9,-52.2982], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)HHH, Group:Cds-CdsCsH, Group:Ss-C=SCd, Group:Cds-CdsC=SSs, Group:C
ds-CdsCdsSs, Group:Cds-CdCS, Group:Cds, Group:C=S-(Cds-Cds)Ss, Group:C=S-(Cds-Cd)Ss
Group:C=S-CdsSs, Group:C=S-CSs, Group:Sd-Cd, Radical:C=CC=CCJ, !Ring:thiirane""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "S(792)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {8,D}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  S u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  S u0 p2 c0 {3,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26084,0.0146286,6.04931e-05,-9.14266e-08,3.54776e-11,28899.8,2.97679], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.1113,0.00785454,-3.01614e-06,5.16019e-10,-3.21389e-14,23722.4,-75.94], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Group:Cds-CdsCsH, Group:Ss-C=SCs, Group:Cs-C=S(Cds-Cds)SsH, Group:C
s-C=S(Cds-Cd)SsH, Group:Cs-CdsCdsSsH, Group:Cs-CCSsH, Group:Cs, Group:C=S-CsSs, Group
:Sd-Cd, !Ring:thiirane""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "S(823)",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u1 p0 c0 {1,S} {4,S} {5,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {7,S} {10,D}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  S u1 p2 c0 {4,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13566,0.0186681,4.03512e-05,-6.52497e-08,2.55803e-11,42264.1,19.4736], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[13.5791,0.0124178,-4.09103e-06,6.14576e-10,-3.48433e-14,38416.8,-39.7468], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsCsH, Gauche:CsOsCdSs, Group:Ss-C=SH, G
auche:Ss(RR), Group:Cs-C=S(Cds-Cds)HH, Group:Cs-C=S(Cds-Cd)HH, Group:Cs-CdsCdsHH, Ga
uche:Cs(RRRR), Group:C=S-CsSs, Gauche:CsOsCdSs, Group:Sd-Cd, Radical:SJ-C=S, Radical:
C=CCJC=C""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "S(847)",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  S u0 p2 c0 {2,S} {6,S}
6  S u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81626,0.0138004,6.2062e-05,-9.2061e-08,3.55904e-11,31763.8,19.2304], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.5717,0.0074047,-2.01199e-06,2.56256e-10,-1.24797e-14,26605.5,-59.2275], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Group:Cds-Cds(Cds-Cds)H, Group:Ss-SsCd, Group:Cds-Cds(Cds-Cds)H, Gr
oup:Cds-CdsSsSs, Group:Cds-CdSsSs, Group:Cds, Group:Ss-SsCd, !Ring:dithiirane, Other:
R""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "S(848)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,D}
5  S u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53305,-0.0065554,0.000115025,-1.39189e-07,5.00517e-11,20011,16.6664], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[12.8598,0.0146913,-5.55202e-06,9.23189e-10,-5.6298e-14,15247,-42.8958], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)SsHH, Group:Cs-(Cds-Cd)SsHH, Group:Cs-CdsSsHH, Group:Cds-CdsCsH, G
roup:Ss-C=SCs, Group:Cds-CdsC=SH, Group:C=S-(Cds-Cds)Ss, Group:C=S-(Cds-Cd)Ss, Group
:C=S-CdsSs, Group:C=S-CSs, Group:Sd-Cd, !Ring:2,5-dihydrothiophene, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "S(866)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {7,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {5,S} {8,S}
4 C u0 p0 c0 {2,D} {5,S} {9,S}
5 S u0 p2 c0 {3,S} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 S u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42658,0.0157729,5.85995e-05,-9.14127e-08,3.6011e-11,27151.5,17.0381], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.3373,0.00327025,-1.23978e-07,-9.70775e-11,1.07847e-14,21437.7,-72.4437], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsSsH, Group:Cds-Cds(Cds-Cds)H, Group:Ss-CdCd, Group:Cds-Cds(Cds-Cds)H, G
roup:Cds-CdsSsSs, Group:Cds-CdSsSs, Group:Cds, Group:Ss-CdH, Radical:SJ-Cd, !Ring:thi
ophene, , Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "S(886)",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  S u0 p2 c0 {2,S} {4,S}
6  S u0 p2 c0 {2,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35982,0.0227433,4.59023e-05,-8.04382e-08,3.25833e-11,13271.2,16.7152], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[18.9434,0.0048391,-6.1312e-07,-2.57365e-11,6.79582e-15,7556.97,-75.3384], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsSsH, Group:Cds-Cds(Cds-Cds)H, Group:Ss-CdCd, Group:Cds-Cds(Cds-Cds)H, G
roup:Cds-CdsSsSs, Group:Cds-CdSsSs, Group:Cds, Group:Ss-CdH, !Ring:thiophene""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "S(883)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  S u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  S u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95958,0.00379577,9.44075e-05,-1.23687e-07,4.59095e-11,21319.6,16.5684], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.706,0.0106237,-3.42106e-06,5.04588e-10,-2.81103e-14,15908.3,-59.3076], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsSsH, Group:Cds-CdsCsH, Group:Ss-C=SCd, Group:Cs-C=S(Cds-Cds)HH, Group:C
s-C=S(Cds-Cd)HH, Group:Cs-CdsCdsHH, Group:C=S-CsSs, Group:Sd-Cd, !Ring:2,3-dihydroth
iophene""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "S(898)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {9,S}
4 C u0 p0 c0 {2,S} {3,D} {8,S}
5 S u0 p2 c0 {1,S} {2,S}
6 H u0 p0 c0 {1,S}
7 S u1 p2 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.51333,0.0437254,-1.00447e-05,-2.86745e-08,1.60313e-11,31095.4,-21.5507], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[21.3844,0.00262327,-4.81431e-07,2.36677e-11,9.29467e-16,25619.2,-121.145], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-(Cds-Cds)CsSsH, Group:Cs-(Cds-Cd)CsSsH, Group:Cs-CdsCsSsH, Group:Cds-CdsCs
H, Group:Ss-CsCs, Group:Cds-CdsCsH, Group:Cs-(Cds-Cds)CsSsSs, Group:Cs-(Cds-Cd)CsSsS
s, Group:Cs-CdsCsSsSs, Group:Cs-CCSsSs, Group:Cs, Group:Ss-CsH, Radical:SJ-Cs, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "S(887)",
    molecule = 
"""
1 H u0 p0 c0 {6,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,D}
4 S u0 p2 c0 {2,S} {7,S}
5 H u0 p0 c0 {2,S}
6 C u0 p0 c0 {1,S} {3,D} {7,S}
7 C u0 p0 c0 {4,S} {6,S} {8,D}
8 S u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80371,0.00798637,6.30691e-05,-8.97264e-08,3.43871e-11,42067.4,5.59762], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.5231,0.00351326,-5.2311e-07,3.43511e-12,3.23766e-15,37226.3,-67.3093], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-(Cdd-Cd)SsH, Group:Cds-CddSsH, Group:Cds-CdSsH, Group:Cds, Group:Cdd-CdsCd
s, Group:Ss-C=SCd, Group:Cds-(Cdd-Cd)C=SH, Group:Cds-CddCdsH, Group:C=S-(Cds-Cdd-Cd)
Ss, Group:C=S-(Cds-Cdd)Ss, Group:C=S-(Cds-Cd)Ss, Group:C=S-CdsSs, Group:C=S-CSs, Grou
p:Sd-Cd, !Ring:FiveMember, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "S(404)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,D} {9,S}
3  C u0 p0 c0 {5,D} {10,S} {11,S}
4  S u0 p2 c0 {1,S} {5,S}
5  C u1 p0 c0 {3,D} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  S u0 p2 c0 {2,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76982,0.0643609,-7.96867e-05,4.76748e-08,-1.08111e-11,46636.6,13.5368], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[17.6698,0.00880387,-2.47807e-06,3.29115e-10,-1.69236e-14,43456.5,-59.3525], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-CsCd, G
auche:Ss(CsR), Group:Cs-C=SSsHH, Gauche:Cs(RRRR), Group:C=S-CsH, Gauche:CsOsCdSs, Gro
up:Sd-Cd, Radical:CdsJ-Ss, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "S(897)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {7,S}
3 C u1 p0 c0 {1,S} {2,S} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {9,D}
5 S u0 p2 c0 {2,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40261,0.0303798,1.37395e-05,-4.35725e-08,1.91896e-11,35045.6,-20.1986], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.316,0.0103981,-4.27113e-06,7.42536e-10,-4.65713e-14,30895.1,-90.3768], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsCsSsH, Group:Cs-CsCsHH, Group:Ss-C=SCs, Group:Cs-C=SCsCsH, Group:C=S-CsSs
Group:Sd-Cd, Radical:cyclopropane, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "S(205)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,D}
3  C u0 p0 c0 {4,D} {5,S} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  S u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  S u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17097,0.0360744,6.87125e-06,-3.66283e-08,1.67329e-11,14569.5,15.6711], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.6207,0.0150728,-5.25474e-06,8.31606e-10,-4.91765e-14,10654,-51.5554], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsSs, Gauche:CsOsCdSs, Group:Sd-Cd, Group
:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsH, Gauche:CsOsCdSs, Group:Ss-C=SCd, Gauch
e:Ss(RR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "S(311)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {5,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {13,D}
5  S u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43963,0.036984,6.26828e-06,-3.46097e-08,1.56576e-11,19276.7,16.9785], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.4544,0.0192703,-7.0746e-06,1.16009e-09,-7.03278e-14,15769.5,-42.7149], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-C=SCs, G
auche:Ss(CsR), Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsSs, Gauche:CsOsCdSs, Gro
up:Sd-Cd, Radical:CsJ-CsSsH, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "S(102)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,D}
5  S u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 S u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47019,0.0342259,2.03308e-05,-4.88624e-08,2.03469e-11,-1224.43,16.1572], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[14.0938,0.0223217,-8.15663e-06,1.33329e-09,-8.06522e-14,-4863.46,-42.7048], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsSs, Gauche:CsOsCdSs, Group:Sd-Cd, Group
:Ss-C=SCs, Gauche:Ss(CsR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, Gauche:C
s(CsRRR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "S(390)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {11,D}
4  C u1 p0 c0 {3,S} {12,S} {13,S}
5  S u0 p2 c0 {1,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 S u0 p2 c0 {3,D}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26519,0.0330943,2.3107e-05,-5.34548e-08,2.23202e-11,17036.9,16.6931], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[15.3682,0.0186583,-6.71215e-06,1.08246e-09,-6.48119e-14,12934.3,-50.1484], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-C=SHHH, Gauche:Cs(RRRR), Group:C=S-CsSs, Gauche:CsOsCdSs, Group:Sd-Cd, Group
:Cs-CsHHH, Gauche:Cs(CsRRR), Group:Cs-CsSsHH, Gauche:Cs(RRRR), Group:Ss-C=SCs, Gauche
:Ss(CsR), Radical:Allyl_P, Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "S(330)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,D} {5,S} {6,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  S u0 p2 c0 {1,S} {3,S}
6  S u0 p2 c0 {3,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1209,0.054766,-3.64336e-05,4.80496e-09,3.08754e-12,4736.12,15.9194], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[16.1212,0.0186709,-6.38969e-06,1.00237e-09,-5.90315e-14,1348.7,-50.7559], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cds-CdsHH, Gauche:CsOsCdSs, Group:Cds-CdsSsSs, Group:Cds-CdSsSs, Group:Cds, Gau
che:CsOsCdSs, Group:Ss-CdH, Gauche:Ss(RR), Group:Ss-CsCd, Gauche:Ss(CsR), Group:Cs-Cs
SsHH, Gauche:Cs(RRRR), Group:Cs-CsHHH, Gauche:Cs(CsRRR), Other:R""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "S(900)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {4,S} {8,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {9,S}
5 S u0 p2 c0 {1,S} {3,S}
6 S u0 p2 c0 {1,S} {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.78265,0.0655515,-8.17604e-05,4.66073e-08,-9.82155e-12,29112.9,-28.477], Tmin=(250,'K'), Tmax=(995,'K')),
            NASAPolynomial(coeffs=[19.6306,0.0050918,-1.57484e-06,2.24134e-10,-1.21883e-14,25400.2,-111.483], Tmin=(995,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (250,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Estimated by RMG using Group Additivity
Group:Cs-CsSsSsH, Group:Cs-(Cds-Cds)CsHH, Group:Ss-CsCd, Group:Cds-CdsCsH, Group:Cds
-CdsSsSs, Group:Cds-CdSsSs, Group:Cds, Group:Ss-CsCd, Radical:Allyl_S, Other:R""",
    longDesc = 
u"""

""",
)

