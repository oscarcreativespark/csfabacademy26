# 5. 3D Scanning and Printing

![](../images/week05/w05-001.jpg){width="100%"}

<aside>
💡 Group assignment:

-  test the design rules for your 3D printer(s)
</aside>

---

# About this week

> *Briefly describe the goal of the assignment. What are you characterizing, testing, or exploring*
> 

Ger:

1. Testing print-in-place parts, with various tests for axial strength tests etc., on the UltiMaker S5.
2. Testing properties of large-format 3d-printing.

**1.:** Printed-in-Place part was Acrylic insterted during a printer pause. Tested "Squiggle" bending, stretching and torsion; Print in place handles, and, for comparison, all-PLA part.

**2.:** Using the [Ginger G1](https://www.gingeradditive.com/products/g1-printer?variant=55840562446684) pellet printer, with a nozzle size of 3.0mm. Did the Overhang Angle Test and the Bridging Test.

Shaaz:

---

# Tools and materials used

> *List all the machines, software and materials used in this assigment.*
> 

### Ger: Tools and Materials
* Laptop, 
    * Rhino, Grasshopper, [Ginger Slicer](https://www.gingeradditive.com/pages/downloads)
    * USB to transfer
* UltiMaker S5
    * FormFutura PLA (2.85mm)
* Ginger G1 system
    * rPLA Pellets
* Measuring devices

---

# Process and methodology

> Describe step-by-step what the group did. Include sketches, screenshots, or videos if possible.
> 

### Ger:

* Drew in Rhino3D, and went from Rhino to DXF for laser cutter part.
    * Tolerance (height) was too low. Measured acrylic thickness was 3.1mm, and layer-height of 0.15mm. Increased by one layer. Caused "Filament-Stuck" error when too low.
    * Rewrote to Grasshopper to test series of dimensions. And re-wrote for all PLA part.
* Printed the 3DHubs on the G1. Scaled x2.4.
* Observed top surface issues on other models. Due to the size, top surfaces drag between infill gaps.
    * Wrote a grasshopper script to test bridges without volumes (series of wall contours)

---

# Group conclusions

> **Findings:** [What did you learn from the process?]
> 

> **Challenges:** [What issues did you encounter?]
> 

> **Solutions:** [How did you solve them?]
> 

Type here

---

# Files

> Add all files created for this group assignment
> 

See below link to to files created this week:
