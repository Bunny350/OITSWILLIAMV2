# Tracker instructional sticker
This folder contains SVG vector and PNG raster image files of the instructional stickers on how to access the tracker's owner in case if it was marked lost.

* For the PDF version, please refer to [Models/STL/Tracker mount/TRACKER-COMMON-FOR-VORON-ready-to-print.pdf](https://github.com/Bunny350/OitswilliamV2/tree/For-Voron-2.4/Models/STL/Tracker%20mount/TRACKER-COMMON-FOR-VORON-ready-to-print.pdf).

## Requirements
* Printable sticker paper.
    * "Printable" should suggest that it is compatible with normal inkjet printer.
* PDF version recommends 4x6", and may only be used for hand-cut stickers.
### Edge cutting
* For hand-cutting, scissors or utility knife,
* For cutting machine users (i.e. Cricut cutting machines or Bambu Lab H2 series), please make sure the following conditions be meet:
    * **Set both width and height to 4cm (40mm),**
    * **Only edges be cut.**
        * PNG version is made as an attempt to make print-then-cut procedure simple, at least for Bambu Suite. If the SVG version of such sticker tries to have text or icons cut, then you may try using the PNG version.

## Contributions and modifications
* Modifications are generally done through SVG vector images. It is not recommended to modify PNG raster images and instead should be exported from SVG.
### Publishing guideline
* To publish own tracker mount instruction to this repository, an SVG file (with no raster or unoptimized vector points) is required, while the PNG in 7500DPI (11811px in both width and height) is advised in-conjunction with SVG.
#### Special instructions for PNG version
* When being exported, be sure to remove the black edge which is the cutout before exporting.
