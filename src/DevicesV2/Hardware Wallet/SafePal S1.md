---
source: https://shop.safepal.io/products/safepal-hardware-wallet-s1-bitcoin-wallet
---
# SafePal S1
A budget device designed and created by SafePal Inc., backed by Binance Labs an R&D and strategical investment unit of Binance focused on Web3 and Cryptocurrencies, a well-known cryptocurrency exchange formerly based in Hong Kong, but after the national restrictions on cryptocurrencies, they've changed their base of operations to Malta. 

## At a glance

### Transparency
The transparency of the device is practically none regarding it's software and hardware. The designers of the hardware are stating, that the device is powered by an EAL5+ certified Secure Element. Specifications of this secure element are unknown, and is subject of research.

A research from Kraken Security had revealed that the SOC is a SafePal S1 IDC80X1E, a propriatary AllWinner i3 processor [Allwinner_i3_Datasheet_V1.0.pdf (odroid.com)](https://dn.odroid.com/obsolete/Allwinner_i3_Datasheet_V1.0.pdf). They also had managed to dump the contents of the flash memory located on the PCB and seems to contain a Linux powered kernel with several GPL licensed libraries and software, and with the closed-source firmware it's not compliant with GPL licensing terms and could lead to possible litigation.

SE has no information and was impossible to track the vendor according to it's pinouts.

According to the statement by SafePal [here](https://blog.safepal.io/our-response-to-the-security-findings-from-kraken-security-labs/), the device was supposed to opensourced by 2021 per their roadmap, but as of the date of writing this is still not true. In the same statement they also mention, that "open-source is a double-sided sword", which expresses strong reluctance to make the device specifics public.

Also the statement seems to host a very hostile stance against Kraken, either stating they haven't had done their work enough, or that the research has no impact. This similar rethoric can be found on [[BC Vault]]'s statements and PR

### Software client
The device seems to require usage of their also propriatary SafePal App. The software serves as means of managing and activating the device. Since the device uses only QR codes for communication, it's probably that it may support ["Bitcoin Uniform Resources"](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) encoding standard. 

Upon further research this haven't been proven conclusive. BURs strive to make the pairing process one-way, with output send say to Sparrow Wallet or other apps to be as frictionless as possible. In case of SafePal this isn't the case, the device requires a pairing code, which 

todo: research possibility of how SafePal used to operate the device between 2019.05 and 2020.05, since there wasn't a SafePal app.

### Optional features
todo: requires walkthrough

### Security
The device does all of it's calculations and input in-hardware, to authenticate the user must enter a PIN code. 

### Physical security
Packaging is sealed with a holographic seal, inside the package there is the device and USB cable. Device needs to be cleared by SafePal's servers before being used by the user via a validation process, where SafePal validates that the device is legitimate and isn't manufactured by malicious party.

From the official documentation, there are supposedly chips, and security measurements located on-chip and also on the PCB. According to the official documentation article [Independent security element & multi-sensors - SafePal Knowledge Base](https://docs.safepal.io/safepal-hardware-wallet/security-features/hardware-security/independent-crypto-element), the device has modules for abnormal voltage detection, electromagnetic attack detection, light sensors, pulse sensors, temperature sensors and at last a metallic RF shield.

These modules are then utilized to protect the device from possible tampering and if the device is being tampered with wipes all data/RAM on-device.

A research from Kraken Security tested the physical security of the device and had found, that the device can be easily tampered and the self-destruction mechanism seems to not trigger as it may be interpreted from the marketing materials by general consumer. And on the self-destruction "Notably, no reset of the device took place, and the old credentials (PIN etc) stayed valid."

The research was released on Feb 2021, SafePal had released a statement ( [Stay tuned of the latest updates and announcements of SafePal](https://blog.safepal.io/our-response-to-the-security-findings-from-kraken-security-labs/) ) about Kraken's findings and stated, that opening up the device and popping open the RF-lid doesn't threaten device's security and that the security is "embedded in many details on the SafePal S1 at hardware level". Whether this is true is discutable, since there isn't any other research being done on the device. 

### Privacy
Hardware, software is propriatary. The only way to use the wallet is via a closed-source application on mobile phones. Privacy is thus limited by the EULA, another word of concern can be, that SafePal seems to be under strong influence of Binance, with tight integration with their platform and receiving strategic investments from their Lab unit.

Todo: study EULA and what the app seems to disclose to Binance

## Non-hardware related

### Manual
There is a paper manual in the packaging and a web manual [User manual - SafePal Knowledge Base](https://docs.safepal.io/safepal-hardware-wallet/user-manual).

### Support
Support is offered through their [SafePal Help Center (zendesk.com)](https://safepalsupport.zendesk.com/hc/en-us). 

## Upgradability
The device is updated via USB by uploading a firmware image to the device. The firmware image can be downloaded here [SafePal Wallet App Upgrade to the newest version](https://safepal.io/upgrade). Before version v1.0.12 there was a requirement of retyping and recovering the seed phrases because the device did a full wipe every single time. From v1.0.13 this stopped being a problem, but the manufacturer recommends backing up the seed phrases. 