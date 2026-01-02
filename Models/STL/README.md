This folder stores STLS of this project.
## Compatibility
Some of this mod supports both Voron Trident and Voron 2.4. However, this project is intended for Voron 2.4 with a modded spec.
| Mod name                  | Folder location | Voron Trident | Voron 2.4 |
| ------------------------- | --------------- | ------------- | ----------|
| Exhaust Lite Generation 2 | Exhaust Lite | :heavy_check_mark: Fully supported |  :heavy_check_mark: Fully supported |
| ELG2 LED back | Exhaust Lite/LED Back | 150mm mod spec specific | 150mm mod spec specific |
| RealEstate Generation 2 | RealEstate | :heavy_check_mark: Fully supported | :heavy_check_mark: Fully supported |
| Tracker mount | Tracker mount | :heavy_check_mark: Fully supported[^daretodeploy] | :heavy_check_mark: Fully supported[^daretodeploy] |
| Deck mounting brackets[^notea] | Replacement | :heavy_check_mark: Fully supported | :heavy_check_mark: Fully supported |
| Front side of 150mm mod skirt[^noteb] | Replacement/Skirt | :x: Not supported | 150mm mod spec only |
| Fan mounting skirt for 150mm mod[^notec] | Replacement | 150mm mod spec specific | 150mm mod spec specific |
| Bottom panel of the printer | Replacement/Bottom panel | 150mm mod spec specific | 150mm mod spec specific |
| 150mm mod SBC-specific skirt | Electronics mounts/Computer mounting/SBC | :x: Not supported | 150mm mod spec specific |
| 150mm mod NUC-specific skirt (early access) | Electronics mounts/Computer mounting/NUC | :x: Not supported | 150mm mod spec specific |
| Condensed 60mm fan grill | Replacement | :heavy_check_mark: Fully supported |  :heavy_check_mark: Fully supported |

[^notea]: The part in question is called *din-rail-bypass-deck-mount-X4.stl*. These (being four of these parts) are used to mount the deck panel without the DIN rail being mounted with. It can be mounted with M3x8mm to M3x10mm BHCS / SHCS. This part is located in Replacements folder.
[^noteb]: This includes the following part names: *front-skirt-150mm-mod-left.stl* and *front-skirt-150mm-mod-right.stl*.
[^notec]: This part mounts one 60mm fan or some accessories into the printer. It uses the same mounting screws as the original. There are two variants for attaching the mount into the frame, *[base]150mm-60mm-fan-mount-m3x8.stl* which uses M3x8mm SHCS, but it seemed way too weak, so there is another variant called *[base]150mm-60mm-fan-mount-m3x12.stl* which requires M3x12mm SHCS on mounting to the frame.

* Most mods for Voron 2.4 do support Voron Trident, but needs user testing.
* Most mods for Voron 2.4 does not support Voron 0, Voron 1.8, Voron Legacy or Voron Switchwire.

### <div id="nuc">NUC Mini PCs and SBCs</div>

OITSWILLIAMV2 mod now uses ASUS / Intel NUC PC which is inserted onto the back of the printer's skirt. This part only supports V2 in 150mm build size (mod). It used to support Morefine M6 with two mounting options (DIN rail mount or adhesive on the bottom) and universal (variant doesn't matter), but because of it's bad performance and compatibility, we have decided to discontinue them. OITSWILLIAMV2 also contains 150mm (mod) skirts that are made specifically for single-board computers such as Raspberry Pi, et cetera.
* For users who still want or repair mounts for Morefine M6, [the last CAD commit with such model](https://github.com/Bunny350/OITSWILLIAMV2/tree/df8fa697d1fd7cfa57b1f74a1fd6d7f7c9acae59/Models/CAD/VORON2.4-150mm) and [the last commit with such printable models](https://github.com/Bunny350/OITSWILLIAMV2/tree/df8fa697d1fd7cfa57b1f74a1fd6d7f7c9acae59/Models/STL/Electronics%20mounts/NUC%20Mini%20PC/Morefine%20M6) can still be accessed.

## Color guide
* If the part name does not have any brackets at the beginning you may use the printer's base color to print the part.
* [acc] - Printer accent color.
* [opaque] - Opaque color, it should block most of the glowing elements. It can be opaque base or accent color.
* [transparent] - Transparent color, it should allow the glow to pass-through and can be diffused. Transparent PETG / PC is recommended.
    * Transparent ABS can be used but seems rare in FFF 3D printing.

##  Printing guidelines
This section tells how to basically configure print settings.
Some parts require a bigger printer to print.
### Settings
These parts require ABS, PETG or PC to print.
Settings and parameters must be set to the following values:
* Layer height 0.2mm
* Layer width of 1.6mm (for 0.4mm nozzle) or 4 layer lines (for 0.4 / 0.6mm nozzle)
* Infill density of 40%, but,
    * On LED diffusers ([transparent]led-diffuser-(direction)-100-infill), the infill density must be 100%,
* Any slicers are welcome.
* Some inner parts such as grills requires modifiers to optimize printing performance.

[^daretodeploy]: This is best when showing off people at the 3D printer-related events, to prevent losing the printer. I know about MRRF, but I couldn't visit. Maybe in the near future I may do that.
