#!/usr/bin/env python
# encoding: utf-8

name = "PDD"
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
    shortDesc = u"""Thermo library: primaryThermoLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
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
    shortDesc = u"""Thermo library: primaryThermoLibrary""",
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
    shortDesc = u"""Thermo library: primaryThermoLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
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
    shortDesc = u"""Thermo library: primaryThermoLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "PDD(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {7,S} {31,S} {32,S}
7  C u0 p0 c0 {6,S} {8,S} {33,S} {34,S}
8  C u0 p0 c0 {7,S} {9,S} {35,S} {36,S}
9  C u0 p0 c0 {8,S} {11,S} {37,S} {38,S}
10 C u0 p0 c0 {1,S} {12,S} {19,S} {20,S}
11 C u0 p0 c0 {9,S} {13,S} {39,S} {40,S}
12 C u0 p0 c0 {10,S} {41,S} {42,S} {43,S}
13 C u0 p0 c0 {11,S} {14,B} {15,B}
14 C u0 p0 c0 {13,B} {16,B} {44,S}
15 C u0 p0 c0 {13,B} {18,B} {48,S}
16 C u0 p0 c0 {14,B} {17,B} {45,S}
17 C u0 p0 c0 {16,B} {18,B} {46,S}
18 C u0 p0 c0 {15,B} {17,B} {47,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {7,S}
34 H u0 p0 c0 {7,S}
35 H u0 p0 c0 {8,S}
36 H u0 p0 c0 {8,S}
37 H u0 p0 c0 {9,S}
38 H u0 p0 c0 {9,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {12,S}
42 H u0 p0 c0 {12,S}
43 H u0 p0 c0 {12,S}
44 H u0 p0 c0 {14,S}
45 H u0 p0 c0 {16,S}
46 H u0 p0 c0 {17,S}
47 H u0 p0 c0 {18,S}
48 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.46941,0.201518,-0.000133188,4.3957e-08,-5.86026e-12,-27240.3,73.7906], Tmin=(100,'K'), Tmax=(1732.99,'K')),
            NASAPolynomial(coeffs=[42.7448,0.0879259,-3.48697e-05,6.13543e-09,-4.04248e-13,-44298.1,-190.701], Tmin=(1732.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "TOLUENE(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {2,S} {7,D} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {13,S}
7  C u0 p0 c0 {4,D} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15375,0.0202054,7.82674e-05,-1.12992e-07,4.35913e-11,4011.52,19.7741], Tmin=(100,'K'), Tmax=(968.67,'K')),
            NASAPolynomial(coeffs=[13.3807,0.0251733,-8.90814e-06,1.70667e-09,-1.28702e-13,-571.662,-46.4623], Tmin=(968.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: SulfurLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "STYRENE(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {10,S}
3  C u0 p0 c0 {1,B} {7,B} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {9,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {3,B} {6,B} {13,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42639,0.038321,4.14785e-05,-7.99144e-08,3.27034e-11,15378.1,21.4427], Tmin=(100,'K'), Tmax=(978.64,'K')),
            NASAPolynomial(coeffs=[15.1285,0.0271012,-9.96737e-06,1.89167e-09,-1.3966e-13,10551.6,-55.3231], Tmin=(978.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cb-(Cds-Cds)) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-CdsCbH) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "ETHBENZ(4)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.33135,0.038971,5.19779e-05,-9.06902e-08,3.58865e-11,1073.66,23.2683], Tmin=(100,'K'), Tmax=(988.57,'K')),
            NASAPolynomial(coeffs=[14.7034,0.0332322,-1.27056e-05,2.42412e-09,-1.77728e-13,-3933.59,-53.0441], Tmin=(988.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "BENZ3(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {17,S}
6  C u0 p0 c0 {4,B} {9,B} {21,S}
7  C u0 p0 c0 {5,B} {8,B} {18,S}
8  C u0 p0 c0 {7,B} {9,B} {19,S}
9  C u0 p0 c0 {6,B} {8,B} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.597156,0.0547886,3.451e-05,-7.79185e-08,3.17328e-11,-1759.89,28.1489], Tmin=(100,'K'), Tmax=(1004.37,'K')),
            NASAPolynomial(coeffs=[16.1147,0.0408126,-1.60407e-05,3.04335e-09,-2.19989e-13,-7289.14,-58.7904], Tmin=(1004.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "BENZ4(6)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {6,B} {7,B}
6  C u0 p0 c0 {5,B} {8,B} {20,S}
7  C u0 p0 c0 {5,B} {10,B} {24,S}
8  C u0 p0 c0 {6,B} {9,B} {21,S}
9  C u0 p0 c0 {8,B} {10,B} {22,S}
10 C u0 p0 c0 {7,B} {9,B} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.142438,0.0706624,1.6886e-05,-6.50125e-08,2.75554e-11,-4593.2,33.0493], Tmin=(100,'K'), Tmax=(1021.93,'K')),
            NASAPolynomial(coeffs=[17.5946,0.0482806,-1.93128e-05,3.64798e-09,-2.61058e-13,-10674.9,-64.9256], Tmin=(1021.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) +
other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) +
other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "BENZ5(7)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {7,B} {8,B}
7  C u0 p0 c0 {6,B} {9,B} {23,S}
8  C u0 p0 c0 {6,B} {11,B} {27,S}
9  C u0 p0 c0 {7,B} {10,B} {24,S}
10 C u0 p0 c0 {9,B} {11,B} {25,S}
11 C u0 p0 c0 {8,B} {10,B} {26,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.888258,0.0866001,-9.11862e-07,-5.19613e-08,2.33547e-11,-7426.24,37.9726], Tmin=(100,'K'), Tmax=(1041.75,'K')),
            NASAPolynomial(coeffs=[19.1599,0.0556099,-2.25074e-05,4.23476e-09,-3.00673e-13,-14098.7,-71.5452], Tmin=(1041.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "BENZ6(8)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {8,B} {9,B}
8  C u0 p0 c0 {7,B} {10,B} {26,S}
9  C u0 p0 c0 {7,B} {12,B} {30,S}
10 C u0 p0 c0 {8,B} {11,B} {27,S}
11 C u0 p0 c0 {10,B} {12,B} {28,S}
12 C u0 p0 c0 {9,B} {11,B} {29,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.64117,0.102609,-1.8898e-05,-3.87628e-08,1.91359e-11,-10259,42.9221], Tmin=(100,'K'), Tmax=(1064.52,'K')),
            NASAPolynomial(coeffs=[20.8333,0.0627648,-2.56053e-05,4.79934e-09,-3.38488e-13,-17571.2,-78.7798], Tmin=(1064.52,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "BENZ7(9)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {9,B} {10,B}
9  C u0 p0 c0 {8,B} {11,B} {29,S}
10 C u0 p0 c0 {8,B} {13,B} {33,S}
11 C u0 p0 c0 {9,B} {12,B} {30,S}
12 C u0 p0 c0 {11,B} {13,B} {31,S}
13 C u0 p0 c0 {10,B} {12,B} {32,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
31 H u0 p0 c0 {12,S}
32 H u0 p0 c0 {13,S}
33 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.40279,0.118705,-3.71074e-05,-2.53942e-08,1.48979e-11,-13091.3,47.9039], Tmin=(100,'K'), Tmax=(1091.38,'K')),
            NASAPolynomial(coeffs=[22.6514,0.0696884,-2.85759e-05,5.33485e-09,-3.73952e-13,-21109.5,-86.8391], Tmin=(1091.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "BENZ8(10)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {7,S} {25,S} {26,S}
6  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
9  C u0 p0 c0 {7,S} {10,B} {11,B}
10 C u0 p0 c0 {9,B} {12,B} {32,S}
11 C u0 p0 c0 {9,B} {14,B} {36,S}
12 C u0 p0 c0 {10,B} {13,B} {33,S}
13 C u0 p0 c0 {12,B} {14,B} {34,S}
14 C u0 p0 c0 {11,B} {13,B} {35,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {13,S}
35 H u0 p0 c0 {14,S}
36 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.1755,0.134909,-5.55909e-05,-1.18237e-08,1.06392e-11,-15923.1,52.9269], Tmin=(100,'K'), Tmax=(1124.24,'K')),
            NASAPolynomial(coeffs=[24.6743,0.0762885,-3.13696e-05,5.83022e-09,-4.0619e-13,-24742.5,-96.0673], Tmin=(1124.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) +
other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "BENZ9(11)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {5,S} {24,S} {25,S}
5  C u0 p0 c0 {4,S} {6,S} {26,S} {27,S}
6  C u0 p0 c0 {5,S} {8,S} {28,S} {29,S}
7  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {6,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
10 C u0 p0 c0 {8,S} {11,B} {12,B}
11 C u0 p0 c0 {10,B} {13,B} {35,S}
12 C u0 p0 c0 {10,B} {15,B} {39,S}
13 C u0 p0 c0 {11,B} {14,B} {36,S}
14 C u0 p0 c0 {13,B} {15,B} {37,S}
15 C u0 p0 c0 {12,B} {14,B} {38,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
37 H u0 p0 c0 {14,S}
38 H u0 p0 c0 {15,S}
39 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.96389,0.151265,-7.44524e-05,2.02534e-09,6.34764e-12,-18754.2,58.0084], Tmin=(100,'K'), Tmax=(1166.88,'K')),
            NASAPolynomial(coeffs=[27.0168,0.0823895,-3.38931e-05,6.26474e-09,-4.33559e-13,-28525.4,-107.125], Tmin=(1166.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) +
other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) +
other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "BENZ10(12)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
2  C u0 p0 c0 {1,S} {3,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {4,S} {23,S} {24,S}
4  C u0 p0 c0 {3,S} {5,S} {25,S} {26,S}
5  C u0 p0 c0 {4,S} {6,S} {27,S} {28,S}
6  C u0 p0 c0 {5,S} {7,S} {29,S} {30,S}
7  C u0 p0 c0 {6,S} {9,S} {31,S} {32,S}
8  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
9  C u0 p0 c0 {7,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {8,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {9,S} {12,B} {13,B}
12 C u0 p0 c0 {11,B} {14,B} {38,S}
13 C u0 p0 c0 {11,B} {16,B} {42,S}
14 C u0 p0 c0 {12,B} {15,B} {39,S}
15 C u0 p0 c0 {14,B} {16,B} {40,S}
16 C u0 p0 c0 {13,B} {15,B} {41,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {7,S}
32 H u0 p0 c0 {7,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
40 H u0 p0 c0 {15,S}
41 H u0 p0 c0 {16,S}
42 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.77921,0.167881,-9.39639e-05,1.63792e-08,1.97045e-12,-21584,63.1906], Tmin=(100,'K'), Tmax=(1228.83,'K')),
            NASAPolynomial(coeffs=[29.9594,0.0875678,-3.59229e-05,6.58901e-09,-4.52173e-13,-32595.4,-121.627], Tmin=(1228.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "BENZ11(13)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
2  C u0 p0 c0 {1,S} {3,S} {22,S} {23,S}
3  C u0 p0 c0 {2,S} {4,S} {24,S} {25,S}
4  C u0 p0 c0 {3,S} {5,S} {26,S} {27,S}
5  C u0 p0 c0 {4,S} {6,S} {28,S} {29,S}
6  C u0 p0 c0 {5,S} {7,S} {30,S} {31,S}
7  C u0 p0 c0 {6,S} {8,S} {32,S} {33,S}
8  C u0 p0 c0 {7,S} {10,S} {34,S} {35,S}
9  C u0 p0 c0 {1,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {36,S} {37,S}
11 C u0 p0 c0 {9,S} {38,S} {39,S} {40,S}
12 C u0 p0 c0 {10,S} {13,B} {14,B}
13 C u0 p0 c0 {12,B} {15,B} {41,S}
14 C u0 p0 c0 {12,B} {17,B} {45,S}
15 C u0 p0 c0 {13,B} {16,B} {42,S}
16 C u0 p0 c0 {15,B} {17,B} {43,S}
17 C u0 p0 c0 {14,B} {16,B} {44,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {7,S}
33 H u0 p0 c0 {7,S}
34 H u0 p0 c0 {8,S}
35 H u0 p0 c0 {8,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {13,S}
42 H u0 p0 c0 {15,S}
43 H u0 p0 c0 {16,S}
44 H u0 p0 c0 {17,S}
45 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.96438,0.188167,-0.000123457,4.02739e-08,-5.28345e-12,-24395.9,69.7509], Tmin=(100,'K'), Tmax=(1769.18,'K')),
            NASAPolynomial(coeffs=[42.3608,0.0789057,-3.08192e-05,5.36571e-09,-3.50595e-13,-41495,-190.96], Tmin=(1769.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "RAD1(14)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {7,S} {31,S} {32,S}
7  C u0 p0 c0 {6,S} {8,S} {33,S} {34,S}
8  C u0 p0 c0 {7,S} {10,S} {35,S} {36,S}
9  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
10 C u0 p0 c0 {8,S} {13,S} {37,S} {38,S}
11 C u0 p0 c0 {9,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {13,S} {14,B} {15,B}
13 C u1 p0 c0 {10,S} {12,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {7,S}
34 H u0 p0 c0 {7,S}
35 H u0 p0 c0 {8,S}
36 H u0 p0 c0 {8,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {10,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.02009,0.203207,-0.000142623,5.17393e-08,-7.72296e-12,-10373.1,68.5451], Tmin=(100,'K'), Tmax=(1540.27,'K')),
            NASAPolynomial(coeffs=[34.7605,0.0973019,-3.9487e-05,7.09953e-09,-4.77526e-13,-22935.7,-145.813], Tmin=(1540.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(Benzyl_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "RAD2(15)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {7,S} {31,S} {32,S}
7  C u0 p0 c0 {6,S} {9,S} {33,S} {34,S}
8  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
9  C u0 p0 c0 {7,S} {13,S} {35,S} {36,S}
10 C u0 p0 c0 {12,S} {13,S} {37,S} {38,S}
11 C u0 p0 c0 {8,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {10,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {7,S}
34 H u0 p0 c0 {7,S}
35 H u0 p0 c0 {9,S}
36 H u0 p0 c0 {9,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {10,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "RAD3(16)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {13,S} {33,S} {34,S}
9  C u0 p0 c0 {10,S} {12,S} {37,S} {38,S}
10 C u0 p0 c0 {9,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {9,S} {14,B} {15,B}
13 C u1 p0 c0 {8,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {8,S}
34 H u0 p0 c0 {8,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {9,S}
38 H u0 p0 c0 {9,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "RAD4(17)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {9,S} {29,S} {30,S}
6  C u0 p0 c0 {8,S} {10,S} {31,S} {32,S}
7  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {5,S} {13,S} {33,S} {34,S}
10 C u0 p0 c0 {6,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "RAD5(18)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {9,S} {27,S} {28,S}
5  C u0 p0 c0 {6,S} {10,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {4,S} {13,S} {33,S} {34,S}
10 C u0 p0 c0 {5,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "RAD6(19)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {4,S} {23,S} {24,S}
3  C u0 p0 c0 {5,S} {6,S} {29,S} {30,S}
4  C u0 p0 c0 {2,S} {9,S} {25,S} {26,S}
5  C u0 p0 c0 {3,S} {10,S} {27,S} {28,S}
6  C u0 p0 c0 {3,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {4,S} {13,S} {33,S} {34,S}
10 C u0 p0 c0 {5,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "RAD7(20)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
2  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
3  C u0 p0 c0 {2,S} {6,S} {29,S} {30,S}
4  C u0 p0 c0 {1,S} {9,S} {23,S} {24,S}
5  C u0 p0 c0 {2,S} {10,S} {25,S} {26,S}
6  C u0 p0 c0 {3,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {4,S} {13,S} {33,S} {34,S}
10 C u0 p0 c0 {5,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "RAD8(21)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {25,S} {26,S}
2  C u0 p0 c0 {1,S} {3,S} {27,S} {28,S}
3  C u0 p0 c0 {2,S} {6,S} {29,S} {30,S}
4  C u0 p0 c0 {7,S} {9,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {10,S} {23,S} {24,S}
6  C u0 p0 c0 {3,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {4,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {4,S} {13,S} {33,S} {34,S}
10 C u0 p0 c0 {5,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {1,S}
26 H u0 p0 c0 {1,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "RAD9(22)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {23,S} {24,S}
2  C u0 p0 c0 {1,S} {3,S} {25,S} {26,S}
3  C u0 p0 c0 {2,S} {4,S} {27,S} {28,S}
4  C u0 p0 c0 {3,S} {6,S} {29,S} {30,S}
5  C u0 p0 c0 {1,S} {10,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {9,S} {11,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {7,S} {13,S} {33,S} {34,S}
10 C u0 p0 c0 {5,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {7,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {1,S}
24 H u0 p0 c0 {1,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {4,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "RAD10(23)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {7,S} {29,S} {30,S}
6  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {8,S} {31,S} {32,S}
8  C u0 p0 c0 {7,S} {12,S} {37,S} {38,S}
9  C u0 p0 c0 {6,S} {13,S} {35,S} {36,S}
10 C u0 p0 c0 {11,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {10,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {8,S} {14,B} {15,B}
13 C u1 p0 c0 {9,S} {10,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {7,S}
32 H u0 p0 c0 {7,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {9,S}
36 H u0 p0 c0 {9,S}
37 H u0 p0 c0 {8,S}
38 H u0 p0 c0 {8,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.22856,0.191231,-0.000122964,3.97217e-08,-5.278e-12,-3912.72,71.8347], Tmin=(100,'K'), Tmax=(1689.29,'K')),
            NASAPolynomial(coeffs=[33.7051,0.0990411,-4.11026e-05,7.41554e-09,-4.96913e-13,-17066.6,-136.41], Tmin=(1689.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJCC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "RAD11(24)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {8,S} {31,S} {32,S}
7  C u0 p0 c0 {1,S} {10,S} {19,S} {20,S}
8  C u0 p0 c0 {6,S} {9,S} {33,S} {34,S}
9  C u0 p0 c0 {8,S} {12,S} {37,S} {38,S}
10 C u0 p0 c0 {7,S} {13,S} {35,S} {36,S}
11 C u0 p0 c0 {13,S} {39,S} {40,S} {41,S}
12 C u0 p0 c0 {9,S} {14,B} {15,B}
13 C u1 p0 c0 {10,S} {11,S} {42,S}
14 C u0 p0 c0 {12,B} {16,B} {43,S}
15 C u0 p0 c0 {12,B} {18,B} {47,S}
16 C u0 p0 c0 {14,B} {17,B} {44,S}
17 C u0 p0 c0 {16,B} {18,B} {45,S}
18 C u0 p0 c0 {15,B} {17,B} {46,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {8,S}
34 H u0 p0 c0 {8,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {9,S}
38 H u0 p0 c0 {9,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {11,S}
41 H u0 p0 c0 {11,S}
42 H u0 p0 c0 {13,S}
43 H u0 p0 c0 {14,S}
44 H u0 p0 c0 {16,S}
45 H u0 p0 c0 {17,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.48577,0.193208,-0.000125837,4.13021e-08,-5.56014e-12,-3901.5,72.9408], Tmin=(100,'K'), Tmax=(1680.92,'K')),
            NASAPolynomial(coeffs=[35.1078,0.0966101,-3.96359e-05,7.11406e-09,-4.75433e-13,-17548.4,-143.982], Tmin=(1680.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "RAD12(25)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {21,S} {22,S}
2  C u0 p0 c0 {1,S} {3,S} {23,S} {24,S}
3  C u0 p0 c0 {2,S} {4,S} {25,S} {26,S}
4  C u0 p0 c0 {3,S} {5,S} {27,S} {28,S}
5  C u0 p0 c0 {4,S} {6,S} {29,S} {30,S}
6  C u0 p0 c0 {5,S} {7,S} {31,S} {32,S}
7  C u0 p0 c0 {6,S} {9,S} {33,S} {34,S}
8  C u0 p0 c0 {1,S} {11,S} {19,S} {20,S}
9  C u0 p0 c0 {7,S} {10,S} {35,S} {36,S}
10 C u0 p0 c0 {9,S} {12,S} {39,S} {40,S}
11 C u0 p0 c0 {8,S} {18,S} {37,S} {38,S}
12 C u0 p0 c0 {10,S} {13,B} {14,B}
13 C u0 p0 c0 {12,B} {15,B} {41,S}
14 C u0 p0 c0 {12,B} {17,B} {45,S}
15 C u0 p0 c0 {13,B} {16,B} {42,S}
16 C u0 p0 c0 {15,B} {17,B} {43,S}
17 C u0 p0 c0 {14,B} {16,B} {44,S}
18 C u1 p0 c0 {11,S} {46,S} {47,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {1,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {6,S}
33 H u0 p0 c0 {7,S}
34 H u0 p0 c0 {7,S}
35 H u0 p0 c0 {9,S}
36 H u0 p0 c0 {9,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {10,S}
40 H u0 p0 c0 {10,S}
41 H u0 p0 c0 {13,S}
42 H u0 p0 c0 {15,S}
43 H u0 p0 c0 {16,S}
44 H u0 p0 c0 {17,S}
45 H u0 p0 c0 {14,S}
46 H u0 p0 c0 {18,S}
47 H u0 p0 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.13257,0.199064,-0.000133898,4.52304e-08,-6.20149e-12,-2571.58,74.3424], Tmin=(100,'K'), Tmax=(1679.75,'K')),
            NASAPolynomial(coeffs=[39.8292,0.0896169,-3.61638e-05,6.44171e-09,-4.28591e-13,-18012.7,-171.235], Tmin=(1679.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C1(26)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20541,-0.00535555,2.51122e-05,-2.13762e-08,5.9752e-12,-10161.9,-0.921272], Tmin=(100,'K'), Tmax=(1084.12,'K')),
            NASAPolynomial(coeffs=[0.908278,0.0114541,-4.57173e-06,8.29189e-10,-5.66313e-14,-9719.98,13.993], Tmin=(1084.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: primaryThermoLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C2(27)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74671,4.54529e-05,4.07964e-05,-4.57415e-08,1.56843e-11,-11474.1,4.74139], Tmin=(100,'K'), Tmax=(981.61,'K')),
            NASAPolynomial(coeffs=[3.34703,0.0161749,-6.00959e-06,1.09621e-09,-7.72297e-14,-12094.2,3.10365], Tmin=(981.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C3(28)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06335,0.0129216,3.47029e-05,-4.70941e-08,1.71382e-11,-14390.6,10.7836], Tmin=(100,'K'), Tmax=(990,'K')),
            NASAPolynomial(coeffs=[5.60444,0.0219528,-8.22077e-06,1.50103e-09,-1.05635e-13,-15839.4,-6.22644], Tmin=(990,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C4(29)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.1692,0.0343903,-1.61507e-06,-1.30733e-08,5.17376e-12,-17250.5,14.6546], Tmin=(100,'K'), Tmax=(1147.59,'K')),
            NASAPolynomial(coeffs=[6.78892,0.03036,-1.21263e-05,2.19947e-09,-1.50291e-13,-19105.7,-11.7323], Tmin=(1147.59,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C5(30)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56222,0.0443731,2.36795e-06,-2.50999e-08,1.02877e-11,-20120.3,19.9091], Tmin=(100,'K'), Tmax=(1075.13,'K')),
            NASAPolynomial(coeffs=[9.02382,0.0365684,-1.45852e-05,2.67665e-09,-1.85598e-13,-22878.1,-21.9933], Tmin=(1075.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C6(31)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.793269,0.0605339,-1.59682e-05,-1.17111e-08,6.10149e-12,-22952.3,24.9186], Tmin=(100,'K'), Tmax=(1144.97,'K')),
            NASAPolynomial(coeffs=[11.0308,0.0431957,-1.73947e-05,3.17576e-09,-2.18145e-13,-26504.5,-31.1322], Tmin=(1144.97,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C7(32)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00291552,0.0769374,-3.48025e-05,1.86091e-09,2.01575e-12,-25782.9,30.0312], Tmin=(100,'K'), Tmax=(1262.73,'K')),
            NASAPolynomial(coeffs=[13.8378,0.0485945,-1.95475e-05,3.52837e-09,-2.39065e-13,-30514.1,-44.8642], Tmin=(1262.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C8(33)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.885254,0.0940525,-5.49402e-05,1.5832e-08,-1.84187e-12,-28608.9,35.4765], Tmin=(100,'K'), Tmax=(1950.39,'K')),
            NASAPolynomial(coeffs=[23.07,0.0449238,-1.71567e-05,2.91726e-09,-1.86478e-13,-37953.4,-96.0966], Tmin=(1950.39,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C9(34)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.37038,0.10723,-6.4278e-05,1.92037e-08,-2.34018e-12,-31454.4,39.4395], Tmin=(100,'K'), Tmax=(1842.9,'K')),
            NASAPolynomial(coeffs=[22.7911,0.0547882,-2.15936e-05,3.76275e-09,-2.4553e-13,-40359.8,-91.8967], Tmin=(1842.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C10(35)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.87596,0.120581,-7.3994e-05,2.28626e-08,-2.90803e-12,-34298.6,43.4818], Tmin=(100,'K'), Tmax=(1753.74,'K')),
            NASAPolynomial(coeffs=[22.7563,0.0643989,-2.59403e-05,4.59541e-09,-3.03992e-13,-42938.3,-89.1917], Tmin=(1753.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) +
group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C11(36)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.3989,0.134083,-8.40518e-05,2.67919e-08,-3.54427e-12,-37141.9,47.591], Tmin=(100,'K'), Tmax=(1679.17,'K')),
            NASAPolynomial(coeffs=[22.9021,0.0738129,-3.02126e-05,5.41655e-09,-3.61844e-13,-45638.8,-87.5849], Tmin=(1679.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C2ene(37)",
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
            NASAPolynomial(coeffs=[3.98877,-0.00674731,5.04405e-05,-5.70753e-08,2.04949e-11,5047.05,3.80489], Tmin=(100,'K'), Tmax=(946.01,'K')),
            NASAPolynomial(coeffs=[4.59017,0.00872731,-2.66498e-06,4.81722e-10,-3.607e-14,4127.04,-3.32432], Tmin=(946.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C3ene(38)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31912,0.00817958,3.34736e-05,-4.36194e-08,1.58214e-11,749.325,9.54025], Tmin=(100,'K'), Tmax=(983.75,'K')),
            NASAPolynomial(coeffs=[5.36755,0.0170743,-6.35108e-06,1.1662e-09,-8.27621e-14,-487.137,-4.54466], Tmin=(983.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C4ene(39)",
    molecule = 
"""
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
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58775,0.0232776,1.9342e-05,-3.55507e-08,1.3691e-11,-1918.73,14.575], Tmin=(100,'K'), Tmax=(1007.28,'K')),
            NASAPolynomial(coeffs=[7.20509,0.0236363,-9.03158e-06,1.65394e-09,-1.16021e-13,-3797.31,-12.4422], Tmin=(1007.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C5ene(40)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.90151,0.0362535,1.29136e-05,-3.55772e-08,1.4307e-11,-4763.1,19.8563], Tmin=(100,'K'), Tmax=(1027.61,'K')),
            NASAPolynomial(coeffs=[9.28062,0.0304043,-1.19376e-05,2.20665e-09,-1.55068e-13,-7487.4,-21.821], Tmin=(1027.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) +
group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) + gauche(CsOsCdSs) +
other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C6ene(41)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {5,D} {17,S} {18,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14824,0.0522686,-5.10148e-06,-2.2328e-08,1.00605e-11,-7595.8,24.807], Tmin=(100,'K'), Tmax=(1073.47,'K')),
            NASAPolynomial(coeffs=[10.9452,0.0375731,-1.50431e-05,2.77295e-09,-1.93021e-13,-10955.8,-29.0055], Tmin=(1073.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) +
group(Cs-(Cds-Cds)CsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cds-CdsCsH) +
gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) + gauche(CsOsCdSs) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C7ene(42)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.377006,0.068458,-2.35457e-05,-8.78943e-09,5.80709e-12,-10427.7,29.8245], Tmin=(100,'K'), Tmax=(1137.86,'K')),
            NASAPolynomial(coeffs=[12.9448,0.0442103,-1.78573e-05,3.27301e-09,-2.25636e-13,-14578.2,-38.1013], Tmin=(1137.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) + gauche(CsOsCdSs) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C8ene(43)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {8,D} {22,S}
8  C u0 p0 c0 {7,D} {23,S} {24,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.426637,0.0849511,-4.26974e-05,5.19267e-09,1.5502e-12,-13258,34.9638], Tmin=(100,'K'), Tmax=(1248.8,'K')),
            NASAPolynomial(coeffs=[15.7325,0.0496313,-2.00189e-05,3.62704e-09,-2.46634e-13,-18575.8,-51.7176], Tmin=(1248.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group
(Cds-CdsHH) + gauche(CsOsCdSs) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C9ene(44)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {9,D} {25,S}
9  C u0 p0 c0 {8,D} {26,S} {27,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29591,0.101978,-6.27494e-05,1.92526e-08,-2.39268e-12,-16084.8,40.3566], Tmin=(100,'K'), Tmax=(1837.13,'K')),
            NASAPolynomial(coeffs=[23.609,0.0477542,-1.84782e-05,3.18797e-09,-2.06658e-13,-25235.9,-94.9435], Tmin=(1837.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) + gauche(CsOsCdSs) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C10ene(45)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {10,D} {28,S}
10 C u0 p0 c0 {9,D} {29,S} {30,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7968,0.115291,-7.23889e-05,2.28583e-08,-2.94878e-12,-18929.4,44.3806], Tmin=(100,'K'), Tmax=(1756.15,'K')),
            NASAPolynomial(coeffs=[23.7489,0.0571038,-2.26878e-05,3.99043e-09,-2.62745e-13,-27901.6,-93.2475], Tmin=(1756.15,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group
(Cds-CdsHH) + gauche(CsOsCdSs) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C11ene(46)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {11,D} {31,S}
11 C u0 p0 c0 {10,D} {32,S} {33,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.31376,0.128743,-8.23403e-05,2.67089e-08,-3.5664e-12,-21773,48.4665], Tmin=(100,'K'), Tmax=(1687.45,'K')),
            NASAPolynomial(coeffs=[24.0183,0.0663234,-2.68543e-05,4.7876e-09,-3.18672e-13,-30659.7,-92.3477], Tmin=(1687.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) + gauche(CsOsCdSs) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "METHYL(47)",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.948,0.000827603,8.34931e-06,-9.82633e-09,3.80103e-12,16425.4,0.336656], Tmin=(100,'K'), Tmax=(660.47,'K')),
            NASAPolynomial(coeffs=[3.2217,0.00522646,-1.64125e-06,2.58225e-10,-1.62579e-14,16521.3,3.53938], Tmin=(660.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "ETHYL(48)",
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
            NASAPolynomial(coeffs=[3.69273,0.00187304,3.1194e-05,-3.71198e-08,1.32021e-11,13168.3,7.07163], Tmin=(100,'K'), Tmax=(967.57,'K')),
            NASAPolynomial(coeffs=[4.21418,0.0122657,-4.3706e-06,7.87967e-10,-5.56023e-14,12480.1,1.5378], Tmin=(967.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "PROPYL(49)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02813,0.0147026,2.405e-05,-3.66726e-08,1.38606e-11,10512.1,12.47], Tmin=(100,'K'), Tmax=(984.47,'K')),
            NASAPolynomial(coeffs=[6.16552,0.0184493,-6.79021e-06,1.23047e-09,-8.6385e-14,9095.03,-6.67653], Tmin=(984.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "BUTYL(50)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25388,0.0316763,2.89996e-06,-1.98049e-08,8.20504e-12,7652.64,17.2725], Tmin=(100,'K'), Tmax=(1050.57,'K')),
            NASAPolynomial(coeffs=[7.59591,0.0260842,-1.01719e-05,1.85189e-09,-1.28169e-13,5716.37,-12.6366], Tmin=(1050.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "PENTYL(51)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.58668,0.0452263,-8.34897e-06,-1.27375e-08,5.91037e-12,4562.96,22.3029], Tmin=(100,'K'), Tmax=(1123.44,'K')),
            NASAPolynomial(coeffs=[9.065,0.0338793,-1.35995e-05,2.48447e-09,-1.70986e-13,1918.44,-18.9375], Tmin=(1123.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "HEXYL(52)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {4,S} {18,S} {19,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.795698,0.0615832,-2.70848e-05,7.89688e-10,1.81266e-12,1732.05,27.3958], Tmin=(100,'K'), Tmax=(1257.32,'K')),
            NASAPolynomial(coeffs=[11.7155,0.0395168,-1.58793e-05,2.86529e-09,-1.94137e-13,-2015.65,-31.7702], Tmin=(1257.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "HEPTYL(53)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0236934,0.0780769,-4.55284e-05,1.31111e-08,-1.52703e-12,-1097.02,32.606], Tmin=(100,'K'), Tmax=(1942.11,'K')),
            NASAPolynomial(coeffs=[19.4311,0.0380067,-1.45793e-05,2.48701e-09,-1.59403e-13,-8653.52,-74.1653], Tmin=(1942.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) +
radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "OCTYL(54)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u1 p0 c0 {6,S} {24,S} {25,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.513508,0.0912939,-5.495e-05,1.65451e-08,-2.04006e-12,-3942.21,36.5872], Tmin=(100,'K'), Tmax=(1813.3,'K')),
            NASAPolynomial(coeffs=[19.1779,0.047856,-1.90172e-05,3.3342e-09,-2.18674e-13,-11083.5,-70.1318], Tmin=(1813.3,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "NONYL(55)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u1 p0 c0 {7,S} {27,S} {28,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.02749,0.104717,-6.48276e-05,2.03299e-08,-2.6393e-12,-6785.98,40.662], Tmin=(100,'K'), Tmax=(1710.81,'K')),
            NASAPolynomial(coeffs=[19.2082,0.0574046,-2.3345e-05,4.16502e-09,-2.77132e-13,-13709.9,-67.8293], Tmin=(1710.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) +
radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "DECYL(56)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u1 p0 c0 {8,S} {30,S} {31,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.56104,0.118313,-7.51033e-05,2.44365e-08,-3.32174e-12,-9628.65,44.8119], Tmin=(100,'K'), Tmax=(1628.32,'K')),
            NASAPolynomial(coeffs=[19.4376,0.0667291,-2.75848e-05,4.98144e-09,-3.34764e-13,-16467.1,-66.7322], Tmin=(1628.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) +
group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "UDECYL(57)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u1 p0 c0 {9,S} {33,S} {34,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.11018,0.132049,-8.57181e-05,2.88292e-08,-4.08161e-12,-12470.5,49.0213], Tmin=(100,'K'), Tmax=(1561.25,'K')),
            NASAPolynomial(coeffs=[19.8136,0.0758795,-3.17518e-05,5.78504e-09,-3.91587e-13,-19316.2,-66.5149], Tmin=(1561.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-
CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) +
gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "BENZYL(58)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74302,0.029662,5.53738e-05,-9.63387e-08,3.97344e-11,22755.7,17.944], Tmin=(100,'K'), Tmax=(955.65,'K')),
            NASAPolynomial(coeffs=[16.3539,0.0185473,-5.72513e-06,1.07726e-09,-8.37424e-14,17678,-63.8377], Tmin=(955.65,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: SulfurLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "EBZYL(59)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u1 p0 c0 {1,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3712,0.0396723,4.16454e-05,-7.86008e-08,3.15232e-11,25756.2,24.9119], Tmin=(100,'K'), Tmax=(992.04,'K')),
            NASAPolynomial(coeffs=[14.4823,0.0309632,-1.19517e-05,2.28492e-09,-1.67401e-13,20982.1,-49.1878], Tmin=(992.04,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "EBZYL2(60)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.11181,0.047706,2.14231e-05,-5.98401e-08,2.5776e-11,17972,20.4843], Tmin=(100,'K'), Tmax=(979.11,'K')),
            NASAPolynomial(coeffs=[14.469,0.0311132,-1.13356e-05,2.07863e-09,-1.48639e-13,13536.1,-52.9699], Tmin=(979.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(Benzyl_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "A3yl(61)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u1 p0 c0 {2,S} {19,S} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.635608,0.0555045,2.41367e-05,-6.57939e-08,2.73633e-11,22922.7,29.7976], Tmin=(100,'K'), Tmax=(1009.81,'K')),
            NASAPolynomial(coeffs=[15.9111,0.0385147,-1.52706e-05,2.90041e-09,-2.09356e-13,17618.8,-55.0334], Tmin=(1009.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) +
radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "A4yl(62)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {17,S}
6  C u0 p0 c0 {4,B} {9,B} {21,S}
7  C u0 p0 c0 {5,B} {8,B} {18,S}
8  C u0 p0 c0 {7,B} {9,B} {19,S}
9  C u0 p0 c0 {6,B} {8,B} {20,S}
10 C u1 p0 c0 {3,S} {22,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.106164,0.0714007,6.45155e-06,-5.28365e-08,2.31777e-11,20089.5,34.706], Tmin=(100,'K'), Tmax=(1029.86,'K')),
            NASAPolynomial(coeffs=[17.4203,0.0459351,-1.8516e-05,3.49888e-09,-2.49923e-13,14220.1,-61.3346], Tmin=(1029.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) +
other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) +
other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "A5yl(63)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {11,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,B} {7,B}
6  C u0 p0 c0 {5,B} {8,B} {20,S}
7  C u0 p0 c0 {5,B} {10,B} {24,S}
8  C u0 p0 c0 {6,B} {9,B} {21,S}
9  C u0 p0 c0 {8,B} {10,B} {22,S}
10 C u0 p0 c0 {7,B} {9,B} {23,S}
11 C u1 p0 c0 {4,S} {25,S} {26,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.855187,0.0873709,-1.1433e-05,-3.97157e-08,1.89672e-11,17256.6,39.6411], Tmin=(100,'K'), Tmax=(1052.96,'K')),
            NASAPolynomial(coeffs=[19.0326,0.0531883,-2.16684e-05,4.07594e-09,-2.88749e-13,10775.2,-68.2217], Tmin=(1052.96,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "A6yl(64)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {2,S} {12,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {7,B} {8,B}
7  C u0 p0 c0 {6,B} {9,B} {23,S}
8  C u0 p0 c0 {6,B} {11,B} {27,S}
9  C u0 p0 c0 {7,B} {10,B} {24,S}
10 C u0 p0 c0 {9,B} {11,B} {25,S}
11 C u0 p0 c0 {8,B} {10,B} {26,S}
12 C u1 p0 c0 {5,S} {28,S} {29,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.6129,0.103428,-2.95451e-05,-2.64177e-08,1.47348e-11,14424.1,44.6084], Tmin=(100,'K'), Tmax=(1080.28,'K')),
            NASAPolynomial(coeffs=[20.7825,0.0602206,-2.46987e-05,4.62506e-09,-3.25313e-13,7267.98,-75.8922], Tmin=(1080.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "A7yl(65)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
6  C u0 p0 c0 {3,S} {13,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {8,B} {9,B}
8  C u0 p0 c0 {7,B} {10,B} {26,S}
9  C u0 p0 c0 {7,B} {12,B} {30,S}
10 C u0 p0 c0 {8,B} {11,B} {27,S}
11 C u0 p0 c0 {10,B} {12,B} {28,S}
12 C u0 p0 c0 {9,B} {11,B} {29,S}
13 C u1 p0 c0 {6,S} {31,S} {32,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {13,S}
32 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38177,0.119596,-4.79389e-05,-1.29075e-08,1.04782e-11,11592.1,49.6171], Tmin=(100,'K'), Tmax=(1113.87,'K')),
            NASAPolynomial(coeffs=[22.7288,0.0669412,-2.75581e-05,5.13531e-09,-3.58744e-13,3670.62,-84.6827], Tmin=(1113.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "A8yl(66)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {27,S} {28,S}
7  C u0 p0 c0 {4,S} {14,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {9,B} {10,B}
9  C u0 p0 c0 {8,B} {11,B} {29,S}
10 C u0 p0 c0 {8,B} {13,B} {33,S}
11 C u0 p0 c0 {9,B} {12,B} {30,S}
12 C u0 p0 c0 {11,B} {13,B} {31,S}
13 C u0 p0 c0 {10,B} {12,B} {32,S}
14 C u1 p0 c0 {7,S} {34,S} {35,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
31 H u0 p0 c0 {12,S}
32 H u0 p0 c0 {13,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {14,S}
35 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.16655,0.135918,-6.67225e-05,8.95284e-10,6.1847e-12,8760.88,54.6851], Tmin=(100,'K'), Tmax=(1157.83,'K')),
            NASAPolynomial(coeffs=[24.9855,0.0731754,-3.01533e-05,5.58592e-09,-3.87396e-13,-71.6738,-95.2484], Tmin=(1157.83,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) +
other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) +
radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "A9yl(67)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {6,S} {24,S} {25,S}
5  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {9,S} {30,S} {31,S}
8  C u0 p0 c0 {5,S} {15,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {10,B} {11,B}
10 C u0 p0 c0 {9,B} {12,B} {32,S}
11 C u0 p0 c0 {9,B} {14,B} {36,S}
12 C u0 p0 c0 {10,B} {13,B} {33,S}
13 C u0 p0 c0 {12,B} {14,B} {34,S}
14 C u0 p0 c0 {11,B} {13,B} {35,S}
15 C u1 p0 c0 {8,S} {37,S} {38,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {7,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {13,S}
35 H u0 p0 c0 {14,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {15,S}
38 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.9791,0.152509,-8.61856e-05,1.52322e-08,1.79795e-12,5930.94,59.8567], Tmin=(100,'K'), Tmax=(1222.94,'K')),
            NASAPolynomial(coeffs=[27.84,0.0784875,-3.2254e-05,5.9259e-09,-4.0725e-13,-4098.9,-109.244], Tmin=(1222.94,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) +
other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) +
other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "A10yl(68)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
2  C u0 p0 c0 {1,S} {3,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {4,S} {23,S} {24,S}
4  C u0 p0 c0 {3,S} {5,S} {25,S} {26,S}
5  C u0 p0 c0 {4,S} {7,S} {27,S} {28,S}
6  C u0 p0 c0 {1,S} {9,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {10,S} {33,S} {34,S}
9  C u0 p0 c0 {6,S} {16,S} {31,S} {32,S}
10 C u0 p0 c0 {8,S} {11,B} {12,B}
11 C u0 p0 c0 {10,B} {13,B} {35,S}
12 C u0 p0 c0 {10,B} {15,B} {39,S}
13 C u0 p0 c0 {11,B} {14,B} {36,S}
14 C u0 p0 c0 {13,B} {15,B} {37,S}
15 C u0 p0 c0 {12,B} {14,B} {38,S}
16 C u1 p0 c0 {9,S} {40,S} {41,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {8,S}
34 H u0 p0 c0 {8,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
37 H u0 p0 c0 {14,S}
38 H u0 p0 c0 {15,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {16,S}
41 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.10824,0.172238,-0.000114153,3.76391e-08,-4.99042e-12,3116.27,66.2081], Tmin=(100,'K'), Tmax=(1752.61,'K')),
            NASAPolynomial(coeffs=[38.9374,0.0717101,-2.81125e-05,4.90976e-09,-3.21665e-13,-12322.4,-171], Tmin=(1752.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "A3ene(69)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {1,S} {9,D} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  C u0 p0 c0 {3,D} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.15186,0.039935,6.5362e-05,-1.094e-07,4.33237e-11,13892.1,23.5664], Tmin=(100,'K'), Tmax=(979.12,'K')),
            NASAPolynomial(coeffs=[16.0998,0.0349707,-1.29818e-05,2.46442e-09,-1.81523e-13,8275.8,-61.9661], Tmin=(979.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)CbHH) + other(R) + group(Cb-Cs) + other(R) + group(Cds-CdsCsH) + other(R) + group(Cb-H) +
other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) +
ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "A4ene(70)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u0 p0 c0 {2,S} {10,D} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {20,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {6,B} {8,B} {19,S}
10 C u0 p0 c0 {4,D} {21,S} {22,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.185742,0.0626549,2.71362e-05,-7.52597e-08,3.15484e-11,10764.5,32.3444], Tmin=(100,'K'), Tmax=(1006.12,'K')),
            NASAPolynomial(coeffs=[18.0178,0.0418474,-1.65156e-05,3.14361e-09,-2.27736e-13,4641.15,-66.3924], Tmin=(1006.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CbCsHH) + other(R) + group(Cs-(Cds-Cds)CsHH) + other(R) + group(Cb-Cs) + other(R) + group(Cds-CdsCsH) +
other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-
CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "A5ene(71)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,B} {7,B}
5  C u0 p0 c0 {3,S} {11,D} {18,S}
6  C u0 p0 c0 {4,B} {8,B} {19,S}
7  C u0 p0 c0 {4,B} {10,B} {23,S}
8  C u0 p0 c0 {6,B} {9,B} {20,S}
9  C u0 p0 c0 {8,B} {10,B} {21,S}
10 C u0 p0 c0 {7,B} {9,B} {22,S}
11 C u0 p0 c0 {5,D} {24,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.554669,0.0785377,9.48459e-06,-6.23239e-08,2.73613e-11,7931.23,37.2478], Tmin=(100,'K'), Tmax=(1023.08,'K')),
            NASAPolynomial(coeffs=[19.5055,0.0493027,-1.97805e-05,3.74658e-09,-2.68669e-13,1251.94,-72.5716], Tmin=(1023.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-(Cds-Cds)CsHH) + other(R) + group(Cb-Cs) +
other(R) + group(Cds-CdsCsH) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "A6ene(72)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {7,B} {8,B}
6  C u0 p0 c0 {4,S} {12,D} {21,S}
7  C u0 p0 c0 {5,B} {9,B} {22,S}
8  C u0 p0 c0 {5,B} {11,B} {26,S}
9  C u0 p0 c0 {7,B} {10,B} {23,S}
10 C u0 p0 c0 {9,B} {11,B} {24,S}
11 C u0 p0 c0 {8,B} {10,B} {25,S}
12 C u0 p0 c0 {6,D} {27,S} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.30122,0.0944835,-8.33956e-06,-4.92426e-08,2.31497e-11,5098.22,42.1737], Tmin=(100,'K'), Tmax=(1042.2,'K')),
            NASAPolynomial(coeffs=[21.0768,0.0566221,-2.29696e-05,4.33207e-09,-3.08179e-13,-2174.48,-79.2253], Tmin=(1042.2,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-(Cds-Cds)CsHH)
+ other(R) + group(Cb-Cs) + other(R) + group(Cds-CdsCsH) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "A7ene(73)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {2,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {8,B} {9,B}
7  C u0 p0 c0 {5,S} {13,D} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 C u0 p0 c0 {7,D} {30,S} {31,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {13,S}
31 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.05485,0.110501,-2.63542e-05,-3.60083e-08,1.89163e-11,2265.53,47.1258], Tmin=(100,'K'), Tmax=(1064.13,'K')),
            NASAPolynomial(coeffs=[22.7539,0.0637707,-2.6064e-05,4.89583e-09,-3.45925e-13,-5648.56,-86.4812], Tmin=(1064.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) +
other(R) + group(Cs-(Cds-Cds)CsHH) + other(R) + group(Cb-Cs) + other(R) + group(Cds-CdsCsH) + other(R) + group(Cb-H) + other(R) + group(Cb-H) +
other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "A8ene(74)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {25,S} {26,S}
6  C u0 p0 c0 {3,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {9,B} {10,B}
8  C u0 p0 c0 {6,S} {14,D} {27,S}
9  C u0 p0 c0 {7,B} {11,B} {28,S}
10 C u0 p0 c0 {7,B} {13,B} {32,S}
11 C u0 p0 c0 {9,B} {12,B} {29,S}
12 C u0 p0 c0 {11,B} {13,B} {30,S}
13 C u0 p0 c0 {10,B} {12,B} {31,S}
14 C u0 p0 c0 {8,D} {33,S} {34,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
31 H u0 p0 c0 {13,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {14,S}
34 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.81713,0.126605,-4.45942e-05,-2.25979e-08,1.46596e-11,-566.766,52.1099], Tmin=(100,'K'), Tmax=(1089.95,'K')),
            NASAPolynomial(coeffs=[24.5719,0.0706942,-2.90343e-05,5.43125e-09,-3.81382e-13,-9186.77,-94.5396], Tmin=(1089.95,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-(Cds-Cds)CsHH) + other(R) + group(Cb-Cs) + other(R) + group(Cds-CdsCsH) + other(R) + group(Cb-H) +
other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) +
ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "A9ene(75)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {8,S} {28,S} {29,S}
7  C u0 p0 c0 {4,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {10,B} {11,B}
9  C u0 p0 c0 {7,S} {15,D} {30,S}
10 C u0 p0 c0 {8,B} {12,B} {31,S}
11 C u0 p0 c0 {8,B} {14,B} {35,S}
12 C u0 p0 c0 {10,B} {13,B} {32,S}
13 C u0 p0 c0 {12,B} {14,B} {33,S}
14 C u0 p0 c0 {11,B} {13,B} {34,S}
15 C u0 p0 c0 {9,D} {36,S} {37,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {6,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {12,S}
33 H u0 p0 c0 {13,S}
34 H u0 p0 c0 {14,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {15,S}
37 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.59068,0.14282,-6.31202e-05,-8.96641e-09,1.03727e-11,-3398.55,57.1359], Tmin=(100,'K'), Tmax=(1121.49,'K')),
            NASAPolynomial(coeffs=[26.5895,0.0773019,-3.18319e-05,5.92746e-09,-4.13683e-13,-12817,-103.737], Tmin=(1121.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-(Cds-Cds)CsHH) + other(R) + group(Cb-Cs) + other(R) + group(Cds-
CdsCsH) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cds-CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "A10ene(76)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
2  C u0 p0 c0 {1,S} {3,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {4,S} {23,S} {24,S}
4  C u0 p0 c0 {3,S} {6,S} {25,S} {26,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {9,S} {31,S} {32,S}
8  C u0 p0 c0 {5,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {11,B} {12,B}
10 C u0 p0 c0 {8,S} {16,D} {33,S}
11 C u0 p0 c0 {9,B} {13,B} {34,S}
12 C u0 p0 c0 {9,B} {15,B} {38,S}
13 C u0 p0 c0 {11,B} {14,B} {35,S}
14 C u0 p0 c0 {13,B} {15,B} {36,S}
15 C u0 p0 c0 {12,B} {14,B} {37,S}
16 C u0 p0 c0 {10,D} {39,S} {40,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {7,S}
32 H u0 p0 c0 {7,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {13,S}
36 H u0 p0 c0 {14,S}
37 H u0 p0 c0 {15,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {16,S}
40 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.38029,0.159193,-8.20466e-05,4.97649e-09,6.03781e-12,-6229.58,62.2216], Tmin=(100,'K'), Tmax=(1162.33,'K')),
            NASAPolynomial(coeffs=[28.918,0.0834233,-3.43659e-05,6.36422e-09,-4.41226e-13,-16592.8,-114.714], Tmin=(1162.33,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-(Cds-Cds)CsHH) + other(R) + group(Cb-Cs)
+ other(R) + group(Cds-CdsCsH) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cds-CdsHH) + other(R) + ring(Ring)""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C17H27(78)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {20,S} {21,S}
2  C u0 p0 c0 {1,S} {3,S} {22,S} {23,S}
3  C u0 p0 c0 {2,S} {4,S} {24,S} {25,S}
4  C u0 p0 c0 {3,S} {5,S} {26,S} {27,S}
5  C u0 p0 c0 {4,S} {6,S} {28,S} {29,S}
6  C u0 p0 c0 {5,S} {8,S} {30,S} {31,S}
7  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
8  C u0 p0 c0 {6,S} {10,S} {32,S} {33,S}
9  C u0 p0 c0 {7,S} {11,S} {34,S} {35,S}
10 C u0 p0 c0 {8,S} {17,S} {36,S} {37,S}
11 C u0 p0 c0 {9,S} {12,B} {13,B}
12 C u0 p0 c0 {11,B} {14,B} {38,S}
13 C u0 p0 c0 {11,B} {16,B} {40,S}
14 C u0 p0 c0 {12,B} {15,B} {39,S}
15 C u0 p0 c0 {14,B} {16,B} {41,S}
16 C u0 p0 c0 {13,B} {15,B} {42,S}
17 C u1 p0 c0 {10,S} {43,S} {44,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {1,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {6,S}
31 H u0 p0 c0 {6,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {8,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {9,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
40 H u0 p0 c0 {13,S}
41 H u0 p0 c0 {15,S}
42 H u0 p0 c0 {16,S}
43 H u0 p0 c0 {17,S}
44 H u0 p0 c0 {17,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.61638,0.185616,-0.000123946,4.13717e-08,-5.5799e-12,272.118,70.2598], Tmin=(100,'K'), Tmax=(1714.55,'K')),
            NASAPolynomial(coeffs=[39.3637,0.0806799,-3.21415e-05,5.67561e-09,-3.75064e-13,-15152.1,-170.994], Tmin=(1714.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) +
other(R) + group(Cs-CbCsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cb-Cs) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) +
group(Cb-H) + other(R) + group(Cb-H) + other(R) + group(Cb-H) + other(R) + ring(Ring) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

