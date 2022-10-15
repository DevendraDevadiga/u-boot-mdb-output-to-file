#!/usr/bin/env python3
#    A script to convert an U-Boot memdump to a text file
#
#    Copyright (C) 2022-23  Devendra Devadiga
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

import sys
import io

n = len(sys.argv)

if n < 2:
    print("Usage: python3 ", sys.argv[0], "logfilename", "[outputfilname]")
    sys.exit(0)

logfile = open(sys.argv[1], 'r')

if n >= 3:
    outputfile = open(sys.argv[2], 'wb')

logfile = open(sys.argv[1], 'r')
Lines = logfile.readlines()

for line in Lines:
    hex_data = line[:-18]
    hex_data = hex_data[10:]
    byte_data = bytes.fromhex(hex_data)
    outputfile.write(byte_data)

logfile.close()
outputfile.close()
