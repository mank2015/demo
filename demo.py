#!/usr/bin/env python3

import sys

def lary(agrv):
    for item in agrv:
        jobnu,inc = item.split(':')
        inc = int(inc)
        salary = inc - baoxian(inc) - 3500
        print(baoxian(inc),inc,salary) 

def baoxian(gongzi):
    baoxianfei =  gongzi * (0.08+0.02+0.005+0.06)
    return baoxianfei

if __name__ == '__main__':
    lary(sys.argv[1:])
