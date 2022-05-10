
---
source: https://shop.archos.com/fr/hardware-wallets/588-archos-safe-t-mini-0690590037069.html
---
# Archos Safe-T Touch
A crypto wallet created by a french manufacturer Archos. The device is as of yet uncovered with reviews. The overview for the device is just at-glance speculation, *tbd until I receive a device for review*

## At a glance

### Transparency
The device can broadcast by itself via Bluetooth connection with an internet-connected Android phone. The device itself doesn't have any Wi-Fi or Bluetooth radios. 

One invalid thing is their claim for EAL7 level of "military-grade security." This claim may be valid for small circuitry but not for the overall architecture of the device. The marketing material claims they use [[ST STSAFE-J102]] Secure Element; this SE is unfortunately certified at EAL5 level only, where or how they assert their EAL7 level of security is to be questioned.

The device seems to garner rather negative reception, with users claiming they've lost their funds or that the software in the hardware wallet is _buggy_. Due to a severe lack of varied professional reviews, it's tough to piece the initial impressions on the device (consumer reviews [(1)](https://archive.ph/SX8IA) and [(2)](https://archive.ph/rGG9P)). There is a "professional" review released [here](https://www.publish0x.com/pass-fire/archos-safe-t-touch-cold-wallet-at-a-glance-xlygljv).

Their hardware seems to be powered by a MediaTek MT65xx/MT66xx/MT67xx chip, according to the driver requirements for usage with the Updater tool. The device appears to run a flavor of Android OS; how secure the OS in question is unknown. The device could be related to the now-infamous BitFi Wallet ([ditto 1](https://www.digitaltrends.com/computing/hacker-doom-bitfi-mcafee-wallet/), [ditto 2](https://techcrunch.com/2018/08/30/john-mcafees-unhackable-bitfi-wallet-got-hacked-again/))

There is an FCC filing [here](https://fccid.io/SOVACSAFETT01); the filing had to be done because the device has a Bluetooth radio. The FCC filing contains photos of the hardware device, which describes its internals; the device is powered by [[MediaTek MT6739V]] SOC and MT6357V Power IC module chips and includes a Kingstone eMMC memory chip.  The SE in question is probably located on the motherboard, but the pictures are not of high resolution to read out information about the QN32 chips located on the motherboard. The device is also manufactured in China.

The general trust on this device is **low**

### Software client
The hardware device does not require any external clients to generate QR codes for the transaction data. The transaction can be broadcast on the device by connecting it to a paired phone using this [app](https://play.google.com/store/apps/details?id=com.archos.safet.bridge&hl=en_US&gl=US).

Another client is an update tool, which allows users to update the device's firmware called Safe-T Touch Updater, a complete tool with firmware blob included with each software version of the updater. The tool is, unfortunately, Windows-only. The tool can be located on this [page](https://www.archos.com/fr/products/crypto/archos_safettouch/index.html?rprod=1)

It's unknown whether the device supports generation of QR codes for sending signed transaction data.

### Optional features
The device may work independently from the host device.
QR Code reader for reading transaction invoices.

### Security
The device has a fingerprint reader built-in and allows the user to use it for unlocking the device. In addition the user can opt instead for PIN code authentication. Whether the user can enable only one of them or even both at the same time is unknown.

### Physical security
The packaging is sealed by holographic seals on the opening seams of the box. The box cannot be opened without tampering with the seals.

### Privacy
The device is an independent black box if used via Bluetooth, use at your risk.

It is unknown how the device operates 

## Non-hardware related

### Manual
Manual is very simplistic and only aims user into the setup of the device. The rest is needed to be figured out on your own.

### Support
The support is according to Amazon.com reviews in French and the staff is not trained to help with general information about the device. The device is possibly abandonware.

## Upgradability
The device is no longer updated for more than a year, the latest firmware is 1.2.5, the device can be upgraded using their AIO tool called Safe-T Touch Updater, which includes the firmware blobs with each software release. 
