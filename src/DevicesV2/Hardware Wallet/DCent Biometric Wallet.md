---
source: https://dcentwallet.com/products/BiometricWallet

---
# D'Cent Biometric Wallet
One of the few cryptowallets analyzed that also offers biometric authentication for the users, aside from the standard PIN authentication. The device prides itself as one of the top devices for managing ERC20/ERC721 based tokens, with plentiful support for various cryptocurrencies and being able sign things via phone easily using Bluetooth.

## At a glance

### Transparency
The hardware is publicly a blackbox, the specifications are vague and it's not trivial to find out which SOC/SE they use. From the FCC filing (https://fccid.io/2ASN5-DCENT-ID-BLK) (all radio communication devices require an FCC filing to be sold in the US), the hardware seems to contain three chips according to the teardown of internal hardware (https://fccid.io/2ASN5-DCENT-ID-BLK/Internal-Photos/Int-Photos-4213743). From the photos it can be roughly seen that the manufacturer is ST Microchips, a favourite among many hardware cryptowallet manufacturers.
This can be supported by the Amazon.com listing which mentions ST as manufacturer of the SOC, and it also mentions that the device has 1 MB of flash storage, but it's unknown whether the flash storage is actually flash or is just programmable memory of the SOC. (https://www.amazon.com/DCENT-Biometric-Wallet-Cryptocurrency-Bluetooth/dp/B07P3XZKWV).
Security audit done independently by Coinspect states that the device has an STM SOC and an NXP based SE (https://medium.com/dcentwallet/coinspect-audit-of-the-dcent-wallet-b8a6cf50cfa4).
Plus, it's important to note minor discrepancies between what is listed on the dcentwallet.com's consumer spec sheet, FCC filing and Amazon.com listing.  
Not only the hardware is black boxed, but also the firmware is proprietary, their firmware GitHub only serves as a CDN for delivering compiled binary blobs. (https://github.com/DcentWallet/biometric-firmware).
The only thing with publicly accessible source code is their SDK for connecting the hardware with web apps or web3 dApps.

### Software client
Their client is called D'Cent Hardware Wallet, and serves as the official app for managing both the Biometric Wallet and also their product range called Card Wallet. // PLATFORM?!
The software is used for updating the hardware and signing transactions. According to the manual and KB, most of the operations are done in the device and they leave the software client only for things not possible to be done anywhere else.
Similarly to hardware and firmware, the client is also proprietary, which raises concerns about vulnerabilities.
### Optional features


### Security
The device offers authentication via PIN and fingerprint. All payments must be paid is

### Physical security
Packaging is only sealed by a simple sticker that tells the user that the refund right is void if torn out. There are no other security elements

### Privacy
The device relies on software wallet to do it's work, reducing confidentiality of the funds on device.
The biometric data are stored in device with no apparent risk of them being leaked out.

## Non-hardware related

### Manual
The manual is located at https://userguide.dcentwallet.com. The manual is well written to explain all the processes and agendas that can be done on the Wallet. Big plus can be also given towards the FAQ section responding to the most common questions, which a first time user or entusiast would have.

Developer guide for integrating the wallet with services and software is located in a separate page at https://dev-docs.dcentwallet.com and explains only essential things how to setup their SDKs
### Support
Aside from FAQ/manual section, they also have a mail support located in the main website at https://dcentwallet.com/support/Questions

## Upgradability
The device is constantly updated with firmware updates, that contain new coin support or security features, not excluding security patches. Due to the uncertainty of the specified hardware specs, we can only guess the support and possible future-proofness of the device. 