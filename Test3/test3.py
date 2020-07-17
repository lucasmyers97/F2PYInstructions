"""
This code creates a Fortran extension for python of a function which produces
a fibonacci sequence and then adds one to all the entries. It is meant to test
using subroutines which live in seprate files.

This test failed.

Lucas Myers
Written: July 15, 2020
"""

import numpy.f2py

with open('fib2.f') as file:
    source = file.read()
    
module = 'fib2'
args = ['fib2.pyf','fib1.f', '--compiler=mingw32']

failure = numpy.f2py.compile(source, extra_args=args, 
                             modulename=module, verbose=False)

print(failure)

import fib2

a = fib2.fibadd(8)
print(a)