# Contributing OitswilliamV2
Thank you for visiting OitswilliamV2 repository! If you are thinking about contributing to this project, you may agree to the following guidelines below:

## To builders
This section below advises the end-users who will build it and read the manuals from this repository.
### Using the issues
You can file issues regarding:
* CAD / STL design errors,
* Klipper configuration file (*.cfg) errors,
* CircuitPython (*.py) errors,
* [bill-of-material](https://docs.google.com/spreadsheets/d/1hI7gKyXv_dqwRoAh5GxhNzBPyU9dn64bGJ1oHiKoa74/edit?usp=sharing) errors,
* help regarding this project, for example, unclear guide instructions.

You will create issues from blank, so please use natural language. You may not make issues where it is off-topic. Users whose have usernames other than `Bunny350`, no matter whatever, may not make *public service announcements*.

You can report issues in any other platforms as well. Please visit [Oitswilliam Pang support](https://www.oitswilliam.com/support) for the list of contacting methods and groups.

## To makers
This section below advises the people who can make compatible parts.
### Compatibility
* OitswilliamV2 mods support Voron 2 from 150mm, 250mm, 300mm, 350mm build volumes and so-on. However this repository is made primarily for it in 150mm build volume, and note that 150mm is not the official build specification.
* Some OitswilliamV2 mods extend support to Voron Trident.
* OitswilliamV2 mods will support Micron, through primarily the Plus version (the variant in 180mm build volume).
* OitswilliamV2 mods do not support other printers that are not Voron or based of Voron printers (such as Creality, Bambu Lab, UltiMaker, Lulzbot, et cetera) , unless explicitly specified.

### Media
#### Typical renders
* All renders should feature Voron 2.
#### Obscure references
* Obscure references need to be meaningful, such as, but not limited to height and design scheme, and for the design scheme, it should not be another base of Voron 2. References should be safe for minors (children and teens under 13, 14 or 16), family-friendly and needed to have a name and the franchise, so that people will research about them. All obscure references where it does not have proper meanings, or just another base of Voron 2, or what Voron 2 is based of (another 3D printer), may be rejected.

### Assembly guides
* All printable parts should have the STL part name.
* Parts where it rely on wrenches need to have the [wrench icon](https://pictogrammers.com/library/mdi/icon/wrench-outline/) and the nut size (10 or 15mm, for example).
* Avoid putting bad humors (for example, screw it tight until it breaks and then print it again).
* Vector images are generally recommended. Future OitswilliamV2 projects may prohibit raster images in assembly manuals.
    * However, all vector images needed to be optimized, with up to 5 decimal points. This is to reduce file size. This is done by Scour, often found inside Inkscape. There are other solutions provided by other software as well.
    * Raster images are not allowed inside the svg container.

### Hardware
* You may access its CAD for proper adaptation and modification. For both f3d and STEP files, if the model is not Voron 2 full model, they may not exceed 50MB uncompressed.
* If the model has parametric history, unless if it has values or parameters that can be set by other users, you may save the model with such feature first, and then change it to direct modeling, before exporting. This will slash a lot of storage occupation of such model.
#### Full assembly
The following parts which must use the original:
* Probe ([Voron Tap](https://github.com/VoronDesign/Voron-Tap))
* Tool head ([Voron Stealthburner](https://github.com/VoronDesign/Voron-Stealthburner))
* XY gantry and carriages ([Voron 2](https://github.com/VoronDesign/Voron-2))
* Z gantry ([Voron 2](https://github.com/VoronDesign/Voron-2))
* Panel clips, door attaching and door clips

The following parts which are condemned from being replaced with parts from other mods (only modified within):
* Side skirts
#### Special instructions for the banger speaker skirts
* You can create a skirt / base mount for such banger speaker units, but if it is not for Voron 2 or Trident, you may put these unit mounts onto your own repository.
#### Special instructions for NUC-specific skirts
* Tall versions of Intel / ASUS NUC Pro or similar are not supported.
#### Special instructions for the tracker mounts
* Make sure the tracker's buzzer or speaker isn't blocked. If the tracker's buzzer or speaker has signs of being blocked, such as sound quieter than before, the part needs to be adjusted.
* **Do not allow it (or them) to be an accessible tool for stalking. All of these parts are never intended to be used for unwanted tracking. They can only be used for tracking printer's place locations.**

### Software
* The currently accepted software configuration file formats are *.cfg and *.py.
#### Instructions for *.cfg file
* OitswilliamV2 Klipper Configuration file is unlike what the original do, instead of fiddling around the one and the only `printer.cfg` file, users can just either include or don't do it.
* Display configuration files needed to be separated from the printer configuration file.
#### Special instructions for *.py file
* Be noted that for *.py it must be based of Adafruit's CircuitPython, and must be placed in **Non-Klipper** folder.
* The keys can go into secondary if a secondary switching key (on RealEstate, mute switch) is pressed.
* Be noted that a macro where it executes more than one different key on-press is not allowed. This is to prevent malicious attacks.
* The code must not be encrypted.
  * Failure to follow may lead to punishment.

### Commits
* All commits need to have clear description, otherwise it can slow down your pull request.
