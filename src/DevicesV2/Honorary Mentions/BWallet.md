---
source: https://github.com/BWallet/bwallet-mcu
---
# BWallet (Trezor Clone)
A lesser known Trezor wallet clone, the wallet fully forked and copied the original Trezor One device. Was target of controversy among the Trezor community. https://www.reddit.com/r/Bitcoin/comments/2tyier/bwallet_review_by_trezor_developer/

## At a glance

### Transparency
The hardware device uses similar architecture to Trezor One and looks akin to [[Archos Safe-T Mini]].

![[Pasted image 20220331190911.png]]

The hardware and firmware but deviates from the original source code. According to Slush, a Satoshi Labs employee and Trezor develop, there were severe discrepancies found that make the device incompatible with the original Trezor Firmware and Tools. These discrepancies were not only code-wise but also on hardware-wise level, which makes the device difficult to use with more up-to-date tools. 

// source: https://www.reddit.com/r/Bitcoin/comments/2tyier/bwallet_review_by_trezor_developer/

The repos in question completely clone the Trezor codebase, and are manually adding new improvements and their own optimizations. The forks do respect GPL-3.0 licensing set by Trezor, but the licensing had been upgraded to LGPL-3.0. This license is compatible with GPL-3.0.

https://github.com/BWallet/
https://github.com/BWallet/bwallet-mcu
https://github.com/BWallet/bwallet-crypto
https://github.com/BWallet/bwallet-mcu
https://github.com/BWallet/bwallet-server
https://github.com/BWallet/bwallet-common
https://github.com/BWallet/bwallet-qrenc
https://github.com/BWallet/bwallet-tools

The cloning prompted Trezor to drastically change their licensing of the device/firmware to Microsoft Reference License, which received a severe backlash from the community. They've reverted this decision shortly after.

Source: https://www.reddit.com/r/Bitcoin/comments/2u1wea/trezor_code_no_longer_lgplv3_but_now_more/
Source: https://news.ycombinator.com/item?id=8966347
Source: http://digitalmoneytimes.com/satoshilabs-changes-trezor-software-open-source-license-reverts-again-after-community-feedback/

### Software client
The device uses a modified Trezor client, which is incompatible with Trezor devices and also uses a modified communication protocol which makes the usage of the software device difficult with other software clients. Also the client has embedded supercookie tracking, which queries for HWIDs on the host device.

### Optional features

### Security
The device has same security options as [[Trezor One]]

### Physical security
N/A

### Privacy
The developers seems to have attempted to do very intrusive modifications to the firmware and architecture of the device. Sharing of HWIDs on host devices is a severe intrusion in privacy.

## Non-hardware related

### Manual
N/A

### Support
The device is abandonned.

## Upgradability
The device is abandonned. Before abandonning the device had been upgraded inline with Trezor, with a small delay of a couple of days. The modifications were done by copypasting the code and not via proper merging of the mainline branch.