# Trezor Crypto
Is a MIT licensed cryptographical library develop by Satoshi Labs. The algorithms are heavily optimized for use in embedded devices which may lack necessary memory, CPU power or both for conventional/naive implementations of algorithms.

List of features is here:
-   AES/Rijndael encryption/decryption
-   Big Number (256 bit) Arithmetics
-   BIP32 Hierarchical Deterministic Wallets
-   BIP39 Mnemonic code
-   ECDSA signing/verifying (supports secp256k1 and nist256p1 curves, uses RFC6979 for deterministic signatures)
-   ECDSA public key derivation
-   Base32 (RFC4648 and custom alphabets)
-   Base58 address representation
-   Ed25519 signing/verifying (also SHA3 and Keccak variants)
-   ECDH using secp256k1, nist256p1 and Curve25519
-   HMAC-SHA256 and HMAC-SHA512
-   PBKDF2
-   RIPEMD-160
-   SHA1
-   SHA2-256/SHA2-512
-   SHA3/Keccak
-   BLAKE2s/BLAKE2b
-   Chacha20-Poly1305
-   unit tests (using Check - check.sf.net; in test_check.c)
-   tests against OpenSSL (in test_openssl.c)
-   integrated Wycheproof testsi

Relevant links:
https://github.com/trezor/trezor-crypto
https://github.com/trezor/trezor-firmware/tree/master/crypto