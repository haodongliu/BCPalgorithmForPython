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
 2. Peter, A., Tews, E., & Katzenbeisser, S. (2013). Efficiently outsourcing multiparty computation under multiple keys.
IEEE Transactions on Information Forensics & Security, 8(12), 2046-2058.

> And also my paper (IEEE DSC on workshop PBD 2017)
> Time series discord discovery under Multi-party Privacy Preserving

## How to install
### OS (only available for Linux)
> I was developed this project on Ubuntu 17.04， and I used three encrypted library， gmp，pbc，and charm.
> Ubuntu has their own python environment, but I don't recommend to use the default Python，there are too many package you need to install in the following steps，so I recommend the anaconda, it already installed many useful packages. link: https://www.continuum.io/downloads/   For Chinese mainland developer, you can download anaconda from "tuna" https://mirrors.tuna.tsinghua.edu.cn/anaconda/

### GMP library
>

