# Trezor Core

Is Trezor's implementation of their secure firmware, this firmware generically implements it's cryptographic library. Which contains implementations of the most utilized cryptographic algorithms in the cryptocurrency space.
Another shared library is their storage library for securely storing the data located in Trezor. 

Other than that, each device maintains its own codebase with [[Trezor Model T]]'s being written mainly in Micropython with small parts of code written in C, and [[Trezor One]]'s mainly in C with parts of the code being written in Micropython or flavor of Python.

Both flavors of the firmware are maintained, receiving regular patches to the codebase fixing bugs and security issues.

## Model One's

Implemented mainly in C language, including the ui and drivers. The architecture of the firmware is monolithic.

This firmware is also utilized in an open source project called PiTrezor, which allows the user to turn a Raspberry Pi into a full Trezor device - https://www.pitrezor.com/2018/02/pitrezor-homemade-trezor-bitcoin-wallet.html

## Model T's

Implemented mainly in MicroPython, with parts of the software calling to lazily binded C libraries, either made by MicroPython and third parties, or Trezor (in case of cryptographic libraries).

The Core runs coroutine-based cooperative multitasking, i.e., there is no preemption. The tasks are run as coroutines giving each task an uncertain amount of processing time until it yields a value. The implementation of Core's event loop can be located here https://github.com/trezor/trezor-firmware/blob/master/core/src/trezor/loop.py. Aside from coroutines there are also system-level "Syscalls" which are used when tasks want to perform any I/O, or do any sort of communication with the scheduler, they do so through instances of a class derived from `Syscall` [https://github.com/trezor/trezor-firmware/blob/e4b5f10223e4a88b926354b0351b360d16c8184d/core/src/trezor/loop.py#L208]. The syscalls implemented are sleep, wait, race. 

**is this really worth discussing?**

The plainest example of the event loop usage can be located here (https://github.com/trezor/trezor-firmware/blob/master/core/src/boot.py), where the firmware on boot initiates the screen and schedules the base Bootloader coroutine and starts the event loop. Bootscreen then initiates Lockscreen and returns it, if at any point the user tries to authenticate the Trezor device, the Lockscreen gets removed from the event loop and switches to Verify User Pin view, and awaits the result, if await succeeds it initiates the storage and removes itself from the event loop. If at any point the Bootloader loop catches PinCancelled exception, it silently catches it and again loads up the Lockscreen, if at any point catches BaseException, it equals to a kernel panic of the firmware and halts the entire MicroPython. 

**end of blabber**

