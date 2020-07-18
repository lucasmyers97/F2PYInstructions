"""
This test (1) whether or not you can properly index an array and (2) whether
Fortran is able to copy arrays.

Lucas Myers
July 17, 2020
"""

import numpy.f2py

with open('add1.f') as file:
    source = file.read()
    
args = ['add1.f', '-m', 'add1', '-h', 'add1.pyf']
r = numpy.f2py.run_main(args)