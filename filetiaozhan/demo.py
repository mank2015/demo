#!/usr/bin/env python3

import sys

args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
print(index)
print(configfile)
