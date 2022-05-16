---
source: https://trezor.io/shamir/
wikisource: https://wiki.trezor.io/Shamir_Backup
devarticle: https://blog.trezor.io/https-blog-trezor-io-dev-corner-shamir-backup-guide-5f9957ff1008
---
# Shamir backup

This new security standard, Shamir Backup, counteracts the two greatest risks involved with protecting your recovery seed: theft and destruction.

## How it works

![](https://trezor.io/static/images/shamir_badges/shamir-lp-generate.svg)

### Generate

Choose how many recovery shares you want to generate, and decide how many of them you want to use for recovery.

![](https://trezor.io/static/images/shamir_badges/shamir-lp-distribute.svg)

### Distribute

Distribute those shares however you want, among people and/or secure locations.

![](https://trezor.io/static/images/shamir_badges/shamir-lp-relax.svg)

### Relax

Sleep peacefully knowing that your private keys are secured by Shamir Backup, safe from theft or accident.

# QA

### How is Shamir Backup different from the single recovery seed backup?

Shamir Backup lets you generate up to 16 recovery shares - sequences of 20 or 33 words. Single backup recovery seeds consist of 12, 18, or 24 words.

Shamir Backup also uses a different wordlist than the BIP-39 recovery seeds. In other words, some of the words used in Shamir backup recovery shares are never used in single seed backups and vice-versa.

### What happens if some of the shares get lost or stolen?

Shamir Backup offers a significant advantage compared to the single recovery seed. Individual shares do not leak any information about the shared secret, as long as the number of compromised shares does not reach the required threshold. In other words, if you use a 7-of-10 scheme and 5 of your shares get compromised, the attacker has no chance to reconstruct your wallet and cause trouble.


