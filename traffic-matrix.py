#!/usr/bin/python
from __future__ import print_function

import csv
import sys

suffixes = ['','K','M','G','T','P','E','Z']

fin = open(sys.argv[1], 'rb')

csvreader = csv.reader(fin)

fout = csv.writer(sys.stdout)

#get the uniq list of egress and egress routers
uniq_set_of_egress_routers = set()
uniq_set_of_ingress_routers = set()

for row in csvreader:
    uniq_set_of_ingress_routers.add(row[0])
    uniq_set_of_egress_routers.add(row[1])


matrix = [[0 for x in range(len(uniq_set_of_egress_routers))] for y in
    range(len(uniq_set_of_ingress_routers))]

# Here we are creating a dict of in and en routers in view: {R1: 0, R2: 1 ...}
ingress_routers = {k: v for v, k in enumerate(uniq_set_of_ingress_routers)}
egress_routers = {k: v for v, k in enumerate(uniq_set_of_egress_routers)}

def dict_to_array_sort(dict_of_routers):
    result_array = [None] * len(dict_of_routers)
    for k, v in dict_of_routers.iteritems():
        result_array[v] = k
    return result_array

def utilization_to_human_readable(utilization):
    suffix_number = 0
    ut = float(utilization)
    while abs(ut) > 1024:
        ut /= 1024
        suffix_number += 1
    return str('%.02f' % ut) + " " + suffixes[suffix_number]


fin.seek(0)
for row in csvreader:
    r = ingress_routers[row[0]]
    c = egress_routers[row[1]]
    matrix[r][c] = utilization_to_human_readable('%.02f' % float(row[2]))

ingress_routers_sort = dict_to_array_sort(ingress_routers)
egress_routers_sort = dict_to_array_sort(egress_routers)

for i in range(len(egress_routers_sort)): 
    print(',', egress_routers_sort[i], end='', sep='')
print("")

for i in range(len(ingress_routers_sort)):
    print(ingress_routers_sort[i], ',', end='', sep='')
    fout.writerow(matrix[i])


fin.close()
