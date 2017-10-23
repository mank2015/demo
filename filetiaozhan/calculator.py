#!/usr/bin/env python3
import sys
import os
class findpwd(object):
    def __init__(self, findpwdd):
        self._findpwdd = findpwdd
    def i_pwd(self):
        return self._findpwdd
    #@property
    def c_pwd(self):
        c_index = self.i_pwd()
        index = c_index.index('-c')
        c_index = c_index[index+1]
        return c_index
    #@property
    def d_pwd(self):
        d_index = self.i_pwd()
        index = d_index.index('-d')
        d_index = d_index[index+1]
        return d_index
    def o_pwd(self):
        o_index = self.i_pwd()
        index = o_index.index('-o')
        o_index = o_index[index+1]
        return o_index

class Config(object):
    def __init__(self, configfile):
        self._configfile = configfile
    def filepwd(self):
        return self._configfile
    def get_config(self,key):
        with open(self.filepwd()) as file:
            self._config = dict(line.strip().split('=') for line in file if line)
            self._con = {}
            for k,value in self._config.items():
                k = k.strip()
                value = value.strip()
                #return k,value
                self._con[k] = value
        return self._con[key]
                         
            #print(self._con)

class UserData(object):
    def __init__(self, userdatafile):
        self.userdata = {}
        self._userdatafile = userdatafile
    def salary(self):
        with open(self._userdatafile) as file:
            self.userdata = dict(line.strip().split(',') for line in file if line)
        return self.userdata
    def baoxian(self, gongzi):
        baoxianfei =  gongzi * (0.08+0.02+0.005+0.06)
        return baoxianfei
    def calculator(self):
        sala= []
        for k,value in self.salary().items():
            salary = int(value)
        
            if salary > 3500:
                inc = salary - self.baoxian(salary) - 3500
                calcul = salary-self.yinnashui(inc)-self.baoxian(salary)
                sala.append((k, calcul))   
                            
#innashui(inc)
               # print(k +':'+ '{:.2f}'.format(salary-self.yinnashui(inc)-self.baoxian(salary)))
            else:
                inc = salary - self.baoxian(salary)
                sala.append((k, inc))
                #print(k +':'+ '{:.2f}'.format(inc)) 
            print(sala)
            return sala
    def yinnashui(self, income):
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
        if 0 < income <= 1500:
            taxable = (income * level) - deduct
        elif income <= 0:
            taxable = 0
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
    pwdfile = findpwd(sys.argv[1:])
    m_pwd = os.path.join('/home/shiyanlou/demo/filetiaozhan',pwdfile.d_pwd())
    #config = Config(m_pwd)
    userdata = UserData(m_pwd)
    userdata.calculator()
    #print(config.get_config('ShiYe'))

