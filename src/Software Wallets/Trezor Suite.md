# Trezor Suite
Desktop client for managing [[Trezor One]] and [[Trezor Model T]]. Also contains modules for managing cryptowallet funds and a password manager, which derives the decryption keys of passwords via the hardware devices.

Software is an Electron-based application, that means the software is developed in a way, that allows it to be cross-compatible across many operating systems and platforms with less work done on the porting of code. This is applied by offering the software as a full desktop application (for Windows, macOS, Linux) and also as a web client using USB/Crypto/Storage APIs offered by a compatible web browser.

The software is open-source and source code can be found on [GitHub ( https://github.com/trezor/trezor-suite )](https://github.com/trezor/trezor-suite) and is licensed under their own T-RSL license. This license restricts the act of redistribution of software, also as known as forking.

The software is regularly updated, with updates released on biweekly basis, adding new features and support for new crypto additions, such as adding custom [ERC20 tokens in Ethereum](https://github.com/trezor/trezor-suite/releases/tag/v21.2.2). All of the binaries are signed by the [Satoshi Labs signing key](https://trezor.io/security/satoshilabs-2021-signing-key.asc), ensuring integrity of the binaries released by the developers.

## Usage
Note: the current observations are done without a cryptowallet and are observed from Youtube videos and blog posts

The software requires a Trezor device to operate. After connecting the device, the client will (depending on the state of the device, if it's new or not) ask for firmware update. With the update done the user is now able to utilise all of the features of Trezor wallet.

The software is split into two views, the dashboard and account view. Dashboard view serves as a general overview of the device owner's portfolio and account view allows the user to manage all the wallets and send, receive or even trade funds with other users/market. Trading of crypto's is offered by a 3rd party service called Invity. 

Most of the operations require a physical approval from the Trezor wallet, without the approval the software refuses (and isn't able) to do even most basic operations.

Communication with the device requires a specialized driver called Trezor Bridge, the bridge contains necessary communication interfaces to allow briding between the Trezor Wallet/Suite and the devices themselves.

## Features
Software has small QOL additions such as Discrete Mode (hides sensitive information and are only show on mouse hover), Tor Mode (connects the wallet to Tor network, to mask the traffic).