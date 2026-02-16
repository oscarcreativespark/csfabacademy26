---
description: https://academy.cba.mit.edu/classes/electronics_design/index.html
icon: gears
cover: .gitbook/assets/cnc.jpg
coverY: -16
---

# Computer Controlled Machining

> 💡 Group assignment
>
> * Complete your lab’s safety training.
> * Test runout, alignment, fixturing, speeds, feeds, materials and toolpaths for your machine.
> * Document your work to the group work page and reflect on your individual page what you learned.

## About this week

> _Briefly describe the goal of the assignment. What are you characterizing, testing, or exploring_

Carl:

***

## Tools and materials used

> _List all the machines, software and materials used in this assigment._

* Shopbot PRS Alpha
* Fusion 360
* 9mm Laser plywood

***

## Process and methodology

> When using the CNC we are following the SOP's that have been creatied by the Fablab

Safety:

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%202.jpeg" alt=""><figcaption><p>Know where your E-Stop is and when to use it</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%203.jpeg" alt=""><figcaption><p>Any time you are interacting with the spindle the interlock shoud be turned off</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%204.jpeg" alt=""><figcaption><p>Never place your hand on areas of the machine where the gantry or spindle car rides!</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%207.jpeg" alt=""><figcaption><p>See this baggy shirt...</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%209.jpeg" alt=""><figcaption><p>No allowed while operating the CNC!</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%2011.jpeg" alt=""><figcaption><p>Non-loose fitting clothes are ideal as there is nothing to get snagged in the machine.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Safety%20-%205.jpeg" alt=""><figcaption><p>Alway read the warning on the PC! This message means it's time to turn the spindle on the machine, if you ignore it your tools will break!</p></figcaption></figure>

The key aspect to opperating the CNC safley is paying attention with all your sences, with an emphasis on your ears!

Is the machine slowly getting louder or higher pitched? - The tool may be loose

Is the tools screeching? - The feed rate may be too low for the spindle speed

Is there a burning smell? STOP the machine, and deal with any hot chips

## **Machine Test:**

For our machine test we will be looking at how being aggressive effects out cuts and exaggerate flaws such as run out, by increasing tool pressure.

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%201%20(1).jpeg" alt=""><figcaption><p>First warm up your spindle, on the shopbot that is comand C5</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%202%20(1).jpeg" alt=""><figcaption><p>Secure your stock to the machine, i used wood screw in the corners, just make sure they are not near your cuts</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%203%20(1).jpeg" alt=""><figcaption><p>Check your actual thickness of your material, this will always be different from your nominal so this is critical.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%204%20(1).jpeg" alt=""><figcaption><p>Measure your stock in X</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%205%20(1).jpeg" alt=""><figcaption><p>and Y</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%206%20(1).jpeg" alt=""><figcaption><p>Us the shopbot macro C3 to home X and. Y</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2071.jpg" alt=""><figcaption><p>We have a spreadsheet that we share with members to calculate feeds and speeds</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2072.jpg" alt=""><figcaption><p>It includes some chiploads for common materials and tooling</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2073.jpg" alt=""><figcaption><p>For our test piece we offset in so that we avoid aread of the stock that have been cut</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2074.jpg" alt=""><figcaption><p>We will do 3 tests, Agressive, normal and precice.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2075.jpg" alt=""><figcaption><p>In the CAM workflow we create a setup and set our WCS in the settup menu</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2076.jpg" alt=""><figcaption><p>Now the axis match that of our machine</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2077.jpg" alt=""><figcaption><p>For our aggressive cut we are going full depth so i have reduced the chipload to 0.2, giving us a feedrate of 4800mm/min</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2078.jpg" alt=""><figcaption><p>We select a 6mm compression endmill and enter the speeds and feeds from our sheet.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2079.jpg" alt=""><figcaption><p>Out first test will be an ID pocket of 50mm, we are using the 2D Pocket Toolpath.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%20710.jpg" alt=""><figcaption><p>We then duplicate this toolpath so that we can apply our other test pieces, adjusting our values as we go.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%20711.jpg" alt=""><figcaption><p>For the precice test, i leave 0.5mm stock on the part after the pocket, this this is then removed by a 2D Contour</p></figcaption></figure>

Note: for all my roughing and finishing i rough the part in climb but i finish in conventional. I find this gives the best finish.

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%20712.jpg" alt=""><figcaption><p>Same procedure for the external of the part, only this is a 2D Contour instead of a Pocket</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%20713.jpg" alt=""><figcaption><p>All the toolpaths organised into folders</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%20714.jpg" alt=""><figcaption><p>This was an error we went back to fix, on my stock to leave we had 0.5mm axial stock to leave which meant that when the countour was run it became a loose piece.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%208%20(1).jpeg" alt=""><figcaption><p>After our programs have been posted we are back to the machine. We use C3 to zero out X and Y</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%209%20(1).jpeg" alt=""><figcaption><p>M3 moves the spindle in 3 axis, in this case it was moved to a convient location to acess it to change the tool.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2010%20(1).jpeg" alt=""><figcaption><p>We use the provided spanners to remove the tool loaded in the machine</p></figcaption></figure>

Note: Shopbot made a very good PokeYoke where the key for disengaging the spindle is conneted to the wrench. This makes it far less likely you will be removing a tool on a potentially active spindle.

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2011%20(1).jpeg" alt=""><figcaption><p>For this project we have a 6mm collet, our collet nut and a 6mm 2 flute compression endmill</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2012%20(1).jpeg" alt=""><figcaption><p>When assembled make sure to shake to confirm that the collet is seated properly in the collet nut.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2013%20(1).jpeg" alt=""><figcaption><p>First hand tighten and minimise stickout, We push the endmill into the collet as far as the start of the ground flutes.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2014%20(1).jpeg" alt=""><figcaption><p>Titghten collet nut</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2015%20(1).jpeg" alt=""><figcaption><p>Attached aligator clip for Z probe to something conductive</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2016%20(1).jpeg" alt=""><figcaption><p>Run comand C2 on the PC and make sure that the endmill makes contact with the plate twice.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2017%20(1).jpeg" alt=""><figcaption><p>Replace the dust shoe</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2019%20(1).jpeg" alt=""><figcaption><p>To confirm Z height is correct we manualy type MZ 18 into the controler to move the tip of the tool to 18mm above the workpiece</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2020%20(1).jpeg" alt=""><figcaption><p>And check with a piece of 18mm stock.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2018%20(1).jpeg" alt=""><figcaption><p>We are now safe to reengage the spindle</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2021.jpeg" alt=""><figcaption><p>We load our program from Fusion.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2022.jpeg" alt=""><figcaption><p>And make sure to hit the green start button on the machine before hitting ok on the program.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2025.jpeg" alt=""><figcaption><p>Cutting begins.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2028.jpeg" alt=""><figcaption><p>All ID tests complete</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2031.jpeg" alt=""><figcaption><p>And the machine now does the external tests</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2033.jpeg" alt=""><figcaption><p>We moved the machine to a safe location</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2034.jpeg" alt=""><figcaption><p>Disengage the spindle</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2035.jpeg" alt=""><figcaption><p>And inspect the parts</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2037%20(1).jpeg" alt=""><figcaption><p>Before removing them i note the different setting used for each part.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2038.jpeg" alt=""><figcaption><p>and then removed the tabs with a multitool</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2039.jpeg" alt=""><figcaption><p>before flushing them up with a chisel.</p></figcaption></figure>

<figure><img src="https://github.com/oscarcreativespark/Fabacademy/blob/main/.gitbook/assets/Training%20-%2040.jpeg" alt=""><figcaption><p>We now have 3 finished test pieces that we can measure and compare.</p></figcaption></figure>

| 9.5mm Ply Test      | 1 Pass      | 2 Pass      | 3 Pass                      |
| ------------------- | ----------- | ----------- | --------------------------- |
| Chipload            | 0.2mm       | 0.28mm      | 0.28mm                      |
| Feed Rate           | 4800 mm/min | 6750 mm/min | 6750 mm/min                 |
| RPM                 | 12000       | 12000       | 12000                       |
| Depth Of Cut        | 10mm        | 6mm         | 6mm                         |
| Direction of Cut    | Climb       | Climb       | Climb + Conventional Finish |
| Nominal Ext X and Y | 100mm       | 100mm       | 100mm                       |
| External X          | 100.75mm    | 100.55mm    | 100.2mm                     |
| External Y          | 100.88mm    | 100.55mm    | 100.2mm                     |
| Nominal Int X an Y  | 50mm        | 50mm        | 50mm                        |
| Internal X          | 49.65mm     | 49.7mm      | 49.9mm                      |
| Internal Y          | 49.3mm      | 49.3mm      | 49.9mm                      |
| Surface Finish      | Poor        | Poor        | Good                        |

***

## Files

> Add all files created for this group assignment

See below link to to files created this week:
