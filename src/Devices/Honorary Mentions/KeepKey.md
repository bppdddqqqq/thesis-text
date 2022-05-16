# KeepKey
KeepKey is a crypto hardware wallet released in 2015. a notable feature is the ShapeShift exchange integration and compared to Trezor’s and Ledger’s top models, a significantly lower price.
## Security Review
The packaging provides security seals, which makes a supply chain attack harder, but not impossible. KeepKey is based on STM32F205 MCU, the same
chip as Trezor uses in their Trezor One model. The firmware of the wallet is fully open source.
When we take a look at KeepKey’s GitHub repository, we can notice forked-off Trezor repositories and the actual KeepKey repositories sharing
similatiries with Trezor. Based on this simple observation, we can expect the KeepKey to be prone to the same or similar vulnerabilities.
Back to the hardware design, the KeepKey wallet features a considerably larger OLED display and only one button to confirm the transactions. I was not able to verify if it is actually possible to deny a confirmation or the only way to do it is to plug off the device from the USB.
During the initialization the mnemonic sentence words are shown on the display and given its size, it is much easier for cameras or someone else to look over your shoulder and see the words. The PIN is entered in the same fashion as on Trezor One. a user is shown a blind matrix on his computer display and the real matrix with numbers on the KeepKey device, they enter the pin by
clicking on the right positions of the matrix on the blind matrix. Again, given its size, over the shoulder attacks are much easier than on devices with smaller displays.
The selling point of the KeepKey wallet is the Shapeshift exchange integration which allows you to swap between different crypto assets easily. Shapeshift is a centralized service that can track your funds and identify you for one reason. Every user of Shapeshift who decides to buy or sell any cryptocurrency using this platform must undergo a classic KYC/AML process (Know Your Customer / Anti-Money Laundering) giving a third party information, such a name, a date of birth, an address, a government-issued ID and linking the wallet addresses you use to your identity.
## Existing Attacks
KeepKey is susceptible to the supply chain attack described in Subsection 5.1.1, “Supply Chain Attacks”, and the voltage glitching fault attack described in Subsection 5.1.2, Fault Injection Attacks. As of April 14, 2020, there are no other publicly known attacks possible if
running the latest device firmware26 (Release v6.4.0).