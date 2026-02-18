# 4. Embedded Programming

![](../images/week04/w04-001.jpg){width="100%"}

<aside>
💡 Group assignment:

- demonstrate and compare the toolchains and development workflows for available embedded architectures
</aside>

---

# About this week

> *Briefly describe the goal of the assignment. What are you characterizing, testing, or exploring*
> 

**Ger:** The aim is to test a workflow to program an ESP32-C3 board using the Arduino IDE.

**Shaaz:**

---

# Tools and materials used

## Equipment

* **Seeed Studio Xiao ESP32-C3 board** (Ger) and **Seeed Studio Xiao RP2040 board** (Shaaz)
* Laptop
* USB Adapter and Cable
* Electronics for demo (LED, 330 ohm Resistor, Breadboard, Jumpers)
* Multimeter (*just in case!*)

## Software

* Arduino IDE and Arduino-CLI
* Terminal
* Other editors (Nano and Zed)

---

# Process and methodology

> Describe step-by-step what the group did. Include sketches, screenshots, or videos if possible.
> 

1. Install **Arduino IDE**.
2. Try install **ESP32 Board**... first install **Board Package Repository**.
3. Fails on Timeout...(See [Fix 2](#fix-2-extend-board-manager-timeout))
  1. Install `Arduino-CLI`,
  2. Edit YAML preferences,
  3. Retry install **Board Package Repository**.
4. Install Board Package, and select port and Board (**XIAO_ESP32C3** in this case)
5. Use sample code from Wiki (changed GPIO)

---

# Group conclusions

> **Findings:** [What did you learn from the process?]
> 

Learned about electronics and code. Used the Datasheet to learn the capabilities of the board, in particular, the functions of GPIO's on the board. The SoC board is a breakout of the functionality of the chips (ESP32 and RP2040). The board adds UART, voltage regulation, Analog-to-Digital conversion and digital inputs, and makes it very compatible for new users, and allows new users to use with breadboards and a number of other compatible shields (Grove and other expansion boards on the Seeed Studio website).

Types of Pins:
* Digital
* Analogue
* PWM
* RXTX
* POWER (eg VCC, 3v3, GND and AREF)
* I2C, SPI, JTAG. Protocols for addressing peripherals, sensors, 

> **Challenges:** [What issues did you encounter?]

1. The boards library didn't load as expected.
2. Breadboard problems. Connections won't survive to much movement. Connections are unreliable, fail in way that is not visibly evident, which may interrupt more complex connections.

> **Solutions:** [How did you solve them?]
> 

1. Extended the IDE timeout to allow board manager to download from the host.

---

# Files

See below link to to files created this week:

* [sketch_ger_feb17a.ino](../../files/week04/sketch_ger_feb17a.ino)
* [sketch_ger_feb18a_sequence.ino](../../files/week04/sketch_ger_feb18a_sequence.ino)
