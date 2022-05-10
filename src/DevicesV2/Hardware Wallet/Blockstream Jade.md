# Blockstream Jade

Open-source hardware wallet built on ESP32 platform, popular among the Internet of Things and embedded hardware developers. Extensibly the device also takes uses of an open hardware platform.

## At a glance

### Transparency

The device is fully open-source in terms of the hardware used, firmware and even related software. This gives the device total transparency in terms of what it's doing with the funds of the user. Another distinct thing is, that the the device is more open-source than Trezor Model One or Trezor Model T, this is achieved by using MIT license for the entiriety of the device compared to much less derivative GPL license used by the Trezor counterparts.

Source: https://github.com/Blockstream/jade

The device is based on the M5Stack.

Source: https://github.com/Blockstream/Jade/blob/master/hardware/Jade_v1_schematics.pdf
Source: https://www.finyear.com/Secure-Your-Bitcoin-and-Liquid-Assets-With-the-New-Blockstream-Jade-Hardware-Wallet_a43441.html

### Software client

Blockstream operates their own client called Blockstream Green. The client fully utilizes of the integrated Liquid Network, which is one of the main selling points for the device.

The device also support HWI.

### Optional features
Supports Blockstream's own Liquid network, which is their response to Bitcoin Lightning network. Compared to BN, Liquid network is capable of working with hardware wallets, which is not possible via BN.

Source: https://www.reddit.com/r/trezor/comments/7wqjmr/_/du2qknl
### Security

Six-digit pin for authentication.

The device is fully open-source including the hardware platform. ESP32 had been subject of many attacks and is subject to voltage glitching and other physical attacks. Thus it's necessary to not fully lose the device if possible.

Source: https://www.infoq.com/news/2019/12/esp32-fatal-fury/
Source: https://limitedresults.com/2019/11/pwn-the-esp32-forever-flash-encryption-and-sec-boot-keys-extraction/

### Physical security
The packaging is protected by a holographic seal. 
### Privacy
The device doesn't need to rely on a vendor-provided software wallet to do its work, ensuring a higher level of transparency. In addition, the software is fully open allowing the user to verify the code running on the desktop client.

## Non-hardware related

### Manual
There is a full manual available [here](https://fccid.io/2AWI3BLOCKSTREAMJD1/User-Manual/User-manual-4762796).
The manual only describes the basics and features. There is also a quickstart guide included with the device that tells the user how to setup the device.
### Support
There is a support portal [here](https://help.blockstream.com/hc/en-us/categories/900000061906-Blockstream-Jade) which entails all possible troubleshooting scenarios and explains elementary questions about Bitcoin transactions and BIP passphrases as well.
### Upgradability
The device is still maintained. It can be updated via the Blockstream Green app according to this [guide](https://help.blockstream.com/hc/en-us/articles/4408030503577-How-do-I-update-Blockstream-Jade-s-firmware-via-USB-cable-).

