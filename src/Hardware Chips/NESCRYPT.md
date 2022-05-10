# What is NESCRYPT
It seems to allow acceleration of cryptographic processes to a certain degree, but documentation-wise it's lacking on what SPECIFICALLY it HW accelerates. For explanation, here are 2 excerpts from official documentation of the [[ST33J2M0 SE]] and official security targets set by ST Technologies.

```
The NESCRYPT (NExt Step CRYPTo-processor) is the latest generation of ST
cryptographic accelerator providing native modular arithmetic for both GF(p) and GF(2n)
with a very high level of performance. NESCRYPT also includes dedicated instructions to
accelerate SHA-1 and SHA-2 family hash functions. NESCRYPT allows efficient and secure
implementation of almost all known public key cryptosystems with a high level of
performance.
```
Source: [[ANSSI-CC-cible_2010-02en.pdf]] page - 11

and...

```
The ST33Jxxx features hardware accelerators for advanced cryptographic functions. The EDES peripheral provides a secure DES (Data Encryption Standard) algorithm implementation, while the NESCRYPT crypto-processor efficiently supports the public key algorithm. The AES peripheral ensures secure and fast AES algorithm implementation.
```
Source: [[st33j2m0.pdf]] page - 3

Also, presence of NESCRYPT means existence of hardware acceleration encryption for ECDSA, which is paramount to signing transactions for Bitcoin protocol. The common criteria in question is FCS_COP.1.

Another helpful explanation can be found in the Security Target document for [[ST33J2M0 SE]]. 

```
The Security IC Embedded Software (ES) is in User NVM.

The TOE optionally comprises a specific application in User NVM: this applicative Embedded Software is a cryptographic library called NesLib. NesLib is a cutting edge cryptographic library in terms of security and performance. 

NesLib is embedded by the ES developer in his applicative code. Note that the NesLib RSA, ECC and Diffie-Hellman functions can only be used if Nescrypt is active, the NesLib AES functions can only be used if the AES accelerator is active and the NesLib EDES functions can only be used if the EDES+ accelerator is active. 

NesLib is a cryptographic toolbox supporting the most common standards and protocols: 
• an asymmetric key cryptographic support module, supporting secure modular arithmetic with large integers, with specialized functions for Rivest, Shamir & Adleman Standard cryptographic algorithm (RSA [17]), and Diffie-Hellman [23], 
• an asymmetric key cryptographic support module that provides very efficient basic functions to build up protocols using Elliptic Curves Cryptography on prime fields GF(p) with elliptic curves in short Weierstrass form [15], and provides support for ECDH key agreement [21] and ECDSA generation and verification [5].
• a module for supporting elliptic curve cryptography on Edwards curve 25519, in particular ed25519 signature generation, verification and point decompression [26]. 
• a cryptographic support module that provides secure hash functions (SHA-1(a), SHA-2 [4]), SHA-3, Keccak and a toolbox for cryptography based on Keccak-p, the permutation underlying SHA-3 [25], 
• a symmetric key cryptographic support module whose base algorithm is the Data Encryption Standard cryptographic algorithm (DES) [2], 
• a symmetric key cryptographic support module whose base algorithm is the Advanced Encryption Standard cryptographic algorithm (AES) [6], 
• support for Deterministic Random Bit Generators [19], 
• prime number generation and RSA key pairs generation [3]
```

The NESCRYPT module is practically just a hardware module and to utilise it's capabilities it's recommended to use ST's own library called Neslib, which is dependant on NESCRYPT. 