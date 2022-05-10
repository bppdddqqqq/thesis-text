# ESP32
Open source chip designed by Espresif. Very popular in tech community as an alternative to Arduino microcontroller/microcomputer range.

# Main info
Source:
- https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/index.html
Specsheet: [[esp32_datasheet_en.pdf]]
Limitations: [[eco_and_workarounds_for_bugs_in_esp32_en.pdf]]
## Specs

| Vlastnost produktu           | Hodnota vlastnosti                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Jádro                        | [[Cadence_Tensillica_Xtensa_LX6_ds.pdf]] |
| Velikost programovací paměti | varies by SOC variant and assembly                                                                                                                                                                 |
| Šířka datové sběrnice        | 32 bit                                                                                                                                                                   |
| Maximální frekvence hodin    | 160/240 MHz                                                                                                                                                                  |
| Datová RAM                   | varies (from 320 to 400, can be extended externally)                                                                                                                                                                |
| Citlivé na vlhkost:          | Yes                                                                                                                                                                      |
|                              |                                                                                                                                                                          |

# Security
- Secure boot
- Flash encryption
- 1024-bit OTP, up to 768-bit for customers
- Cryptographic hardware acceleration:
	- AES
	- Hash (SHA-2)
	- RSA
	- ECC
	- Random Number Generator (RNG)
		
Built-in WiFi and Bluetooth, strong customizability from the side of manufacturer and also assembler. Highly programmable.
Very rich documentation.