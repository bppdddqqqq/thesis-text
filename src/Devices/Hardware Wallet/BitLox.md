
---
source: https://shop.archos.com/fr/hardware-wallets/588-archos-safe-t-mini-0690590037069.html
---
# BitLox
BitLox is card-sized hardware wallet device made by a Hong Kong-based company BitLox Ltd. The hardware device is 

## At a glance

### Transparency
The hardware device on release was a blackbox.  But the developers had released the source code for the firmware, shortly after the release ( https://www.bitlox.com/pages/open-source-apps ). Aside from firmware, they've also released source code for their apps on mobile platforms and Chrome. One highly concerning thing, is that the source code had been released at once sometime between 2016 and 2017, without any further updates. Thus any updates on the firmware are undocumented and may have changed since the disclosure.

The device had been disassembled - http://www.stellaw.info/blog/2016/2/12/bitlox-first-impressions-and-teardown. The teardown showed that the device is sealed shut in epoxy resin and contains a single Atmel SAM ARM SOC, specific model number is unknown because the manufacturer had scratched off the model number of the SOC.

Firmware is available here ( https://github.com/BitLox/bitlox-firmware ). The firmware hints at the device running on Arduino platform, with bindings for necessary porting from AVR to ARM architecture (Arduino is primarily for running on AVR). There are also strings which hint at the device running on Atmel SAM3 Platform. The account seems to have forked firmware for Nordic Semiconductors nRF52840 SOC, which may mislead potential analysists from misidentifying the device.

BitLox has multiple hardware editions. Advanced, Ultimate and Extreme Privacy. All editions share the same feature-set on the software, but Ultimate has a metal case and Extreme Privacy contains a bootable umage of TAILS OS for operation of BitLox in a trusted software environment with Tor on.

The device is allegedly FCC-certified, but this certification is nowhere to be found on FCC's website (it's probable that the filings had been done, but a request for full redaction of the device had been submitted). There are no markings or options to see if the device has a relevant FCC ID. FCC certification is necessary for sale of devices with wireless ICs in the USA. 

The device ceased marketing itself shortly after the release of the device by the end of 2016. Their website blog and facebook ceased publishing new blog posts and statuses. This cannot be said of Twitter, which is still active possibly by it's founder and responds on regular basis to questions by other people.

The website was also reliant on a website under the https://bitlox.io/ domain, which sometime between 2016-2022 and changed it's purpose from hosting documents and BitLox web client into "insight - an open-source Bitcoin blockchain explorer" server. Thus causing link rot to some resources. 

Todo: check archive.org

### Software client
They have a software client called BITLOX which is available on Google Chrome as a webapp or as a phone app on Google Play store.

The app supports pairing via Bluetooth. Apps are frequently updated

todo: check whether airgappedness is possible

### Optional features
The user can optionally order special editions of hardware. Ultimate which contains titanium casing, Extreme Privacy Edition which contains embedded USB with TAILS OS installed.

### Security
The device has 3 variable levels of security. Standard, Advanced and Extreme. Each level applies different security procedures to the device, to increase the level of security. These options can be set during setup and are non-changeable without resetting the device first.
- Standard - A 12-word mnemonic is generated for the wallet, as well as a 4-8 digit PIN.
- Advanced - An 18-word mnemonic is generated and you can create your own PIN that contains up to 20 characters. In addition there are other advanced “anti-device tampering” methods, such as the AEM, or “Anti Evil Maid”.
- Expert - Creates a 24-word mnemonic recovery phrase and a PIN is required for each transaction.

It seems that the levels are presets and lack any possibility of creating a custom mixture of the presets.

The device supports generation of up to 100 "wallets" with unlimited addresses, implying that the device is capable of storing up to 100 different deterministic wallets. Out of the 100, up to 50 can be hidden by special passcode and according to the vendor, the encrypted data is undiscernable from random bytes.

### Physical security
Device case is sealed shut with epoxy. The device lacks an SE.

### Privacy
The device requires their software clients to operate. If the device is ran in trusted TAILS OS environment, there is a possibility of the device running in a full blackbox mode. Similarly if the user runs the transactions with their clients, the user has no control over the process with custom apps as well. Open-sourcing of the protocol and apps did help with increasing transparency of the entire process, but the underlying TAILS OS environment is still close-sourced

## Non-hardware related

### Manual
Manual is very verbose and of high quality. It contains all necessary instructions and steps on how to operate the wallet. A nice inclusion is list of BIP-39 phrases, for easier lookup of necessary keywords, if user had seldom written the words incorrectly.

### Support
There is a mail and web support.

### Upgradability
todo: 
