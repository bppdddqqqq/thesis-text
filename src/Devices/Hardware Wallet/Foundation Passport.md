---
source: https://foundationdevices.com/passport/details/
---
# Foundation Passport
A very atypically shaped device which reminds of old cellphones from the days of past, than a hardware cryptowallet. Made with air-gappedness in mind, it's one of the most premium wallets that a consumer can buy and use.  Powered by [[STM32H753 SOC]] and [[Microchip ATECC608A SE]] for secure enclave storage. Also it's one of the few devices that actively enforces using store-bought batteries over USB power supply or USB charging

## At a glance

### Transparency
The device's hardware, firmware and software is FOSS and freely readable on their [Github](https://github.com/Foundation-Devices/passport-firmware). Their software uses bits of software developed by [[Trezor]], for that matter their cryptographic library. The firmware during development was based on [[ColdCard - a taxonomy]] and it's predecessor's firmware, but over time they've fully transitioned to a fresh MicroPython-based firmware.

The device was a target of controversy by CoinKite's founder, @nvk.

Source: https://medium.com/coinmonks/rekt-crypto-hardware-con-artists-creep-into-bitcoin-8ad713198d3a
Source: https://archive.ph/yt0vp
Source: https://twitter.com/nvk/status/1288860345864527874

The complete schematics are publicly available in this repository https://github.com/Foundation-Devices/passport-electronics.

Personally, I perceive this as a very nice addition to the premium cryptowallet space, due to other similarly priced devices being mostly proprietary like [[BC Vault]] or partially open-source like [[Cobo Vault|Cobo Vault/Keystone]].

### Software client
There is no official software client and the device is fully compliant with ["Bitcoin Uniform Resources"](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) encoding standard, which allows it to be used by any client around if they support this standard.

The wallet officially supports Bitcoin Core, BlueWallet, BTCPay, Electrum, Sparrow, Specter and Wasabi. 

### Optional features
- User can flash a custom firmware under premise that the device will actively warn the user about non-Foundation firmware being installed.
- Duress pin
- PSBTs
### Security
The device has their security document publicly available on their [github](https://github.com/Foundation-Devices/passport-firmware/blob/main/SECURITY/SECURITY.md).

In summary, the device uses multiple security features to secure the device from tampering and direct attacks on the device. From the fact, that the device isn't officially meant to be ran from USB chargers/connection, or to multiple integrity elements in communication between SOC and SE, to how SE operates with the outside.

The device strictly disables JTAG interface and has very restrictive MPU politics on the device, restricting many parts of the memory to non-executable (AXI SRAM, SRAM1, SRAM2, SRAM3, SRAM4, ITCM, DTCM, Backup Memory). Code must be signed either by 2-to-4 signature from Foundation or user-provided PPK.

Secure enclave is used for storage only and has restricted permissions to many of it's slots.

The device also has monotonic counters for login, bootup attempts, and inserts random delays and uses keystretching.

The device also contains unique/shared private keys that are used for genuity validation of the Passport device on this [website](https://validate.foundationdevices.com/).

The SOC and SE are linked by a secret key, without this key it's not possible to communicate with SE at all.

The backups are encrypted by a unique device ID rather than by a user-set password, ensuring that the backups can be restored easily if to the same device. Backups are stored to an SD card and the default filename is also appended by a monotonic counter from the SE, ensuring that the user knows how many times the device had been backed up. 

The device also has many security features at transaction-level and bootloader-level as well.

### Physical security
Good to watch - https://www.youtube.com/watch?v=4MCwetDUJ0E
The device is packed in a delivery package which has a shipping label and a tamper-proof security seal (leaves residue color). The seal has a serial number, but it's not internally tracked. After unpacking the box, there is a consumer box hidden inside which is shrink-wrapped and sealed with another tamper-proof seal (has micro-cuts that makes it hard to unpeel).

Another thing to note is the security document, already mentioned previously - https://github.com/Foundation-Devices/passport-firmware/blob/main/SECURITY/SECURITY.md

The document states the entire assembly process for the device and also how they protect the device. Some parts of the assembly process are overseen by the employees of the Foundation to ensure that the devices are not tampered with.

### Privacy
The device relies on a software wallet to do it's work, reducing confidentiality of the funds on the device.

## Non-hardware related

### Manual
There is a public knowledge base where user can read the quick start guide and also most of the info about the device. The manual is written in a guided manner, where the user gets an explanation by clicking through the individual options/menus as if he was on the device.

### Support
They have a mail support located here at [hello@foundationdevices.com](mailto:hello@foundationdevices.com)

## Upgradability
The device has an outstandingly beefy SOC which allows it to do much more compared to other SOCs. Performance-wise, it's only weaker to [[Cobo Vault]].
The upgradability issues could stem from lack of any wireless communication hardware, which may make 
