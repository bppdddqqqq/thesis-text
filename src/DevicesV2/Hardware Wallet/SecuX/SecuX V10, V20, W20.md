
---
source: https://shop.archos.com/fr/hardware-wallets/588-archos-safe-t-mini-0690590037069.html
---


# SecuX V10,V20,W20 Line
Is a range of devices manufactured by a "TODO" company. The line consists of 3 devices, which vary in form factor and feature-sets. All of the devices seem to use the same Secure Element, so-called [[InfoKeyVault S97 Omni]]. The range of devices suffer from informational blackout, with various source codes pulled and removed after a critical video review on Youtube, regarding the device's security.
## At a glance

### Transparency
The hardware of the device is to greather relevance unknown and aside from public FCC Filings for V20/W20, it wouldn't be known much about it's hardware.

FCC Filings:
- https://fccid.io/2ASNW-SX001

The FCC filing partially redacts some information, like the BOM and schematics, but according to the FCC specifications, they cannot redact/hide inside photographies of the hardware. Which is publicly available and allows the user to know the hardware. V20/W20 runs on the [[Nordic Semiconductors nRF52840 SOC]] and seems to contain a rather propriatary [InfoKeyVault S97 Omni](InfoKeyVault%20S97%20Omni) security element.

The hardware can be confirmed on the vendor's press statements. 

- [The SecuX V20 wallet employs nRF52840 SoC to provide secure wireless connectivity for crypto asset transaction via host smartphone, tablet, or PC - nordicsemi.com](https://www.nordicsemi.com/News/2019/04/SecuX-V20-wallet-use-nRF52840-to-provide-secure-wireless-connectivity-for-crypto-asset-transaction)
- add slides about Omni S97

The information about [Nordic Semiconductors nRF52840 SOC](Nordic%20Semiconductors%20nRF52840%20SOC) are public and user can easily find documentation, source codes, etc. This is not the case of Omni S97. The chip is a black box with no publicly available details. After further inquiries with the vendor, there is a requirement of an NDA. This chip is not officially advertised as Omni by the manufacturers, rather as [Infineon SLE78 SE](../../../Hardware%20Chips/SE/Infineon%20SLE78%20SE.md) line of secure element chips.  

The SOC had been publicly exploited - https://vuldb.com/?id.175464
The SE has no public records of exploits, it's probably that the vendor demands an NDA for any vulnerability disclosures.

There are some source codes available on SecuX's public github account.
- [GitHub - secuxtech/SecuXMCU: SecuX device firmware](https://github.com/secuxtech/SecuXMCU) - the firmware files seem to be incomplete, lacking whole parts of the source code, imports to certain libraries, there are no guides on how to compile the firmware and it fully redacts all code regarding crypto and secure element communication. The firmware is not reproducible

There was an incident which caused SecuX to suddenly rebase/censor repositories or outright withdraw them from public access. Allegedly it's caused by an author of this Youtube video https://www.youtube.com/watch?v=Az5-pboXnaQ which showcased an exploit where the adversary can exploit the device to show arbitrary messaging, which may cause confusion to inexperienced or non-techsavvy users. The exploit used a modified host library for communicating with the device. Which was formerly available on npm and github. After the video, the npm repo points to an empty package with no binary blobs and github repo contains nothing and is fully redacted from all commits. It was attempted to contact the author of the video if he has backed up data to the relevant SecuX info, and he did.

### Software client
The device requires usage of SecuX's own clients //todo: add names ;; the clients utilise a library called SecuXConnect, which builds the necessary USB/Bluetooth interface for communication with the device and also necessary update of the device details. The client enhances the on-device experience by providing balance info straight to the hardware wallet. This had been exploited in the aforementioned youtube video,  

### Optional features
The optional feature are the editions. There are virtually no differences between V20/W20 on the software or chip level, aside from different form factor and existence of USB-C port on W20, compared to MicroUSB on V20.

V20/W20 contains a faster SOC, but support same amount of currencies as V10, plus V20/W20 have a battery and bluetooth radios, to allow linking with phone devices.

### Security
PIN entry

### Physical security
V10/V20 use the same device casing. Which is easily openable with regular prying tools.

W20 has casing glued shut with harder access for prying tools.

The packaging uses hollographic seals to guarantee integrity of the devices from the place of manufacturing.

## Non-hardware related

### Privacy

### Manual

### Upgradability
