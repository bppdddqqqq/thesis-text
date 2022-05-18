# ColdCard Mk4

```
Warning, the document is intentionally brief, to know more please refer to ColdCard - a taxonomy
```

Fourth continuation of the device. It boasts improved features and uses new firmware branch 5.x which is separate from ColdCard Mk1/2/3's 4.x

## Improvements

* USB-C connector
* Unlimited memory: no Bitcoin transaction size restrictions!
* Expanded multisig capabilities: handle bigger, more complex transactions.
* NFC-V compatible: tap to transmit all data types, including PSBTs, addresses, and XPUBs.
* Protective sliding cover shields screen and keypad when not in use.
* Two Secure Elements for even more security:
    * Many new and extensive duress PIN options (Trick PINs)
    * Two Secure Elements, two manufacturers; minimizes unknown vulnerability risks.
* USB Virtual Disk Mode: emulates a 4MB disk when connected to macOS, Windows, iPhone, etc.
* Tougher case: upgraded with new plastic and cleaner edges.
* Faster processor and substantially higher memory capacity.

Newly uses #!markdown_get('ColdCardMk4', 'mcu') SOC. Which is much more performant than Mk3.

The SEs in question are #!markdown_get('ColdCardMk4', 'secureelement')

Source: https://coldcard.com/docs/coldcard-mk4