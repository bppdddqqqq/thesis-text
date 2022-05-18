# BitFi Wallet

## Briefly 

The device is unique in terms of ignoring existing Bitcoin norms. The most outrageous issue is that it completely shies away from BIP-39/BIP-44 and instead uses a propriatary key derivation scheme consisting of a salt (min. 6 letters) and passphrase (min. 30 letters). BitFi released a tool that allows to derivate the necessary pub/priv keys from the scheme here https://www.btknox.org/ 
## Citing: Kozák

Bitfi Wallet is a Wi-Fi enabled crypto hardware wallet announced in June 2018 and supported by a cyber-security pioneer John McAfee, claiming to be the first unhackable, open source hardware wallet. a phrase that was later taken off their website.

### Security Review
Although the vendor claims that the wallet is fully open source. We are only given an absolutely bizarre “developer” website bitfi.dev that is against everything we know from regular open source development, such as a lack of any transparency of repository, a way to download and compile firmware, etc. Also we have nowhere to read what the actual hardware running this wallet is, because on the first look, it seems to be an Android phone.

#### Malware Suite Included
The most alarming things are the Adups FOTa suite, Baidu GPS/Wi-Fi tracker. Both of them were found actively running in the Bitfi Wallet and
communicating over the Internet to China. The Adups FOTa suite is a spyware platform that allows for the transmission of text, call, location, and app data to a server in China every 72 hours.

### Existing Attacks
The hacking community took the Bitfi Wallet by storm and by disassembling the device soon discovered that the Bitfi Wallet is powered by MEDIATEK MT6580, a system on a chip (SOC) used in inexpensive Android smartphones and without a secure element. The device is not a custom designed piece of hardware, but a stripped down low-end Android smartphone.

More can be found at Kozák