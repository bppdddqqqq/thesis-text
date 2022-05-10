---
source: https://keyst.one/
---
# Cobo Vault (now Keystone Pro)
Is an airgapped hardware cryptowallet powered by custom fork of Android OS and custom hardware. The device prides upon it's airgapped nature up to you a point of not being able to directly charge the device while it's powered on and no communication modules.

## At a glance

### Transparency
Most of the OS and hardware, and SE firmware are fully open-source and available on their [github](https://github.com/KeystoneHQ) and [github repo](https://github.com/KeystoneHQ/Keystone-developer-documents/tree/main/hardware). The device also has a publicly released third-party code audit at https://github.com/KeystoneHQ/Keystone-developer-documents/tree/main/audit-report.

The ~~SE schematics, spec sheet are proprietary and can be accessed under an NDA~~, the only thing under NDA is the self-destruct mechanism, which is stated here:
```The self-destruct mechanism has been removed from the schematic as we chose not to disclose all of its functionality. In order to minimize the attack surface, we do not share detailed information on the Secure Element. For researchers who are interested in our Secure Element design, you can request we share the development board, datasheet, and other materials under NDA (required by our Secure Element vendor). Contact us at [eng@keyst.one](mailto:eng@keyst.one)```

MCU (SOC) is internally coded as Cobo CBYXM001 in BOM. The device thus far seems to hint, that they use fully custom SOCs, which may make creation of fakes much harder. The MCU is ARMv7 based.

The Secure Element is custom-made as well, and the specsheet can be found here - [https://github.com/KeystoneHQ/Keystone-developer-hub/blob/main/se/Keystone_Secure_Element_Datasheet.md](https://github.com/KeystoneHQ/Keystone-developer-hub/blob/main/se/Keystone_Secure_Element_Datasheet.md). 
```
Keystone's Secure Element is a 32-bit security microcontroller, which is specifically targeted at low-cost and low-power fields. The Secure Element is an ARM Cortex M0 microcontroller integrated with a variety of secure cryptographic modules, including the SM1, SM2, SM3, SM4 algorithm, as well as RSA/ECC, DES/3DES, AES128, AES192/256, SHA1/256, SHA384/512 and other internationally recognized security algorithms. It supports true random number generation (TNRG). The Secure Element provides a variety of peripheral interfaces: USB2.0 full speed, SPI, UART, ISO7816, I2C, etc. built-in ROSC, and also supports crystal-free applications.

Keystone's Secure Element has a 256K byte on-chip eFlash, 16K bytes of ROM, 16K bytes of on-chip SRAM, and 4K bytes of dedicated SRAM algorithm, of which on-chip ROM provides various algorithm interface programs for developers. It improves the development efficiency and optimizes system performance.
```

This document had been released after rebranding and partially redisigning their device from Cobo Vault to KeyStone Pro. The rebrand was followed by spinning off from the parent Cobo company onto a separate business entity for management reasons, since Cobo had started focusing on their software segment and was uninterested in maintaining their hardware division. Cobo is maintaining the former device with maintenance patches.

An article by Nick Johnson had been released, that prior publication of this specsheet had tried to disassemble the device and assess what hardware is being used - [# Defeating the Cobo Vault Pro’s Self-Destruct Mechanism](https://medium.com/swlh/defeating-the-cobo-vault-pros-self-destruct-mechanism-abf321e2f5b5). Also it has x-ray scans of the hardware and the still redacted anti-tamper mechanism.

The communication between SOC and SE is done via serial port, according to the [https://github.com/CoboVault/cobo-vault-cold](https://github.com/CoboVault/cobo-vault-cold), quoting:
```
Interaction with the Secure Element (SE) via serial port, open source SE firmware can be found at [cobo-vault-se-firmware](https://github.com/CoboVault/cobo-vault-se-firmware). Transaction data is signed by the Secure Element and the generated signature is sent back to the application. This signature and other necessary messages are displayed as a QR code. You can check the animation on our webpage to see the whole process. Users use their mobile or desktop application to acquire signed transaction data and broadcast it.
```

Some parts of the OS are removed due to vendor requirements and require an NDA. 

In addition, the circuitry related to the anti-tampering mechanism are hidden in publicly available schematics and require an NDA as well. What's known is, that it uses an internal battery to power the circuitry, with the battery lasting according to manufacturer around 2 years. If the battery dies, so does the anti-tampering safeguard (TODO, find out more).
Personally, I perceive this kind of security measure as an act of planned obsolescence than as a security feature. Especially with such a short timeframe. A better improvement would've been making the battery user removable.

~~For the reasons above, the BOM and schematics don't describe the full device but only a part of it, requiring some amount of work to get complete picture of the device.~~

Cobo also has a GitHub guide for implementing the communication API to facilitate communication with other clients. It uses Bitcoin Uniform Resources which is also used on [[Foundation Passport]]. 

### Software client
Cobo used to support the device with their own app called Cobo Vault. Due to the discontinuation of the device by the original team and change of focus by Cobo, the app is now deprecated for usage.

Sparrow Wallet supports linking with Cobo and Keystone.

### Optional features
- Pro edition contains physical anti-tampering safeguard, on attempted opening of the device it will wipe the contents of the NAND flash (https://blog.keyst.one/self-destruct-mechanisms-unique-defense-against-side-channel-attacks-4cfea3d4eff1)
- Upgrade to bitcoin-only firmware, this is one-way only
- Higher-tier Pro edition contains a fingerprint reader
- [[Shamir backup]]
- PRNG Entropy modification via physical dicerolls
- Pattern lock for easier access to device (not to sign transactions though)

### Security
The device's SE hides a special keypair assigned at manufacturing, which atestates genuity of the SE and the device itself. This challenge is done by reading special QR codes which validate if the messages are signed properly, if not, the device is not genuine.

https://blog.keyst.one/web-authentication-a-counter-to-supply-chain-attacks-62d0272f656b

The pro edition contains a fingerprint reader for validating transactions and fast unlocking of the device. The device uses a master password for encrypting data and unlocking the device.

https://blog.keyst.one/keystone-product-design-principles-cd833bc11125

---

Cobo Vault and Keystone Pro are virtually the same device, with minor hardware differences, which makes both devices different. Both devices are designed by the same development team formerly part of Cobo company and spun off into a separate company.

Maintenance on Cobo Vault's firmware is already limited by the fact, that the device had been discontinued from manufacturing and is maintained by Cobo, supposedly applying only minimal maintenance to it's product.

Source: [Leaving Cobo to continue the Cobo Vault legacy | by Lixin Liu | Keystone](https://blog.keyst.one/leaving-cobo-to-continue-the-cobo-vault-legacy-29bb2f8f026e)

The difference on Keystone and Cobo stems on more technical side of things, such as placement of SD card slot, and support for greater capacity SD cards. Aside from that, the software foundation is the same on both the SOC (frontend and parser), and SE (backend). 

The SE according to the available documentation allows efficient usage of known cryptographic algorithms. On the github repository, the firmware hosts .lib files for ecdsa and rsa, which either hint for software-based implementation of the cryptographic algorithms. ([cobo-vault-se-firmware/source/driver at 29321e8c0efb41069c62860d9e670201e3aab749 · CoboVault/cobo-vault-se-firmware · GitHub](https://github.com/CoboVault/cobo-vault-se-firmware/tree/29321e8c0efb41069c62860d9e670201e3aab749/source/driver))

Another thing to note, that the firmware seems to utilise an anti-tamper mechanism, which checks for illicit inputs to GPIO pins of the SE (https://github.com/CoboVault/cobo-vault-se-firmware/blob/29321e8c0efb41069c62860d9e670201e3aab749/source/main.c#L104).

The logic is located here (https://github.com/CoboVault/cobo-vault-se-firmware/blob/29321e8c0efb41069c62860d9e670201e3aab749/source/main.c#L225), if at any point during the idle mode of the SE a trip flag called `defense_trig_flag` gets set to true (this happens if illicit inputs are inputted into SE's GPIO pins), the device irrevocably wipes the SE of it's settings, wallets and webauth keys and fallbacks into a `HDW_STATUS_ATTACK` mode. 

This defense measurement seems to prevent possible attack via voltage glitching or feeding invalid inputs into device's GPIO pins. One important thing to note, that device's tamper check is disabled if `emHDWstatus` of the device is set to `E_HDWS_CHIP` or `E_HDWS_FACTORY`.

---


### Physical security
The packaging is protected by holographic anti-tampering tapes.

The security of the device is very strict. The device is truly airgapped, even charging the device requires to shut down the device and physically remove the battery.

The Pro edition of the hardware contains a physical anti-tamper mechanism which wipes the device if any attempts are made to access the device via it's display panel. If the anti-tamper mechanism is tripped, the device immediately wipes the NAND, thus bricking the device.

https://blog.keyst.one/self-destruct-mechanisms-unique-defense-against-side-channel-attacks-4cfea3d4eff1

### Privacy
The device relies on a software wallet to do it's work, reducing confidentiality of the funds on the device.

## Non-hardware related

### Manual
Manual is located https://support.keyst.one/. It's 

### Support
They have a web support located here https://keystonewallet.atlassian.net/servicedesk/customer/portal/1

## Upgradability
The firmware is regularly updated, and the update is loaded into an external SD card. The hardware seems to be beefy enough to support even the most demanding cryptocurrencies and 4 GB NAND (according to the BOM) and SD card slot gives a big space for expandability in the future.
