---
source: https://product.tangem.com/choose-and-buy/tangem-wallet
githubalt: https://github.com/Gimly-Blockchain/Tangem-Blockchain-NFC
---
# Tangem Wallet
Compared to other cryptowallet devices, this device's sole purpose is to offload private wallet keys to an external hardware device. It is powered by [[Samsung S3D350A SE]], most commonly used in banking industry as a credit card IC.
The manufacturer is more focused serving as a vendor of cryptowallet or even as an authority that validates authenticity of a product (Gimly collab - https://www.gimly.io/tangem). 

## At a glance

### Transparency
The software client and relevant SDKs are open-source, the hardware itself is not, which could be understandable because it only has the chip and relevant NFC ICs, but for the sake of transparency it would've been better.
Another issue that's necessary to raise is that the ICs manuals aren't trivial to look up on Samsung's official website, requiring credentials/registration to their B2B portal (as of time of writing I haven't tested how easy is it to fetch the data). 

### Software client
The device can be used on official Tangem apps, which also double as cryptowallets or on apps which had integrated Tangem's SDK to their apps for payment processing (there is promotional material on youtube for russian payment terminals integrating Tangem - https://www.youtube.com/watch?v=3ISBO1SQu1Y) or management of funds (this is the case of XUMM XRP App - https://www.youtube.com/watch?v=31fXvWEvBR8). 

### Optional features
- Other security functions: Security delays

### Security
The device can either sign anything blindly, or with a valid certificate that authenticates the host device. But the security is heavily dependent on the host device. 
There are no recovery options unless the user invests for more expensive Tangem Twin which allows the user to duplicate the stored keys onto another paired device.

Quoting:
- EAL6+ certified secure smart-card chip based on ARM SC000 core architecture and having ISO14443 Type A contactless interface.
- Support sec256k1 and ed25519 cryptographic curves.
- 2FA: allow only transactions or data validated through issuer signature.
- Other security functions: Security delays, PIN codes, CVC codes.

The device is independently audited by company called Kudelski Security
https://research.kudelskisecurity.com/2018/08/06/audit-of-tangems-smartcard-wallet-code/

The firmware is proprietary, relying on security through obscurity.

### Physical security
Device has simple packaging, no security there.

### Privacy
The device relies on software wallet to do it's work, reducing confidentiality of the funds on device.

## Non-hardware related

### Manual
Manufacturer's only official manual is located here https://shop.tangem.com/pages/faq-security-and-technical-details.  Due to the simplicity of the device, the requirement for a more precise manual is not required.

Another support links for affiliate devices:
- https://support.xumm.app/hc/en-us/articles/360020752359-XUMM-Tangem-cards-Information-FAQ-s
- [[Tangem+by+Gimly +Technical+Manual_Inc+SSI.pdf]]

### Support
The company seems to offer email and mail support, but it's not trivial to find it on the website. Another issue is that the website as of the time of writing suffers from terrible SEO, which makes it difficult to look up information about the device.

## Upgradability
The device's firmware is constant and is not subject to change. Hampering resiliency for new breaking changes. According to the marketing material the device offers support of dApps but these apps are most likely processed on host device with required signing done by the device itself.