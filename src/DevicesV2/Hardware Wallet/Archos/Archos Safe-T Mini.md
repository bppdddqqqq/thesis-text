---
source: https://shop.archos.com/fr/hardware-wallets/588-archos-safe-t-mini-0690590037069.html
---
# Archos Safe-T Mini
A cryptowallet created by a french manufacturer Archos. The device forks Trezor One's firmware, specifically from commit hash [bfb8dda](https://github.com/archos-safe-t/safe-t-mcu/commit/bfb8dda5e8582b9e17bca0904affd8bfdf1b6652).
## At a glance

### Transparency
The firmware is based upon [[Trezor One]]'s 1.6.1 firmware with modifications done to the storage controller to support a [[Microchip AT88SC0104CA]] secure memory, which should guarantee higher level of protection regarding storage of cryptographical seeds.

The source code has traces of vulnerable U2F implementation patched on Trezor One's [firmware 1.7.2](https://blog.trezor.io/details-about-the-security-updates-in-trezor-one-firmware-1-7-2-3c97adbf121e). Whether the device supports U2F is unknown, but from prior observation of the manual that's not the case. Archos also had forked and modified every single repository relevant to Trezor One hardware.

[Safe-T Link](https://github.com/archos-safe-t/safe-t-link) - Is a forked Trezor-Link 1.3.8 library with modifications to support Safe-T hardware and modifies target USB descriptors and address of the initial signed config file+relevant signature.

[Safe-T Common](https://github.com/archos-safe-t/safe-t-common) - Is a fork of repository called Trezor-Common, it removes Trezor device descriptors, which merges some changes to support Ethereum's IPFS storage of token info, introduces Archos' own pubkey for signing config.bin files, and modified array of supported coins.

[Safe-T MCU](https://github.com/archos-safe-t/safe-t-mcu) - is a forked Trezor One 1.6.1 firmware, replacing original storage driver with one supporting Microchip's secure memory IC embedded in the hardware. Also it  

The underlying hardware seems to be an open secret though, with no BOM or schematics available about the hardware - whether this device is also forked is unknown, because Trezor's schematics are licensed under "CERN Open Hardware Licence Version 2 - Strongly Reciprocal" license, which is copyleft on all modifications of the existing schematics. 


### Software client
Software client is a web-based [Archos Safe-T client](https://app.safe-t.io/). The client is based upon the existing Trezor protocol, thus there is a possibility that the device may link 

### Optional features
todo:

### Security
The security is similar to [[Trezor One]] with an exception of added SE to securely store data into an embedded SE.

### Physical security
The packaging is sealed by holographic seals on opening seams of the box. The box cannot be opened without tampering with the seals.

### Privacy
The device seems to require their propriatary client, whether it's possible to use [[Trezor Suite]] or [[Trezor Wallet]] to connect it with Safe-T is unknown.
The device relies on software wallet to do it's work, reducing confidentiality of the funds on device.

## Non-hardware related

### Manual
todo: 
### Support
todo:
## Upgradability
The device is no longer updated, the lastest firmware is 1.1.4 which had bee released on 13th December 2018. 