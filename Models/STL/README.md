This folder stores STLS of this project.
## Compatibility
Some of this mod supports both Voron Trident and Voron 2.4. However, this project is intended for Voron 2.4 with a modded spec.
| Mod name  | Voron Trident | Voron 2.4 |
| ------------- | ------------- | ------------- |
| Exhaust Lite | :heavy_check_mark: Fully supported |  :heavy_check_mark: Fully supported |
| RealEstate display unit | :heavy_check_mark: Fully supported | :heavy_check_mark: Fully supported |
| Tracker mount | :heavy_check_mark: Fully supported[^daretodeploy] | :heavy_check_mark: Fully supported[^daretodeploy] |
| 150mm mod 60mm fan mount | 150mm mod spec recommended | 150mm mod spec recommended |
| 150mm mod webcam mount | 150mm mod spec only | 150mm mod spec only |
| 150mm mod skirt | :x: Not supported | 150mm mod spec recommended |
| LED back | 150mm mod spec recommended | 150mm mod spec recommended |
| Condensed fan grill | Compatible as exhaust grill or fittable with 150mm fan mount front |  Compatible as exhaust grill or fittable with 150mm fan mount front |

<div id="nuc">Mini PC / NUC Mini PCs</div>

OITSWILLIAMV2 uses PCs that can run Windows natively as a replacement of the recommended Raspberry Pi. This guide shows what Mini PCs fit into not just Voron Trident and Voron 2, but across every Voron 3D Printers Voron Design is offering.
| Mini PC / NUC | Voron Trident | Voron 2.4 | Voron 0 | Voron 1.8 | Voron Switchwire |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
| Morefine M6 | :heavy_check_mark: Fully supported[^nucspecnote] | :heavy_check_mark: Fully supported[^nucspecnote] | :heavy_check_mark: Fully supported [^adhesive] | :heavy_check_mark: Fully supported[^nucspecnote] | :heavy_check_mark: Fully supported[^nucspecnote] |


[^adhesive]: This mount to the particular printer can only be mounted via adhesive.
* Most mods for Voron 2.4 do support Voron Trident, but needs user testing.
* Most mods for Voron 2.4 does not support Voron 0, Voron 1.8, Voron Legacy or Voron Switchwire.

## Color guide
* [acc] - Printer accent color.
* [base] - Printer base color.
* [opaque] - Opaque color, it should block most of the glowing elements. It can be opaque base or accent color.
* [transparent] - Transparent color, it should allow the glow to pass-through and can be diffused. Transparent PETG is recommended.
* If the part name does not have any brackets at the beginning you can use the printer's base color or better use the least used filament to print the part. These parts are mostly hidden on the outside.

##  Printing guidelines
This section tells how to basically configure print settings.
Some parts require a bigger printer to print.
### Settings
These parts require ABS or PETG to print.
Settings and parameters must be set to the following values:
* Layer height 0.2mm
* Layer width of 1.6mm or 4 layer lines
* Infill density of 40%, but,
    * On LED diffusers ([transparent]led-diffuser-(direction)-100-infill), the infill density must be 100%,
* Any slicers are welcome.
* Some inner parts such as grills requires modifiers to optimize printing performance.

[^daretodeploy]: This is best when showing off people at the 3D printer-related events, to prevent losing the printer. I know about MRRF, but I couldn't visit. Maybe in the near future I can do that.
[^nucspecnote]: For spec printers (250 / 300 / 350), it also has VoronDesign DIN clip mount screw holes, which is printable.
