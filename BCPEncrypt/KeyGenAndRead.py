# coding=utf-8
'''
Created on May 24, 2017

@author: lhd
'''

from BCP import *
from charm.core.math.integer import serialize,deserialize
import time
#===============================================================================
# this function will Generator bcp parameters,includes:
# public parameters: N2,N,k,g (write in to file named 'param')
# master key (write into file named 'mk')
#===============================================================================
def keyGen(secparam = 1024,paramPath = 'param',mkPath = 'mk'):
    bcp = BCP(secparam)
    MK = bcp.GetMK()
    param = bcp.GetParam()
    file = open(paramPath,'w')
    file.write(serialize(param.N2)+'\n')
    file.write(serialize(param.N)+'\n')
    file.write(serialize(param.k)+'\n')
    file.write(serialize(param.g))
    file.close()
    
    file2 = open(mkPath,'w')
    file2.write(serialize(MK['pp'])+'\n')
    file2.write(serialize(MK['qq']))
    file2.close() 
    

def genBCPContext(paramPath = 'param'):
    param = readParamFromFile(paramPath)
    bcp = BCP(param = param)
    return bcp
    
def genKeyPair(bcp,keyPairPath = 'keyPair'):
    pk,sk = bcp.KeyGen()
    file = open(keyPairPath,'w')
    file.write(serialize(pk)+'\n')
    file.write(serialize(sk))
    file.close()
    
    return pk,sk

def readParamFromFile(paramPath = 'param'):
    file = open(paramPath,'rb')
    param = Param()
    param.N2 = deserialize(file.readline())
    param.N = deserialize(file.readline())
    param.k = deserialize(file.readline())
    param.g = deserialize(file.readline())
    file.close()
    return param

def readMKFromFile(mkPath = 'mk'):
    file = open(mkPath,'rb')
    MK = {} 
    MK['pp'] = deserialize(file.readline())
    MK['qq'] = deserialize(file.readline())
    file.close()
    return MK

def readKeyPairFromFile(keyPairPath = 'keyPair'):
    file = open(keyPairPath,'rb')
    pk = deserialize(file.readline())
    sk = deserialize(file.readline())
    file.close()
    return pk,sk
    