# Ledger Nano S
Versatile hardware wallet device created by a french company Ledger. Company is at competition with Trezor company, by releasing their device shortly after the release of [[Trezor Model One]].

## At a glance

### Transparency

The device has a specific architecture, where MCU is handling all UX and communication with the outside world and SE which is connected via serial connection to the MCU and handles cryptographical operations with the MCU, holds private key handling key derivation of the relevant wallets and also holds unique signature by Ledger which ensures genuinity of the SE chip.

The MCU is made to be an untrusted environment, requiring for the chip to be verified by the SE on bootup. Verification is done by copying the memory regions of the bootloader and firmware to the SE and SE validating that the underlying code is untampered by comparing the resulting hash. SE is only capable of requesting said data and not having direct access to it, this could pose a problem if the bootloader/firmware can fit extra data into their memory regions and modifying copy function to omit modified regions.

This had been exploited and publicly disclosed by a hacker Saleem Rashid, where he presented the exploit by forcefully setting recovery seed to a preset. The exploit was attempted to be disclosed by Rashid to Ledger but it had been denied and determined to be implausible. There was also a level of evasiveness by the Ledger CTO and other staff members. Eventually the firmware update had been released by Ledger to mitigate this issue. The bug fix haven't been uploaded to their premium device [[Ledger Blue]] (per the blog post written on Mar 20, 2018)

- source: https://saleemrashid.com/2018/03/20/breaking-ledger-security-model/

The main OS of the device called BOLOS is closed-source. BOLOS is according to the public info an operatingsystem which handles secure communication between the various "apps" of the Ledger ecosystem and syscalls offered by BOLOS. BOLOS facilitates the cryptographical seeds for generation of transactions. Apps are fully sandboxed from accessing other apps/resources unless defined by BOLOS.

- source: https://www.ledger.com/secure-hardware-and-open-source

An open-source implementation of BOLOS caled BOLOS Tee can be found on their GitHub repository. And is meant for usage on Samsung devices supporting propriatary "Secure UI" feature. The repository is seemingly abandonned.

- source: https://github.com/LedgerHQ/bolos-tee 

Various parts of the firmware are open-source, that includes firmware for the MCU and UI. Firmware for the MCU is shared with Ledger Blue, last update to the repo had been done on Aug 4, 2017. Nano S' latest firmware had been released on March 2, 2022. Thus the repo haven't been updated for the MCU portion of the firmware. Similarly it can be said about the Nano UI repo, which had ceased updating on Mar 10, 2017.

- source:  https://github.com/LedgerHQ/nanos-nonsecure-firmware
- source on update: https://support.ledger.com/hc/en-us/articles/360002731113-Update-Ledger-Nano-S-firmware
- source on nano ui: https://github.com/LedgerHQ/nanos-ui

There had been a rewrite of Nano UI to Rust. Whether it's used is unknown

- source: https://github.com/LedgerHQ/ledger-nanos-ui

Speculation: The timing of abandoning the support for repositories may correlate with the Rashid article. The version at the time of Rashid's article was 1.3.1 released on 28 February 2017, new firmware 1.4.1 was released on 6 March 2018. Few months after the last commit and disclosure of the exploit.

There is a public SDK for development of Ledger "Apps", which handle signing of transactions and sending relevant payloads to SE for signature. Approval of transaction is handled by the MCU, SE has no way of knowing whether consent had been given by the user or by malicious party. The relevant wallets are derived from the main seed stored on the SE, thus reinstalling apps won't pose risk of having the assets lost.

source: https://www.ledger.com/academy/hardwarewallet/what-are-ledger-applications-and-why-do-i-need-them

Nano S has a small memory for storing the apps, requiring frequent installation/uninstallation of apps to free up space for other cryptos. Apps need to be executed to access it's relevant functions.

### Software client

Nano S requires Ledger Live, which handles firmware and app updates, installation of apps and also facilitates some optional features, like U2F and Password manager.

The client is open-source and relevant githubs for desktop and mobile can be found here
* https://github.com/LedgerHQ/ledger-live-mobile - mobile frontend
* https://github.com/LedgerHQ/ledger-live-desktop - desktop frontend
* https://github.com/LedgerHQ/ledger-live-common - shared backend for mobile and desktop, makes up complete business logic of the software

### Optional features

- password manager
- u2f

### Security

4-8 digit pin code with randomized input, the pin is inputted on-device. The device have had achieved EAL5+ level certification ( https://www.ledger.com/academy/security/the-importance-of-certification ) and Ledger has it's own dedicated penetration teams called Doujon, which aside from security testing their own devices, they also dedicate their time researching other hardware wallets for security vulnerabilities.

source: https://blog.ledger.com/Introducing-Ledger-Donjon/

Ledger also maintains a bug bounty program with 90-day disclosure policy. Bounties are paid in bitcoins with necessity of fullfilling several conditions like minimal age, not being from imbued with trade sanctions, etc.

source: https://blog.ledger.com/bounty/

### Physical security

The vendor doesn't use any protective features on the device and packaging itself, instead relying on cryptographical keys attesting genuity of the device. On initialization the device necessitates to fullfill a security checklist which also includes validating the cryptographical keys embedded in the device with Ledger servers. If the keys are valid, the device passes genuinity tests and may continue operating. (lacking citation for verity of claims, does the device stop operating if it's not genuine?)

### Privacy

The device has open-source client and is HWI-compliant. The device relies on a software wallet to do it's work, reducing confidentiality of the funds associated with the device.

## Non-hardware related

### Manual
Device has a publicly accessible PDF-version of their manual. Which very broadly and extensively describes all the functions of the Ledger.

source: https://support.ledger.com/hc/en-us/articles/360007061974-User-Manual?docs=true

### Support

They have a support link located [here](https://support.ledger.com/hc/en-us/categories/4404369571601?support=true). They offer support primarily via support tickets.

### Upgradability

The device has a very small amount of memory allowing the user to only install a small amount of apps (up to 6). The device is frequently updated with security and feature patches by Ledger. Due to the generalized nature of the device, the device is not limited by it's hardware specs, rather specifically by the memory storage only.

This is also supported by the availability of the SDK, that allows the user to create custom implementations of many popular or less supported cryptocurrencies. Apps still need to be installed via Ledger Live, even if the app's functions won't be available via Ledger Live but by something else.
