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
    def calculator(self):
        for k,value in self.salary().items():
            try:
            jobnu,salary = item.split(':')
            salary = int(salary)
        except ValueError:
            print("Parameter Error")
        else:
            if salary > 3500:
                inc = salary - baoxian(salary) - 3500
                yinnashui(inc)
                print(jobnu +':'+ '{:.2f}'.format(salary-yinnashui(inc)-baoxian(salary)))
            else:
                inc = salary - baoxian(salary)
                print(jobnu +':'+ '{:.2f}'.format(inc)) 
                

if __name__ == '__main__':
    pwdfile = findpwd(sys.argv[1:])
    m_pwd = os.path.join('/home/shiyanlou/demo/filetiaozhan',pwdfile.d_pwd())
    #config = Config(m_pwd)
    userdata = UserData(m_pwd)
    userdata.calculator()
    #print(config.get_config('ShiYe'))

