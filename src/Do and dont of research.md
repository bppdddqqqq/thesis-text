# Do's and don'ts of research
The rules, the baseline, always keep them in check.

## Don'ts
I should strive myself from using these things or to indulge myself into researching them:
- Do not analyse sidechain attack prevention.
- Do not deeply analyse which cryptos do the wallet support.
- **KeepKey is DEAD**
- Don't focus on software-only features outside of the hardware device.

## Do's
- One thing we need to take a note of, is that cryptowallets lack major standardization. And we need to focus on things, that aren't standardized yet and are good to take a note of. Compare things among the already mapped cryptowallets.
- What's important is not only the software, but also the hardware and how it handles the secrets/encryption/signing of the described tasks. The software must be also resilient from outer forces.
- Does it have a software client? If so, for which purpose?
- Analyze elementary building blocks of the hardware, including how each cryptowallet utilizes the hardware.
	- Is it able to derive new keys? 
	- Backups? 
	- Communication? 
	- PSBT/Multisig? 
	- Taproot?
		-	https://academy.binance.com/en/articles/what-is-taproot-and-how-it-will-benefit-bitcoin
	- Support of Hardware Wallet Interface?
		- https://github.com/bitcoin-core/HWI
		- https://bitcoinops.org/en/topics/hwi/
	- Source of entropy? Sourced from chip? Sourced from outside?
	- Firmware updates of device, does it update SOC only or SE as well?
	- Authentication/authorization? How is it handled?
	- Support for secure multi-party communication.
	- Secure channel in BitBox02? - "šifrovaná komunikácia USB prevozu" - [[BitBox02]]
	- How secure the hardware is? Physically and board wise

It is necessary to establish the baseline definition of an entry. The data is scattered across many places and it's needed to show what may be needed to 

# Found

- what is CoinJoin?