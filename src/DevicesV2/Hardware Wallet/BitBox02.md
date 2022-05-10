---
source: 
---
# BitBox02
It is a small hardware wallet manufactured by a Swiss company called Shift Crypto. The device is released in two versions, one with general support for various cryptocurrencies and the other with support for Bitcoin only, known as Bitcoin-only edition. 

## At a glance

### Transparency
The hardware device is fully open-source with a permissive and derivation-allowed Apache 2.0 license. The repository for the firmware and schematics can be found [here](https://github.com/digitalbitbox/bitbox02-firmware). 

The firmware is coded primarily in Rust and C, with some support scripts written in Python for establishing the communication protocol between the device and host computer. The C code is bound to the Rust code. The firmware utilizes `libwally` for implementing cryptographical functions in the SOC and only it's the implementation of AES for encrypting seeds.

The primary logic resides in the Rust code, with C code serving more to write lower-level and optimized code. Protobuf is used to serialize and deserialize data used while the device is communicating with the software client or library.

There is a software library implementing BitBox02's communication API in Javascript [here](https://github.com/digitalbitbox/bitbox02-api-js). There is also a Go flavor of the library [here](https://github.com/digitalbitbox/bitbox02-api-go).

### Software client
There is a software client called BitBoxApp, which is an application written in Javascript and Go. 

Citing:
```
The wallet UI is a [React](https://reactjs.org/) single page webapp. It sources its data from the backend written in Go.

The Desktop app is a C++ Qt5 program containing only a `WebEngineView`, displaying the UI.

Static assets are sourced from a Qt rcc file, and the dynamic data is bridged from Go with WebChannels.

The Go library is compiled as a C library which exposes two functions only: one to set up the bridge, and one to invoke calls in the backend.

Similarly to the Desktop variant, the Go library can be compiled and added to an Android Studio / XCode project.
```

The hardware wallet can used without the included software. There is an official support for Electrum and Wasabi wallet. (ex. tutorial [here](https://shiftcrypto.ch/blog/bitbox02-with-electrum-wallet/)).

### Optional features
The hardware device supports U2F.

### Security
[[BitBox02]]'s firmware is publicly available on GitHub [bitbox02-firmware/src at master · digitalbitbox/bitbox02-firmware · GitHub](https://github.com/digitalbitbox/bitbox02-firmware/tree/master/src), as well as underlying specs and PCBs.

The architecture of the BitBox02 is similar to [[Ledger Nano S]], with MCU powered by [[Microchip ATSAMD51J20A-AU SOC]] operating all peripheral hardware of the device, which is the OLED, microSD card reader, slider buttons and finally the Secure Element powered by [[Microchip ATECC608A SE]].

This architecture had been historically flawed as it had been shown on [[f00dbabe]] exploit, which hijacked Nano S' MCU to show illicit information on the display confusing user into signing anything that the adversary had proposed.

Compared to other Secure Elements used say in Ledger or [[Cobo Vault]], the SE is not a fully-fledged MCU, but instead only offers a minimal feature set related to cryptography, keystore and communication between the SE itself and an MCU. Cryptography-wise, the SE fully implements and also hardware-accelerates algorithms like AES128, ECDSA, SHA256. Hardware acceleration according to the manufacturer prevents "usual high risk of key exposure that is endemic to standard microprocessors." (further prove?).

The device also supports authentication via public/private keys to prevent on-board tampering/intrusion.

A concernable thing is, that the secure element's manufacturer doesn't seem to assess any standardized level of evaluation assurance on the chip. This EAL level is commonly assessed on chips manufactured by Samsung or STElectronics, which can be easily found for example on websites of French security authority ANSSI, but this is not the case of Microchip's products lacking any entires on their website, or publicly on the internet as of time of writing. It's probable that these documents are available after signing an NDA. 

The firmware implementation fully acknowledges and respects the existence of this SE. Offloading most of the cryptographical operations to the SE. Implementation related to the communication between SE and MCU is located here - [bitbox02-firmware/securechip.c at master · digitalbitbox/bitbox02-firmware · GitHub](https://github.com/digitalbitbox/bitbox02-firmware/blob/master/src/securechip/securechip.c). The implementation also includes code which is executed at the factory setup and internal functions that help with access to the SE's data slots and counters.

The github repository forks part of the source code related to communication between SE and MCU from [GitHub - MicrochipTech/cryptoauthlib: Library for interacting with the Crypto Authentication secure elements](https://github.com/MicrochipTech/cryptoauthlib), which is the official library for all of their SEs. 

The [[Microchip ATECC608A SE]] albeit cannot protect the data from physical attacks, an exploit [[ATECC608A Laser Fault Injection]] exists which allows the adversary to attack the device and possible extract the seeds from the secure data banks. Whether this attack had been addressed is yet unknown.

### Physical security
The device has simple tamper-proof packaging. // todo: validate

### Privacy
The device doesn't need to rely on a vendor-provided software wallet to do its work, ensuring a higher level of transparency. In addition, the software is fully open allowing the user to verify the code running on the desktop client.

## Non-hardware related

### Manual
//todo

### Support
//todo

## Upgradability
//todo


https://github.com/digitalbitbox
https://github.com/digitalbitbox/bitbox02-firmware/tree/ea520f5156a64d3fc57eee8cffae505e674f646e/src/rust/bitbox02-rust/src
https://shiftcrypto.ch/app/
https://shiftcrypto.ch/bitbox02/bitcoin-only/
https://shiftcrypto.ch/bitbox02/threat-model/
https://saleemrashid.com/2018/11/26/breaking-into-bitbox/
https://github.com/digitalbitbox/bitbox-wallet-app
#wip