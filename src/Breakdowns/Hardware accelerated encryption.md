On topic of accelerated hardware encryption. Only a subset of cryptowallets support true hardware-accelerated encryption.

In case of devices based on Microchip SOCs, the devices support a form of hardware acceleration for publicly known cryptographic methods/algorithms, like RSA, ECC, AES. Depending on whether it is an SOC or SE, the variety of support ranges from better in case of SEs and worse in case of SOCs.
This cannot be stated about SOCs manufactured by ST Technologies. Where the devices must rely on embedded SE chips or coprocessors to HW accelerate any processes or in case of some devices just rely on SW calculation. The only security related item that can be found in all chips is a hardware-based PRNG generator, allowing to secure better entropy from the outer world.  

Their SE's are much better tooled with a dedicated coprocessor called NESCRYPT

