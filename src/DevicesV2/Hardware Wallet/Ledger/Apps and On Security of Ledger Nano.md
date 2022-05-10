[[Ledger Nano S]] and [[Ledger Nano X]] runs on application-based architecture, akin to mobile devices. An OS called BOLOS is "The open native Operating System developed by Ledger. One of BOLOS’s features is to manage Apps (delete, install) after issurance on the field. This capability offering flexibility allows to enrich the Ledger Nano S/X experience.", and contains only minimal amount of code related to the operation of the device as a cryptowallet device.

To fully utilize the devices, the user must install "apps" that are downloaded from Ledger Live's store, that either enable support for relevant cryptocurrencies (Bitcoin, BCH, Ethereum app) or it's side features such as 2-FA app, U2F, Password Manager app.

BOLOS is closed-source, and its architecture can be inferred from Security Targets of the respective devices, or the developer documentation publicly available here https://developers.ledger.com/docs/nano-app/bolos-introduction/. Apps are open source and most of them are available on Ledger's GitHub.

Ledger runs apps on the SE, with MCU only serving as a supporting hardware. The difference between both devices is, that on S, the MCU is more prominent in hardware functions, driving the LCD or receiving button inputs. X instead handles these functions on the SE instead, this architectural vulnerability on S had been exhibited via the [[f00dbabe]] exploit.

Both devices utilize STElectronics' proprietary [[NESCRYPT]] coprocessor to accelerate the encryption in hardware. This means that the implementations of cryptographic algorithms used by Ledger may not available publicly and may require an NDA from STElectronics.

The apps written for Ledger devices are written in C and use C's native libraries. Ledger have also published Security Targets of their devices, which briefly detail the security and assesses possible threats to the device. Also it details on-boarding experience.

