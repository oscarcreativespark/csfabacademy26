# Mechanical and machine design

💡 Group assignment (part 1 of 2) - Mechanical design

* Design a [machine](http://machines.fabcloud.io/) that includes a mechanism + actuation + automation + application
* Build the mechanical parts and operate it manually
* Document the group project

***

💡 Group assignment (part 2 of 2) - Machine design

* Actuate and automate your machine
* Document the group project

***

### About this week <a href="#id-19caf66e-e64e-8057-8ecc-ddd585390c2c" id="id-19caf66e-e64e-8057-8ecc-ddd585390c2c"></a>

For mechanical and machine design, our group will be designing and building a roto-casting machine from upcycled 3d printer components.

Roto-Casting is a process where a mold is partially filled with a self-casting material and rotated about 2 axes so as to create a hollow part, ideally with an even wall thickness

**Ice Cream Sandwich** - got its name from the appearance of an ice cream wafer. Printed parts are the ice cream, and the laser-cut ply is the wafer - we wanted to build something that would be relatively simple to produce and programme. We also figured it would run nicely into our moulding and casting week.&#x20;

***

<figure><img src=".gitbook/assets/Main Slide.jpg" alt=""><figcaption></figcaption></figure>

{% embed url="https://fabacademy.org/2025/labs/creativespark/students/carl-mcateer/video/abomination.mp4" %}

***

### Key roles and responsibilities for the project:

* Diarmuid Kelly - Mechanical Design Lead
* Carl McAteer - Fabrication Lead
* Thom Conaty - Electronic Design Lead

While these are our areas of responsibility, there are significant areas of overlap throughout the project.

***

### Tools and materials used <a href="#id-19caf66e-e64e-8066-9139-ccc89444c8ba" id="id-19caf66e-e64e-8066-9139-ccc89444c8ba"></a>

> _Autodesk Fusion_
>
> _Onshape_
>
> _Prusa Slicer_
>
> _Arduino IDE_
>
> _Ultimaker 2 (used for parts)_
>
> _Makerbot Replicator 2 (used for parts)_

***

### Process and methodology <a href="#id-19caf66e-e64e-805f-9104-c8b7ba0a1c3f" id="id-19caf66e-e64e-805f-9104-c8b7ba0a1c3f"></a>

### **Mechanical Design (part 1 of 2)** <a href="#id-19caf66e-e64e-806f-a181-fb94fbc4acda" id="id-19caf66e-e64e-806f-a181-fb94fbc4acda"></a>

We set out to design a rotational casting/moulding machine. We started with the initial sketches we had in our notebooks and digital sketching tools.

<figure><img src="docs/img/w12/w12-1.jpeg" alt=""><figcaption><p>Some concept sketches Diarmuid's notebook.</p></figcaption></figure>

This development through sketches was where we came up with our overall structure or having 3d printed components being sandwiched between laser cut ones

<figure><img src="docs/img/w12/w12-2.jpeg" alt=""><figcaption><p>Carl doing some development sketches.</p></figcaption></figure>

Diarmuid took Carl's concept sketches and worked up an initial CAD model in Autodesk Fusion

He also took the time to set up a shared Fusion 360 workspace so that all our files for the project were in one place.

<figure><img src="docs/img/w12/w12-3.jpeg" alt=""><figcaption><p>Using Sketch as Canvase in Autodesk Fusion</p></figcaption></figure>

We used the Canvas feature in Autodesk Fusion to insert one of the selected concept sketches. This was calibrated to size so we could sketch to actual size. To do this, right-click on the canvas in the Fusion Browser and click Calibrate. Select two points of known dimension and enter the desired dimension. Your canvas will now resize.

<figure><img src="docs/img/w12/w12-4.jpeg" alt=""><figcaption><p>MakerBot Replicator 2 - disacembled</p></figcaption></figure>

Diarmuid took apart the Makerbot Replicator 2, and Carl took apart the Ultimaker 2. Both of these printers were donated machines - the replicator from South West College and the Ultimaker from Stweart Lawn from Manerhamilton Fab Lab - thank you to both for donating the printers.

<figure><img src="docs/img/w12/w12-5.jpeg" alt=""><figcaption></figcaption></figure>

We wanted to keep the design simple so as to reduce the gears and drive shafts needed. We wondered if it would be possible to bend the belt around the corner. Constrained by the belt sizes we had salvaged from the Makerbot and Ultimaker printers, we decided to pick the longest - the Replicator X-axis belt. To confirm the size, we printed a ¼ section that was using the belt to drive around the corner. This initial test piece was too small.

<figure><img src=".gitbook/assets/12_pic_01 - 4.jpeg" alt=""><figcaption><p>First Laser Cut Size Test</p></figcaption></figure>

We measured the belt a bit more accurately the second time and got something that moved. This would need to be refined and would also need a way of tensioning the belt. But we were happy to use this as a drive mechanism.

<figure><img src=".gitbook/assets/12_pic_01 - 5.jpeg" alt=""><figcaption></figcaption></figure>

<figure><img src="docs/img/w12/w12-8.jpeg" alt=""><figcaption></figcaption></figure>

Once we were happy that the dimensions of the outside ring would accommodate the belts we were using, we started to build the full CAD model for manufacture.

* Base - Carl - CNC'd bottom and laser-cut uprights taken from the Ultimaker 2 side panels
* Outer Ring - Diarmuid - This is the most complex assembly as it contains the structure that holds the inner ring, but also all the gearing and the belt tensioning system.
* Inner Ring - Carl - This is the piece that will hold the mould, so it needs to be robust and lightweight, as this is the fastest part of the product due to the 4:1 gearing.
* Electronics and programming - Thom - Our control unit would enable control of the rate and duration of the rotocaster movement via RP2040 which output controls to a stepper motor control board and OLED screen (with rotary encoder and button for menu select) which controlled the Nemo 17 stepper motor.

Think we need to add images here of the test laser cuts

We laser cut ¼ of the arm that was going to be used

The Inner ring consists of 8 identical 3d printed parts that are sandwiched between 2 MDF rings.

As all the parts are identical, they needed to be multifunctional

So they could each hold:

* 2 skateboard bearings
* 1 belt pulley from the Ultimaker to retain the drive axis
* 2 mounting points for the mould assembly

<figure><img src="docs/img/w12/w12-6.jpeg" alt=""><figcaption></figcaption></figure>

The full assembly was created in Fusion 360

<figure><img src="docs/img/w12/w12-7.jpeg" alt=""><figcaption></figcaption></figure>

And using 'insert component', it was brought into Diarmuid design, so we had a complete CAD model

<figure><img src="docs/img/w12/w12-9.jpeg" alt=""><figcaption></figcaption></figure>

And the full set was printed on Carls Bambu Lab P1S -

{% embed url="https://fabacademy.org/2025/labs/creativespark/students/carl-mcateer/video/w12-printer.mp4" %}

Where possible, we designed parts around press fits as this is a reliable assembly method with 3d printed parts, such as the skateboard bearings in these 3d printed idlers.

<figure><img src="docs/img/w12/w12-11.jpeg" alt=""><figcaption></figcaption></figure>

Full assembly for the outer ring is shown below

<figure><img src="docs/img/w12/w12-12.jpeg" alt=""><figcaption></figcaption></figure>

While Carl and Diarmud worked on the mechanical design, Thom created the electronic design for the project. Here he is desoldering power supply components from the Ultimaker main board.

<figure><img src="docs/img/w12/w12-13.jpeg" alt=""><figcaption><p>Desoldering the power circuit from the non-functional Ultimaker 2</p></figcaption></figure>

The linear rods from the Ultimaker were cut into sections using an angle grinder and used as the axles for the rotocasting machine.

<figure><img src="docs/img/w12/w12-14.jpeg" alt=""><figcaption></figcaption></figure>

The angle grinder can leave a sharp edge, so all pieces were finished on the bench grinder

<figure><img src="docs/img/w12/w12-15.jpeg" alt=""><figcaption></figcaption></figure>

This shows how we transmitted drive through the axles, the pulley from the ultimaker motion system was captured in between the 2 halves of the print and the grub screw was used to hold the axle in place.

<figure><img src="docs/img/w12/w12-16.jpeg" alt=""><figcaption></figcaption></figure>

The assembly of the outer ring

<figure><img src="docs/img/w12/w12-17.jpeg" alt=""><figcaption></figcaption></figure>

The longer linear rails from the Makerbot were used to align the printed components.

<figure><img src="docs/img/w12/w12-18.jpeg" alt=""><figcaption></figcaption></figure>

We just had to be careful not to knock them together too hard... we got some flex issues, oops...

<figure><img src="docs/img/w12/w12-19.jpeg" alt=""><figcaption></figcaption></figure>

The inner ring used the same process: a captured pulley on one end and a set of skateboard bearings on the other.

<figure><img src="docs/img/w12/w12-20.jpeg" alt=""><figcaption></figcaption></figure>

Giving it a spin!

<figure><img src="docs/img/w12/w12-22.jpeg" alt=""><figcaption></figcaption></figure>

The completed ring assembly with belts attached. The critical element of this is the 4:1 gearing, so each time the big ring spins once, the inner ring spins 4 times. This allows the contents of the mould to be spread evenly, assuming a relatively evenly proportioned mould.

<figure><img src="docs/img/w12/w12-23.jpeg" alt=""><figcaption></figcaption></figure>

The side panels were laser-cut from the acrylic panels of the Ultimaker

<figure><img src="docs/img/w12/w12-24.jpeg" alt=""><figcaption></figcaption></figure>

And the parts were dry-fitted together, and we checked the belt alignment and tension.

<figure><img src="docs/img/w12/w12-25.jpeg" alt=""><figcaption></figcaption></figure>

{% embed url="https://fabacademy.org/2025/labs/creativespark/students/carl-mcateer/video/w12-cnc.mp4" %}

The base was cut out of 24mm plywood, as we wanted something heavy to keep the machine from rocking in operation.&#x20;

<figure><img src="docs/img/w12/w12-26.jpeg" alt=""><figcaption></figcaption></figure>

Removing the piece from the CNC

### **Machine Design (part 2 of 2)** <a href="#id-19caf66e-e64e-802f-bbba-fe4c9e5ba9f0" id="id-19caf66e-e64e-802f-bbba-fe4c9e5ba9f0"></a>

### Electronic Control Board

#### Electronic Control Board - Idea 1: Recycled Power and Voltage Regulation Electronics&#x20;

In order to meet the design requirements of having both control of a 24v stepper motor and microcontroller let control, the opportunity to recycle the power circuit from an old Ultimaker 2, SLA 3D printer was explored.&#x20;

The parts required were identified from the schematic and (open source) board files and desoldered from the board.

![](<.gitbook/assets/Screenshot 2025-04-23 113914.jpg>)![](<.gitbook/assets/Screenshot 2025-04-15 155850.jpg>)

\[Image - Desoldering parts]

Although this presented a feasible route to a shared power system, the limitation of the available tooling bits for our mill (Roland SRM-20), it proved impossible to mill accurately enough for the QFN packaging of the 24 - 5v regulator.&#x20;

<figure><img src=".gitbook/assets/IMG_20250423_113044332.jpg" alt=""><figcaption><p>Unsuccessful Milling Tests for QFN Package</p></figcaption></figure>

#### Electronic Control Board - Idea 2: Recycled Power Input Electronics, Seperate Voltage Lines

Compromising on our inability to repurpose the shared electrical input with voltage regulation (to accomodate servo control and powering the microcontroller), we limited ourselves to recycling on the 24V power input circuit for the servo, and leveraging USB power for the RP2040. We kept the use of the OLED as well as the rotary encoder and button for system controls.

<figure><img src=".gitbook/assets/image.png" alt=""><figcaption><p>Circuit design with Separate Power Rails</p></figcaption></figure>

<figure><img src="docs/img/w12/w12-02-2.jpeg" alt=""><figcaption><p>Control board hosting RP2040, stepper motor control board, OLED and control inputs. </p></figcaption></figure>

Despite our best efforts, difficulties milling the board and the looming time constraints pushed us to revert to a final, simpler iteration of the control board design and automation functions.

#### Idea 3: Recycled RepRap servo board (Arduino) and Arduino IDE&#x20;

<figure><img src="docs/img/w12/w12-02-3.jpeg" alt=""><figcaption></figcaption></figure>

We attached the motor mount with the drive belt to check fit and tension - we decided to use a 1:4 reduction gear to reduce the load on the stepper motor - (at least we think this is what it will do).  Two issues were encountered&#x20;

* The belt was rubbing the printed motor mount.
* The mounting holes were in the wrong place - it was designed for a smaller belt with a 1:1 ratio, but when we decided to use a 4:1 reduction gear, this required a longer belt.&#x20;



<figure><img src="docs/img/w12/w12-02-5.jpeg" alt=""><figcaption></figcaption></figure>

A quick widening with the Dremel tool and we are good to go!!

<figure><img src="docs/img/w12/w12-02-4.jpeg" alt=""><figcaption></figcaption></figure>

When we were having issues with the stepper motor skipping, we decided to balance the outer ring -  using bearings and duct tape - it fixes everything!!&#x20;

<figure><img src="docs/img/w12/w12-02-6.jpeg" alt=""><figcaption></figcaption></figure>

[A4988 motor current tuning](https://ardufocus.com/howto/a4988-motor-current-tuning/)

In order to get the wheel to spin we needed to adjust the current tuning on the driver using the built in pot. We to a voltage reading from the pot to ground and adjusted until we read 0.94v

Note: This is going to generate more heat on the driver so we made sure to add a cooling fan to our design.

<figure><img src="docs/img/w12/w12-02-7.jpeg" alt=""><figcaption></figcaption></figure>

To make sure we finished on time we put the last few mission critical steps on a white board.

<figure><img src="docs/img/w12/w12-02-8.jpeg" alt=""><figcaption></figcaption></figure>

The general layout for the electrical enclosure was done in [Maker Case](https://en.makercase.com/#/)

<figure><img src="docs/img/w12/w12-02-9.jpeg" alt=""><figcaption></figcaption></figure>

Setting up the enclosure box files in Rhino and adding some additional details, such as a fan hole and cooling vents at the top. We also had to extend the size of the box. We just selected the lower nodes in Rhino and dragged them to the desired length.&#x20;

<figure><img src="docs/img/w12/w12-02-10.jpeg" alt=""><figcaption></figcaption></figure>

We added a fan to the enclosure to ensure the stepper driver would be kept cool.

<figure><img src="docs/img/w12/w12-02-11.jpeg" alt=""><figcaption></figcaption></figure>

Diarmuid is drilling the counterbore for the M3 nuts that will hold the acrylic frame to the base. Note the tape marking the depth to drill. &#x20;

<figure><img src="docs/img/w12/w12-02-12.jpeg" alt=""><figcaption></figcaption></figure>

Balancing with the extra weight - look at all the duct tape lol.... fear not, it's only temporary.

<figure><img src="docs/img/w12/w12-02-13.jpeg" alt=""><figcaption></figcaption></figure>

We used some spare parts to decide how much weight we needed to add to the other side of the wheel to balance it with the load on the stepper.

<figure><img src="docs/img/w12/w12-02-14.jpeg" alt=""><figcaption></figcaption></figure>

While we reassembled the machine, we took the opportunity to loosen the belt tension.

<figure><img src="docs/img/w12/w12-02-15.jpeg" alt=""><figcaption></figcaption></figure>

We took inspiration from how the panels were connected on the Ultimaker 2 to connect the machine to the base

<figure><img src="docs/img/w12/w12-02-16.jpeg" alt=""><figcaption></figcaption></figure>

Our final system integration jobs were to add the enclosure and the fan for the electronics.

{% embed url="https://fabacademy.org/2025/labs/creativespark/students/carl-mcateer/video/w12-video-3.mp4" %}

***

### Group conclusions <a href="#id-19caf66e-e64e-80af-bf32-f202965a9eaf" id="id-19caf66e-e64e-80af-bf32-f202965a9eaf"></a>

> **Findings:** \[What did you learn from the process?]
>
> * **There is no MKII** - we made decisions thinking that we would revised them later but due to time constraints were not realize this was a mistake. For example we should have made the rings out of plywood as it would have been stronger, the MDF was only meant to be temporary.
> * **Using each machine to its strength -** Using a mix to printing, laser cutting and CNC was a big help for this project. CNC for big heavy parts, laser cut for large simple parts and printing for complex transition parts.

> **Challenges:** \[What issues did you encounter?]
>
> * **Integrating second like parts is sometimes changeling** - we were ambitious with our up-cycled components from the ulimaker main board and in the end we had to scrap the idea as we couldn't get it to work.
> * **Autodesk Fusion** - CAD as a team was a challenge, as we were referencing multiple parts with each team member having different approaches to designing and creating components, such as internally referenced or externally referenced components and the location of the origin, top-down vs. bottom-up modeling. Additionally, referenced parts, if changed and updated, can break parts. On one occasion, all the printed parts disappeared from the model as the referenced McMaster-Carr component that was edited, this changed how it was referenced in most of the 3d printed parts. (We did figure it out, but it was a big "uh no monent)

> **Solutions:** \[How did you solve them?]
>
> * **Utilizing Available Resources** - Since the intended board was not functioning, we had to get the machine operational on the last day. We used what was available—an Arduino Mega with a RAMPS 1.4 shield. We realize that this was overkill for the requirements, but it at least allowed us to get it working. We plan to revisit this and get the intended board operationl this week.

***

### Files <a href="#id-19caf66e-e64e-8056-aa8f-ff906f2f0f5b" id="id-19caf66e-e64e-8056-aa8f-ff906f2f0f5b"></a>

> Add all files created for this group assignment

See below link to to files created this week:
