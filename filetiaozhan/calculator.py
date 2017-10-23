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
            for item in file:
                

if __name__ == '__main__':
    pwdfile = findpwd(sys.argv[1:])
    m_pwd = os.path.join('/home/shiyanlou/demo/filetiaozhan',pwdfile.c_pwd())
    config = Config(m_pwd)
    print(config.get_config('ShiYe'))

