"""
This compiles the .pyf for the fifth Fortran test. Here I'm seeing if it will
change a variable that is marked with an intent(in) marker. It definitely will.

Lucas Myers
Written: July 17, 2020
"""

import numpy.f2py

with open('ChangeToOnes.f') as file:
    source = file.read()
    
module = 'ones'
args = ['ones.pyf', '--compiler=mingw32']

failure = numpy.f2py.compile(source, extra_args=args, 
                             modulename=module, verbose=False)

print(failure)