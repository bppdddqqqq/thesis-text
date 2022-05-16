---
source: https://shop.archos.com/fr/hardware-wallets/588-archos-safe-t-mini-0690590037069.html
---

https://github.com/Coldcard/firmware/tree/master/stm32/bootloader/releases

# ColdCard
A range of cryptographical hardware wallets, are released frequently with newly added features and tweaks to the hardware. MK4 is currently on sale, which had been released just recently. Previously there were MK1, MK2, and MK3, all devices share the same form factor and firmware.

## At a glance

### Transparency
The device is open-source. MK3 and MK4 has open-sourced it's firmware and hardware, albeit MK1/MK2 only has it's firmware available. The open hard

Firmware is licensed under COPYING-CC License, aka Commons Clause License Condition, and MIT, which allows the developers to freely fork, modify and sell the firmware under the presumption that it maintains the same license. The range of the license coverage is up for discussion because /hardware directory despite being bound by the COPYING-CC is clearly stated in the readme.md file that the hardware schematics are not meant to be reproduced for a clone of the device.

The firmware is split into 2 parts. The first part is the bootloader, which is written in C with exceptions in Python and only for the compilation. The bootloader includes a Micropython kernel and implements numerous internal syscalls which bridge the hardware and software running after the bootloader. The bootloader maintains the integrity of the underlying software with strongly set public signatures which belong to CoinKite Inc., if the software is not signed by those keys, it will fail the security checks.

The second part is the primary software, this software is written in Python, with bindings calling to the bootloader's syscalls for further interaction with the hardware.

There used to be a dispute with SatoshiLabs over code ownership, because CoinKite forked Trezor-Crypto and renamed the library without adding any significant changes. This dispute had been resolved recently by changing all relevant cryptographical and hash functions with CoinKite's or other publicly licensed work. 

![[FKDqP9_XsAgvAVw.jpg]]

If inferring from Pavol Rusnak's statement, it's probable that CoinKite was compelled to open-source the firmware for the sole reason that they've previously used parts of [[Trezor Crypto]] in MK1 and MK2 firmware.

Another detail in their repo is the lack of git modules or any kind of synchronization with mainline repositories, from which they import libraries. Most significant is [[Micro-ECC]], which implements ECC functions specifically for embedded devices. 

https://github.com/kmackay/micro-ecc
https://github.com/Coldcard/firmware/tree/master/stm32/bootloader/micro-ecc

The final detail is in the COPYING-CC license, which by the legal terms is not truly an "open-source" license. Which they propagate in their recent marketing material. This statement is partially correct because the hardware and software are public for private consumption, but for commercial or other purposes there are certain and marginal restrictions, either by the code imported and forked or by the restrictions set by CoinKite Inc. on parts of their code. Previously the code was licensed under GPL-3.0, but according to @nvk (CoinKite's founder), he considered it a "mistake". Thus he was prompted to rewrite everything under current MIT+COPYING-CC license.

Source: https://twitter.com/nvk/status/1288860345864527874

MK3 is powered by [[STM32L496RGT6 SOC]] and [[Microchip ATECC608A SE]]

### Software client
The device supports HWI, it also has a remote web interface with an embedded server for browser payments in a so-called Bunker mode.  Bunker mode requires from the user to define a set of settings, which are unmodifiable during the run of the Bunker mode, and dictate which transactions or operations are allowed. 
The hardware wallet can operate in a truly air-gapped and software-agnostic way if necessary by transferring transaction data via MicroSD cards.

### Optional features

### Security
The device uses the number pad for pin entry, the PIN must be at least 6 digits long. The PIN code may either authenticate the device, log in to a so-called "duress" wallet or outright destroy the device. The device shows a challenge response after inputting the first four digits. The challenge is unique to each device and number combination, allowing the owner to identify evil maid attacks. 

The device has a considerable amount of overengineering done, to the authentication mechanisms, allowing timelocks and pinpad shuffling. Plus potential bricking of the SE.

Since the device has multiple versions, there is some difference in the security model of the device. If the user fails to input the PIN several times, the device will only exponentially increase the time delay before inputting the next PIN code. In the case of MK3 and above, the device is able to fully brick the SE, this operation is touted to be done from the SE itself.

### Physical security
The hardware device is wrapped in a specialized bag, which is tamper-proof and has a serial number printed on it. This serial number is identical to the serial number of the device itself.

There is a control LED to signify whether the firmware is valid or not according to the known signatures. The LED light initially lights red, but after the initialization, it usually lights to green. The cases where the light might go red under official circumstances are cleanly stated in the manual.

The hardware has a clear-view case for the user to easily inspect the innards of the device. The PCB contains markings that allow the user to easily identify the SE, in case of needing to destroy the SE physically, rather than in software.

## Non-hardware related

### Privacy
The device does not rely on a propriatary software wallet to do it's work. The user can either use the ColdCard as a remote signing device or as the most isolated signing device.

### Manual
The documentation is located under the link [here](#!markdown_get('ColdCardMk4','manual'))

## Upgradability
The hardware devices share a common firmware, which has varying levels of support for individual versions. MK1 and MK2 are considered as obsolete, citing small memory and weak performance of the SOC.
MK3 is still supported with regular firmware updates, despite of MK4 having been released recently.