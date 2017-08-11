#!/usr/bin/python

import sys

SUFFIXES = ['','K','M','G','T','P','E','Z']
DIMENSION = 1000 # Can be 1024 if we want to work in bandwidth dimension

##
def utilization_to_human_readable(utilization_str):
    suffix_index = 0

    try:
        ut = float(utilization_str)
    except ValueError,e:
        print "ERROR !!!", e
        sys.exit(1)

    while abs(ut) > DIMENSION:
        ut /= DIMENSION
        suffix_index += 1
    return str('%.02f' % ut) + SUFFIXES[suffix_index] 


##
if len(sys.argv) != 1:
    for arg_num in range(1, len(sys.argv)):
        print utilization_to_human_readable(sys.argv[arg_num])
else:
    for line in sys.stdin:
        bw = float(line)
        print utilization_to_human_readable(bw)
