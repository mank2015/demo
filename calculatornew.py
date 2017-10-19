#!/usr/bin/env python3

import sys

def lary(agrv):
    for item in agrv:
        try:
            jobnu,salary = item.split(':')
            salary = int(salary)
        except ValueError:
            print("Parameter Error")
        else:
            inc = salary - baoxian(salary) - 3500
            yinnashui(inc)
            print(jobnu +':'+ '{:.2f}'.format(salary-yinnashui(inc))) 

def baoxian(gongzi):
    baoxianfei =  gongzi * (0.08+0.02+0.005+0.06)
    return baoxianfei

def yinnashui(income):
    level = 0.03
    onelevel = 0.1
    twolevel = 0.2
    threelevel = 0.25
    fourlevel = 0.3
    fivelevel = 0.35
    sixlevel = 0.45

    deduct = 0
    onededuct = 105
    twodeduct = 555
    threededuct = 1055
    fourdeduct = 2755
    fivededuct = 5505
    sixdeduct = 13505
    if 0 <= income <= 1500:
        taxable = (income * level) - deduct
    elif income <= 0:
        print ('0.00')
    elif 1500 < income <= 4500:
        taxable = (income * onelevel) - onededuct
    elif 4500 < income <= 9000:
        taxable = (income * twolevel) - twodeduct
    elif 9000 < income <= 35000:
        taxable = (income * threelevel) - threededuct
    elif 35000 < income <= 55000:
        taxable = (income * fourlevel) - fourdeduct
    elif 55000 < income <= 80000:
        taxable = (income * fivelevel) - fivededuct
    elif 80000 < income:
        taxable = (income * sixlevel) - sixdeduct
    return taxable
if __name__ == '__main__':
    
    lary(sys.argv[1:])
