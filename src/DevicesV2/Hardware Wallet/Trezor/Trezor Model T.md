---
source: https://shop.trezor.io/product/trezor-model-t
---
# Trezor Model T
A more featured device compared to Trezor One, containing an SD card reader and a stronger [[STM32F427VIT6 SOC]], allowing greater support for more demanding cryptocurrencies and FIDO2 Authentication. FIDO2 authentication is theoretically possible to be implemented on lower-tier Trezor One, but the plans are currently on hold (https://www.reddit.com/r/TREZOR/comments/f8uza0/comment/finvd9n/?utm_source=share&utm_medium=web2x&context=3).  The device also features a touchscreen which is a departure from the computer-reliant input of Trezor One device, allowing the device to be a bit more airgapped by requiring entry of a PIN code on it's touch display rather than on the computer, which could be potential points of attack.

The device lacks an SE, similarly to Trezor One, which could be a matter of concern compared to its counterparts in this space. The device had as of the time of writing suffered only minor incidents, mostly related to malware/ransomware attacks on the computer (https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14199) or strongly physical attacks using voltage attacks (https://blog.trezor.io/our-response-to-the-read-protection-downgrade-attack-28d23f8949c6).

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
The wallet also contains support for U2F and FIDO2 authentication. In addition, in conjunction with Trezor's official software, the device may operate as an external encryptor/decryptor for it's built-in password manager called Trezor Password Manager.
Aside from standard BIP-39 support the device supports a custom feature called [[Shamir Backup]], which is an alternative to BIP-39 single-key'd recovery strategy

### Security
User can validate and authenticate on the device itself. The process of generating the wallet is done all in-device, including writing down the recovery seed and validating correct transcription of the seed. Recovery of the wallet is also done in-device, allowing complete secrecy of the recovery seed from an external attacker.

There is an option to set a specialized Wipe pin, which will irreversibly wipe the keys stored in the wallet in case of an attack. In case the attacker uses brute force, the device will wipe itself after 16 unsuccessful tries.

There is an optional added layer of safety by storing an additional encryption/decryption seed on the SD card, which would render the device useless without it. 

The device does not allow installation of any external software whatsoever, restricting potential attack points on the device itself.

### Physical security

The device's case is sealed shut and ultrasonically welded together, hardening access to the hardware. The packaging is protected by holographic tapes and the port is also sealed by a holographic seal, which renders the device useless unless it's torn off.

### Privacy
The device relies on software wallet to do it's work, reducing confidentiality of the funds on device.

## Non-hardware related

### Manual
The device doesn't have a very rich manual (only a quick start guide, which only instructs user on how to setup the device), the quality of documentation is at times poor and demands user to look up information or even how the precise processes look from the community on the internet, such as Youtube or Reddit.

### Support
Support is either done via Reddit (https://reddit.com/r/trezor), on their official website's forum (https://forum.trezor.io/) or via their email form (https://trezor.io/support/technical/issue/).

## Upgradability
With the device being the 2nd in line of their cryptowallets, the device has a much stronger support for more demanding cryptocurrencies. The most concerning thing would be lack of an SE, which per the claims of Trezor isn't essential due to its equal amount of attention given to security of not only the hardware but also the software and lack of any hardware acceleration for common cryptographical algorithms, which may will impact its longevity in case of a hypothetical introduction of multi-layered encryption schemes in cryptocurrencies. 