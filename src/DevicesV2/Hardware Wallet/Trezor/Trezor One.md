---
source: https://shop.trezor.io/product/trezor-one-white
---
# Trezor One
First cryptowallet released by a company called [[Trezor]], previously a flagship model, it was superseded by [[Trezor Model T]] albeit the device still receives software via regular security patches and less frequent feature updates. Powered by [[STM32F205RE SOC]].

The device lacks an SE, which could be a matter of concern compared to its counterparts in this space. The device had as of the time of writing suffered only minor incidents, mostly related to malware/ransomware attacks on the computer (https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14199).

## At a glance
BECH32 - yes
Legacy Addresses - yes
Multisig - yes
Segwit - yes

### Transparency

The device is fully open-source, with both the software client and hardware itself being open-source and is deterministically manufactured. All hardware info is publicly available on their [GitHub](https://github.com/trezor/trezor-hardware/). The device is heavily audited not only by Trezor itself but also by independent developers, ensuring its security and soundness in safety. 
The developers had also released a full devkit specification with an emulator, that allows the developer to test out the wallet itself without physically having it.

### Software client
The device is managed by a software called [[Trezor Suite]], which not only doubles as a device manager but also as a crypto-wallet to manage all funds stored by the device.

### Optional features
The wallet also contains support for U2F. In addition, in conjunction with Trezor's official software, the device may operate as an external encryptor/decryptor for it's built-in password manager called Trezor Password Manager.

### Security
User can validate on the device itself. The process of generating the wallet is done all in-device, including writing down the recovery seed and validating correct transcription of the seed.

The rest of the processes are done out of the device, on a computer, which makes the device easily susceptible to attack from outside, such as hijacking the pincode, or recovery seed. 

There is an option to set a specialized Wipe pin, which will irreversibly wipe the keys stored in the wallet in case of an attack. In case the attacker uses brute force, the device will wipe itself after 16 unsuccessful tries.

The device does not allow installation of any external software whatsoever, restricting potential attack points on the device itself.

### Physical security

The device's case is sealed shut and ultrasonically welded together, hardening access to the hardware. The packaging is protected by very tight packaging, which demands irreparable damage to it, to access the device itself.

There had been a security incident, where due to the open-source nature of the device, there were clones of the device freely distributed in the wild.
https://blog.trezor.io/psa-non-genuine-trezor-devices-979b64e359a7

### Privacy
The device relies on software wallet to do it's work, reducing confidentiality of the funds on device.

## Non-hardware related

### Manual
The device doesn't have a very rich manual (only a quick start guide, which only instructs user on how to setup the device), the quality of documentation is at times poor and demands user to look up information or even how the precise processes look from the community on the internet, such as Youtube or Reddit.

### Support
Support is either done via Reddit (https://reddit.com/r/trezor), on their official website's forum (https://forum.trezor.io/) or via their email form (https://trezor.io/support/technical/issue/).

## Upgradability
The device is already superseded by [[Trezor Model T]] which creates a divide in support of cryptocurrencies/features and also range of support by the developers themselves. The device is still sold and there are currently no known plans of phasing out the device in favor of Model T, the weaker SOC could be concerning where there would be necessary support for more expansive improvements to protocols on already support cryptocurrencies.

The most concerning thing would be lack of an SE, which per the claims of Trezor isn't essential due to its equal amount of attention given to security of not only the hardware but also the software and lack of any hardware acceleration for common cryptographical algorithms, which may will impact its longevity in case of a hypothetical introduction of multi-layered encryption schemes in cryptocurrencies. 