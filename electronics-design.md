# Electronics Design

💡

Group assignment

* Use the test equipment in your lab to observe the operation of a microcontroller circuit board (as a minimum, you should demonstrate the use of a multimeter and oscilloscope)
* Document your work on the group work page and reflect what you learned on your individual page

***

### About this week <a href="#id-19caf66e-e64e-809a-a019-d031dff40495" id="id-19caf66e-e64e-809a-a019-d031dff40495"></a>

> _Briefly describe the goal of the assignment. What are you characterizing, testing, or exploring_

Learning how to use an Oscilloscope I started reviewing these two videos on YouTube.

[https://youtu.be/u4zyptPLlJI?si=OFvzzVEfxAZjMUsn](https://youtu.be/u4zyptPLlJI?si=OFvzzVEfxAZjMUsn)

and

[https://youtu.be/lSHAE\_Y6snc?si=9KTCRDw6nMqq1bSD](https://youtu.be/lSHAE_Y6snc?si=9KTCRDw6nMqq1bSD)

These are a good introduction guide to using Oscilloscopes. After watching these I switched on the Oscilloscope, calibrated the probes,

Probed some boards.

Carl: Tenma 72-2610 Multimeter

My first steps for learning to use my multi meter were looking at the manual found at

[https://www.farnell.com/datasheets/2616986.pdf?\_gl=1\*rga25o\*\_gcl\_aw\*R0NMLjE3NDA2NTAxMDYuQ2p3S0NBaUF0NEMtQmhCY0Vpd0E4S3AwQ1VkLWxTc1RmWHA2YmZtTDNMV3VVbVotY1RqN3hyTGg3M0tRNEtOaVJ0SnhIU0pHZ2J0Und4b0N2b2dRQXZEX0J3RQ](https://www.farnell.com/datasheets/2616986.pdf?_gl=1*rga25o*_gcl_aw*R0NMLjE3NDA2NTAxMDYuQ2p3S0NBaUF0NEMtQmhCY0Vpd0E4S3AwQ1VkLWxTc1RmWHA2YmZtTDNMV3VVbVotY1RqN3hyTGg3M0tRNEtOaVJ0SnhIU0pHZ2J0Und4b0N2b2dRQXZEX0J3RQ).._\_gcl\_a&#x75;_&#x4D;TEyNzIwMDQzNy4xNzQwNjQ5OTEx

***

### Tools and materials used <a href="#id-19caf66e-e64e-808c-874b-ca2e9ffbee1a" id="id-19caf66e-e64e-808c-874b-ca2e9ffbee1a"></a>

> _List all the machines, software and materials used in this assignment._

* OWON - SDS6062 Oscilloscope
* User manual for OWON SDS6062 (PDF in the Files section bottom of page)
* XIAO Board programmed with a breakout board with a sensor attached and programmed with the relevant Code.

Carl:

* Tenma 72-2610 Multimeter
* Xiao ESP32-C3

***

### Process and methodology <a href="#id-19caf66e-e64e-807d-a3b6-f9bb9e3b7b6d" id="id-19caf66e-e64e-807d-a3b6-f9bb9e3b7b6d"></a>

> Describe step-by-step what the group did. Include sketches, screenshots, or videos if possible.

Diarmuid Testing

Step by step testing the OWON SDS6062



Oscilloscopes allow you to measure a circuit's voltage over time, giving more information than a basic digital multimeter. The image below shows a typical screen we see on the oscilloscope.



The probes generally have a 1X. and 10X positions. The 10X will attenuate the reading by ten (reduce the signal strength X10) we will typically have the probes set to the 10X positions.



The image below shows the internal resisto setup for 10x and 1x positions 10x has a 9 M oam resistor and the 1X has a 1M oam resistor



The Probes have spring-mounted tips that can be removed to probe tight to reach places.



#### Probe Calibration <a href="#id-1a8af66e-e64e-802b-bbb3-df5d82e01b39" id="id-1a8af66e-e64e-802b-bbb3-df5d82e01b39"></a>

I connected the first probe to the Oscilloscope CH1 and attached the probe connectors to the probe comp or frequency generator. This produces 5v at 1kHz so we can calibrate the probes.



Note the red wave on the screen indicating ch1.



Adjusted the vertical position and volt/div knobs to get the wave in view on screen.



The probe calibration screw is at the oscilloscope connection end. This probe needed a little calibration.



I tried to save an image using the save button, inserted USB pen and pressed save. I followed the on-screen instructions to save the image. Used the default file name and presed enter using the multipurpose knob. At this point, the Oilliscope froze – tried many combinations of button presses, left It for a while - nothing worked  - went for a hard reset power off and on cycle -leave off for a few moments before powering on.

Connected the other probe to CH2 and followed the same procedure – I couldn't seem to get control of the waveform in the viewer by adjusting the vertical position and  Volts – DIV or the Horizontal Position.



Spotted the “autoscale” button, pressed it and presto –it was centred on the screen.



Again, slight adjustment needed on the probe collaboration screw.





Now time to start probing the XIAO

Need to get some programmes and code running. I will check the 3-axis digital accelerometer to try and see the info it’s sending to and from  the XIAO –

Pic\_06\_13

Push the code to the board using Arduino IDE

Carl:

Step 0:

Put in the battery!



Step 0.1:

Read the manual





Step 1:

My first test is checking the current on all the pins on my ESP32-C3



To do this i connect the red and black probes as per the instructions and start to check each pin.



I place the red on the pin and the black on ground



Second I tested voltage.



I set up the lead as per the instructions



See results on the table below.

| Pin Reference | Current  | Volts dc |
| ------------- | -------- | -------- |
| GPIO 2        | 24.35 mA | 1.5 - 0. |
| GPIO 3        | 0        | 0.013 v  |
| GPIO 4        | 0        | 0.11 v   |
| GPIO 5        | 0        | 0.12v    |
| GPIO 6        | 75.6 uA  | 3.3v     |
| GPIO 7        | 0        | 0.008v   |
| GPIO 21       | 41.75 mA | 3.3v     |
| GPIO 10       | 0        | 0.008v   |
| GPIO 9        | 405.3 uA | 3.314v   |
| GPIO 8        | 0        | 0.008v   |
| GPIO 20       | 73.6 uA  | 3.26v    |
| 5V            | 0        | 5.122 v  |
| 3.3V          | 0        | 3.317 v  |

***

### Files <a href="#id-19caf66e-e64e-8009-99ac-c7f474210fe7" id="id-19caf66e-e64e-8009-99ac-c7f474210fe7"></a>

> Add all files created for this group assignment

See below link to to files created this week:
