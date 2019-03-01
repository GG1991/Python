#!/usr/bin/python3

import sys

sensors =  {
        '2' : ['S0', 0.0],
        '3' : ['S1', 0.0],
        '4' : ['S2', 0.0],
        '5' : ['S3', 0.0]
        }

if (len(sys.argv) <= 1):
    print("Please guy specify the Alya output file as:\npost_vars <file.sld.set>\n")
    exit(1)

f_in = open(sys.argv[1], 'r')
f_out = open('sensors.dat', 'w')
line = f_in.readline()

while (line):

    line = line.split()

    if (len(line) > 1 and line[1] == 'Time'):

        time = line[3]
        f_out.write("{0:e}\t".format(float(time)))
        for i in sensors.keys():
            f_out.write("{0:e}\t".format(float(sensors[i][1])))
        f_out.write('\n')
        

    elif (len(line) > 0 and line[0] != '#'):

        if line[0] in sensors:
            strain = line[2:11]
            sensors[line[0]][1] = strain[0]

    line = f_in.readline()


f_in.close()
f_out.close()
