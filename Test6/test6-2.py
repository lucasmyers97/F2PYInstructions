"""
This just compiles the test6 *.pyf file.

Lucas Myers
Written: July 17, 2020
"""

import numpy.f2py

with open('add1.f') as file:
    source = file.read()
    
module = 'add1'
args = ['add1.pyf', '--compiler=mingw32']

failure = numpy.f2py.compile(source, extra_args=args, 
                             modulename=module, verbose=False)

print(failure)