# coding=utf-8
'''
Created on May 23, 2017

@author: lhd
'''
from charm.toolbox.integergroup import IntegerGroup
from charm.schemes.pkenc.pkenc_rsa import RSA_Enc, RSA_Sig
from charm.core.math.integer import integer,randomBits,random,randomPrime,isPrime,encode,decode,hashInt,bitsize,legendre,gcd,lcm,serialize,deserialize,int2Bytes,toInt


class Param():
    def __init__(self):
        pass
    def setParam(self,N2,N,g,k):
        self.N2 = N2
        self.N = N
        self.g = g
        self.k = k

class BCP():
    def __init__(self,secparam=1024,param = None):
        if param:
            self.N2 = param.N2
            self.N = param.N
            self.g = param.g
            self.k = param.k            
        else:
            self.p, self.q = randomPrime(secparam/2,True), randomPrime(secparam/2,True) 
            self.pp = (self.p -1)/2
            self.qq = (self.q - 1)/2
            self.N = self.p * self.q
            while True: # choose a good N
                if bitsize(self.N) ==secparam and len(int2Bytes(self.N)) == secparam/8 and ord(int2Bytes(self.N)[0]) &128 !=0:
                    break
                self.p, self.q = randomPrime(secparam/2,True), randomPrime(secparam/2,True) 
                self.pp = (self.p -1)/2
                self.qq = (self.q - 1)/2
                self.N = self.p * self.q
            self.N2 = self.N**2
            self.g = random(self.N2)
            one = integer(1)% self.N2
            while True: #choose a good g
                self.g = random(self.N2)
                self.g = (self.g-1)*(self.g-1)% self.N2
                if self.g == one:
                    continue
                tmp = self.g**self.p %self.N2
                if tmp == one:
                    continue
                tmp = self.g**self.pp % self.N2
                if tmp == one:
                    continue
                tmp = self.g**self.q %self.N2
                if tmp == one:
                    continue
                tmp = self.g**self.qq %self.N2
                if tmp == one:
                    continue
                tmp =self.g**(self.p*self.pp) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.p*self.q) %self. N2
                if tmp== one:
                    continue 
                tmp = self.g**(self.p*self.qq) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.pp*self.q) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.pp*self.qq) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.q*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp = self.g**(self.q*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp = self.g**(self.p*self.pp*self.q) % self.N2
                if tmp == one:
                    continue   
                tmp =self.g**(self.p*self.pp*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp =self.g**(self.p*self.q*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp =self.g**(self.pp*self.q*self.qq) % self.N2
                if tmp == one:
                    continue  
                break 
            self.k = integer((self.g**(self.pp*self.qq) - 1)) / self.N % self.N
            self.MK ={"pp":self.pp,"qq":self.qq}
    
    def GetMK(self):
        return self.MK
    
    def GetParam(self):
        param = Param()
        param.setParam(self.N2, self.N, self.g, self.k)
        return param
    
    def KeyGen(self):
        tmp = self.N2 / 2
        sk = random(tmp) % self.N2
        pk = (self.g**sk) % self.N2
        return pk,sk
    
    def Encrypt(self,pk,plaintext):
        r = random(self.N/4) % self.N2
        A = (self.g** r ) % self.N2 
        B1 = (self.N*plaintext+1)% (self.N2)
        B2 = (pk**r) % (self.N2)
        B = B1*B2 % self.N2
        ciphertext = {"A":A,"B":B}
        return ciphertext
    
    def Decrypt(self,ciphertext,sk):
        t1 = (ciphertext['B']*((ciphertext['A']**-1)**sk) -1) % self.N2
        m = integer(t1) / self.N
        return m
    
    def DecryptMK(self,ciphertext,MK,pk):
        k_1 = self.k ** -1
        tmp = (pk**(MK['pp']*MK['qq']) -1) 
        tmp = integer(tmp) /self.N 
        a = tmp * integer(k_1) % self.N
        
        tmp = ciphertext['A'] **(MK['pp']*MK['qq']) -1
        tmp = integer(tmp) /self.N 
        r = tmp * integer(k_1) % self.N
        
        gama = a*r %self.N
        sig = ((MK['pp']*MK['qq'])%self.N) **-1
        
        tmp = (self.g **-1)**gama
        tmp = ciphertext['B'] *tmp    
        tmp = tmp**(MK['pp']*MK['qq']) -1
        tmp = integer(tmp) /self.N
        
        m = integer(tmp) * integer(sig) %self.N
        return integer(m) 

    def multiply(self,ciphertext1,ciphertext2):
        ciphertext={}
        ciphertext['A'] = ciphertext1['A'] * ciphertext2['A']
        ciphertext['B'] = ciphertext1['B'] * ciphertext2['B'] 
        return ciphertext

    def exponentiate(self,ciphertext,m):
        text={}    
        text['A'] = ciphertext['A'] **m % self.N2
        text['B'] = ciphertext['B'] **m % self.N2
        return text  
  
