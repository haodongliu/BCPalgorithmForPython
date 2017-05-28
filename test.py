#!/usr/bin/env python
# coding=utf-8
from BCPEncrypt.BCP import *
from BCPEncrypt.KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize

######            setup                #####
#keyGen(secparam = 1024,paramPath = 'BCPEncrypt/param',mkPath = 'BCPEncrypt/mk')
MK = readMKFromFile(mkPath = 'BCPEncrypt/mk')
############################################

##### get BCP context and generate pk,sk#####
########################################
bcp = genBCPContext(paramPath = 'BCPEncrypt/param')
pk,sk = genKeyPair(bcp,keyPairPath = 'keyPair')
#next time directly read pk,sk from file
#pk,sk = readKeyPairFromFile(keyPairPath = 'BCPEncrypt/keyPair')
# print pk,sk
#############################################

######            Encrypt               #####
#############################################
ciphertext1 = bcp.Encrypt(pk, 12)
ciphertext2 = bcp.Encrypt(pk, 18)
print ciphertext1 #print two line ciphertext
############################################

######       Decrypt with sk            #####
#############################################
m = bcp.Decrypt(ciphertext1,sk)
print m # m = 12
############################################

#####        Decrypt with MK            #####
#############################################
m = bcp.DecryptMK(ciphertext1,MK,pk)
print m # m =12
#############################################

#####           Computation             #####
############################################
ciphertext3 = bcp.multiply(ciphertext1, ciphertext2)
print bcp.Decrypt(ciphertext3,sk) # 12+18 =30

ciphertext3 = bcp.exponentiate(ciphertext3,2)
print  bcp.Decrypt(ciphertext3,sk) # 30 * 2 = 60
###########################################
