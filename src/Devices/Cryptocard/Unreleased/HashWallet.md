---
source: https://www.gethashwallet.com
---
# HashWallet
As of writing, the unreleased hardware wallet device (14.2.2022) boasts high security and adaptability. It was developed by eSignus, a company founded to create and develop the device.

```
WARNING: SPECULATION

The device is not as of yet released; most of the info can be critically out of date or may contain speculative arguments.
```

## At a glance

### Transparency
Because the device is not yet released, the only information we can infer are from the marketing videos, their IndieGogo campaign, and the official website.

There is a severe discrepancy between the hardware specifications publicly listed on the website and what's genuinely inferred from the specs. The most significant discrepancy is on memory. They list out the memory of their chosen Apollo3 Blue SOC and copy-paste the memory to the memory for their remote backup device powered solely by [[Infineon SLE78 SE]].

Their blog at [https://esignus.medium.com](https://esignus.medium.com/) slightly details the development of their device and describes the eSignus company's history. 

There is also no real hardware demo of their latest unit. The only real demo can be found on Youtube, located [here](https://www.youtube.com/watch?v=KfnVWekIZd0). Their IndieGoGo campaign has a low amount of actual orders. Allegedly the device will receive FCC Certification; as of the time of writing (14.2.2022), there is no FCC certification uploaded yet or is uploaded under a codename not yet known. The FCC certification is necessary for sale in the US because it has Bluetooth and NFC radio embedded.

Initially, the hardware was conceived with the usage of already tried and tested ICs for Spanish ID cards, no longer valid - https://link.springer.com/article/10.1007/s12394-010-0041-3#Sec6 and https://esignus.medium.com/the-beginnings-of-esignus-and-hashwallet-8591efe5b69f

### Software client
It's supposedly tethered on an in-house HashWallet Client, 

This necessity is allegedly due to its non-programmable nature, containing only a secure HOLa Runtime and necessary tooling for managing the cryptographic keys/seeds.

HOLa, from what can be read on their blog, is a custom bytecode for operating the device and all of its cryptographic functions. This runtime according to their [Medium article](https://esignus.medium.com/an-overview-of-hola-and-its-macros-467b876f1368) entails how it operates on the protocol level (i.e. sending the program bundle with parameters to the wallet for processing).

### Optional features

### Security
The device uses a fingerprint reader, according to the spec sheet they use "FCP-1300 Fingerprint Reader IC".  Aside from this, there is no real knowledge about how the user gets authenticated into the wallet.

Another thing is that the device bundles in a separate device which serves as an external backup card, which stores the necessary cryptographical seeds onto a secure embedded device. Whether it's possible to backup the BIP phrase or data differently is still unknown, no possibility will hint into a vendor lock-in.

The security is better explained here - https://esignus.medium.com/what-are-the-key-aspects-of-security-in-hashwallet-5971bcdf570a

### Physical security

TBA

### Privacy
Privacy will highly rely on their HashWallet application than anything.

## Non-hardware related

### Manual
TBA

### Support
TBA

## Upgradability
Allegedly the device is non-programmable, instead relying on sending complete programs with set parameters for transaction requests, with user just approving the execution of said signature.
How this is achieved is still not yet known, TBA for release on device