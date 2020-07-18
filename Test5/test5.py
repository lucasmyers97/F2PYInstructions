"""
Tests whether, if I label the variable going into a python-interfaced Fortran
script as input, it will be immutable, even if I try to change it in the
Fortran script.

Lucas Myers
July 17, 2020
"""

import numpy.f2py

with open('ChangeToOnes.f') as file:
    source = file.read()
    
args = ['ChangeToOnes.f', '-m', 'ones', '-h', 'ones.pyf']
r = numpy.f2py.run_main(args)

# args = ['--compiler=mingw32']
# module = 'ChangeToOnes'

# failure = numpy.f2py.compile(source, modulename=module, 
#                              extra_args=args, verbose=True)
# print(failure)

if not r:
    print("Success")