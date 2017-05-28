# coding=utf-8
'''
Created on May 22, 2017

@author: lhd
'''
import time
from BCP import *
from KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize
print 'begin()'

# start = time.clock()
# keyGen()
# print 'generator done, cost %s seconds',time.clock() - start

start = time.clock()
bcp = genBCPContext(paramPath = 'param')
# pk,sk = genKeyPair(bcp, keyPairPath = 'keyPair')

pk,sk = readKeyPairFromFile(keyPairPath = 'keyPair')

ciphertext1 = bcp.Encrypt(pk, 12)
ciphertext2 = bcp.Encrypt(pk, 18)
for index in range(1000):
    ciphertext1 = bcp.multiply(ciphertext1,ciphertext2)
m = bcp.Decrypt(ciphertext1,sk)
print 'm is ',m
print 'generator done, cost %s seconds'%(time.clock() - start)

