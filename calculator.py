#!/usr/bin/env python3

import sys
import math

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

try:
    salary = sys.argv[1]
    income = int(sys.argv[1]) - 3500
except ValueError:
    print("Parameter Error")
else:
    if 0 <= income <= 1500:
        taxable = (income * level) - deduct
        print('{:.2f}'.format(taxable))
    elif income <= 0:
        print ('0.00')
    elif 1500 < income <= 4500:
        taxable = (income * onelevel) - onededuct
        print('{:.2f}'.format(taxable))
    elif 4500 < income <= 9000:
        taxable = (income * twolevel) - twodeduct
        print('{:.2f}'.format(taxable))
    elif 9000 < income <= 35000:
        taxable = (income * threelevel) - threededuct
        print('{:.2f}'.format(taxable))
    elif 35000 < income <= 55000:
        taxable = (income * fourlevel) - fourdeduct
        print('{:.2f}'.format(taxable))
    elif 55000 < income <= 80000:
        taxable = (income * fivelevel) - fivededuct
        print('{:.2f}'.format(taxable))
    elif 80000 < income:
        taxable = (income * sixlevel) - sixdeduct

