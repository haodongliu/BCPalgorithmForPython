# BCPalgorithmForPython
The BCP Algorithm For Python2.7

## A brief overview about BCP algorithm

### Firstly we should know the concept of Additive Homomorphic Cryptosystem
> Suppose [M<sub>1</sub>]<sub>pk</sub> and [M<sub>2</sub>]<sub>pk</sub> are two additive homomorphic ciphertexts under the same public key pk. The additive homomorphic cryptosystem (AHC) has the additive homomorphic property:

> <center> D<sub>sk</sub> ([M<sub>1</sub>]<sub>pk</sub> * [M<sub>2</sub>]<sub>pk</sub>) = M<sun>1</sub> + M<sub>2</sub></center >

> **BCP** is an Additive Homomorphic Cryptosystem. besides, it has a special property which offers two independent decryption mechanisms, The second decryption mechanism decrypts given ciphertext successfully if and only if a certain master secret key is known.

#### The BCP algorithm and its properties
![image](http://github.com/haodongliu/BCPalgorithmForPython/raw/master/BCPEncrypt/img/BCP1.png)

![image](http://github.com/haodongliu/BCPalgorithmForPython/raw/master/BCPEncrypt/img/BCP2.png)

> To know more about the BCP algorithm and its properties, I highly recommend you to read the original paper
 1. Bresson, E., Catalano, D., Pointcheval, D.: A simple public key cryptosystem with a double trapdoor decryption mechanism and its applications. In: ASIACRYPT. LNCS, vol.2894, pp. 37–54. Springer (2003).
 2. Peter, A., Tews, E., & Katzenbeisser, S. (2013). Efficiently outsourcing multiparty computation under multiple keys.IEEE Transactions on Information Forensics & Security, 8(12), 2046-2058.

> And also my paper (IEEE DSC on workshop PBD 2017)

> Time series discord discovery under Multi-party Privacy Preserving

## How to install
### OS (only available for Linux)
> I was developed this project on Ubuntu 17.04， and I used three encrypted library， gmp，pbc，and charm.

> Ubuntu has their own python environment, but I don't recommend to use the default Python，there are too many package you need to install in the following steps，so I recommend the anaconda, it already installed many useful packages. link: https://www.continuum.io/downloads/   For Chinese mainland developer, you can download anaconda from "tuna" https://mirrors.tuna.tsinghua.edu.cn/anaconda/

### Environment
> sudo apt-get install m4

> sudo apt-get install pyparing (unnecessary)

> sudo apt-get install openssl-dev

> sudo apt-get install python-dev (necessary)

### GMP library
> For Ubuntu, you can directly install the gmp library with command “ sudo apt-get install libgmp-dev”

> For other linux system，you need to download the gmp source code and make. I have provided the source code in the folder “gmp-6.1.1”

> cd gmp-6.1.1  excute

> ./configure 

> make

> make install

### PBC library

> ./configure  

> make

> make install

> ln -s /usr/local/lib/libpbc.so.1 /usr/lib

### Charm Library (must installed openssl-dev,python-dev)
> ./configure.sh (notice that if you use anaconda, you need to change the python path in configure.sh line 134, change it to your anaconda's python path)

> make build

> make install

> ldconfig

## How To Use
### BCP SetUP
>  For BCP algorithm, the first thing we should to do is setup -- generate the public key and master key.
>>keyGen() Function, **def keyGen(secparam = 1024,paramPath = 'param',mkPath = 'mk')** it will generate:

     >>>1. public parameters: N2,N,k,g (write in to paramPath )
     
     >>>2. master key (write into paramPath)
>
>  After generated the public parameters, you can instantiate a BCP context by using parameters
>  bcp = genBCPcontext(paramPath = 'param')

### Generate KEYS
> And the pk and sk will be generated when you got the BCP context
> pk,sk = genKeyPair(bcp,  keyPairPath = 'keyPair')
>> generate pk and sk ( write into keyPairPath)
>
> When you get the key pair, you don't need to generate them again the next time, you can directly read it from file
> > pk,sk = readKeyPairFromFile(keyPairPath = 'keyPair')
	
### Encrypt
> You got pk, and BCP context now, so you can encrypt the number now,
	>> ciphertext1 = bcp.Encrypt(pk,12)
	>> ciphertext2 = bcp.Encrypt(pk,18)
	>> print ciphertext1 
	>>#it will show two line ciphertext

### Decrypt 
> there are two types decypt, decrypted by sk and decrypted by mk
> >with sk
> >>m = bcp.Decrypt(ciphertext1,sk)
> >>print m               
> >>#m = 12
> >>
>>with MK
>>> m = DecryptMK(ciphertext2,pk)
>>> print  m
>>>  #m = 18

### Computation 
>Multiply
>> ciphertext3 = bcp.multiply(ciphertext1,ciphertext2)
>> print Decrypt(ciphertext3,sk)
>>  #30
>>
>Exponentiate
>>ciphertext3 = bcp.exponentiate(ciphertext3, 2)
>>print Decrypt(ciphertext3,sk)
>>#60 (30*2)  

