<p align=center>
    <a>
        <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Logo-whitetext.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Logo.svg">
  <img alt="OITSWILLIAMV2" src="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Logo.svg">
</picture>
    </a>
</p>

Project to be completed. 

# OITSWILLIAMV2

  <img alt="Voron 2.4 with 150mm mod and OITSWILLIAMV2 mods" src="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/printer-render.png">

OITSWILLIAMV2 is a Voron 2 mod project with unique features, and sometimes breakthrough features. It is modded by OITSWILLIAM PANG and the [original design](https://github.com/VoronDesign/Voron-2) is by the members of Voron Design.

This project is for those who already had a normal and big Voron printer (can be from friends or relatives).

## Goal
The goal for this mod is:
* Make it unified,
* Make it safer to use.

## Feature development status

| Feature  | Status |
| ------------- | ------------- |
| Exhaust Lite / EL w/o webcam | Released |
| Exhaust Lite / EL with webcam | EA |
| Replacement / 150mm spec 60mm fan mount | Released |
| Replacement / Replacement skirts | EA |

## Unique features

### Using OITSWILLIAMV2 Mod compoments

When using OITSWILLIAMV2 Mod compoments to modify your printer, you can take with:
* Easily Replaceable screen.
    * Touch screen support after having OctoScreen / OctoDash (for OctoPrint users) or KlipperScreen (for Moonraker / lightweight WebUI users)
* Full DC input (no AC).
* Smaller version of chamber exhaust called Exhaust Lite.
* Installing Windows / Debian Linux SBC (single-board computer) or NUC requires replacing the display for the better experience.
* Flying colors (RGB LEDs).
* Webcam from the back facing to the front build plate.
* Modular vent port with hose support.
* Some mods even supports Voron Trident. See STLs Readme for explaination.

### Building from start

OITSWILLIAMV2 is a mod for shrunk-down Voron 2.4 with 150x150x130mm build area except that can be a powerhouse of magical flying colors. Other features including:
* It has a DC power input and power output.
* Will have LED bars for users who are interested in putting "flying colors" in back panel.
* Panel clips can be printed in TPU, to prevent scratching on surfaces prone to scratching.

### What is V2.4 150mm?
V2.4 150mm is an unofficially shrunk down size variant of Voron 2.4. [Chaosdrucker](https://www.youtube.com/channel/UCaoSTYmgV7NxaQGyTauBBSw) from Germany might did it first[^chaosdruckersv2.4serial][^v2.4150mmframevideo], while OITSWILLIAM may did it the fourth seralized.

For the repository creator, it is because he originally did not have enough space to put a proper Voron 2.4.

#### Recommended BOM changes required when compared normal V2.4 with V2.4 150mm:
| Standard V2.4  | V2.4 150mm |
| ------------- | ------------- |
| Z chain IGUS E2-15-10-028-0 Chain | IGUS E2i-10-10-018-0 Chain |
| Z chain end IGUS E2-150-10-12PZ Chain Ends | IGUS E2-100-10-12PZ Chain Ends |
| 2x SKR 1.3 | 1x BTT Octopus, FYSETC Spider or MKS Monster8 |

#### Recommended BOM changes required when compared normal V2.4 with the mod from start:
| Standard V2.4 recommended | OITSWILLIAMV2 Mod Project |
| ------------------------- | ------------------------- |
| Coroplast panels as bottom, back and Deck panels |   Acrylic panels as bottom, back and Deck panels|
| AC heated bed | 24V DC heated bed |
| AC input | 24V DC input |

## Kit promotion guidelines
If you want to sell the kits of this mod project, please call it with "Voron 2.4 with OITSWILLIAMV2 Mod". Do not call it "Voron 2.4 enhanced version" or any other means.

## Questions
### Is 150mm an official spec size of Voron 2.4?
No. There are reasons on why 150mm is not the spec size.
1. The spacing of the mounts between themselves needs to be changed, which means, like for example standard size (from 250mm to 350mm) has 150mm spacing between the bed mounts, but on a 150mm Voron 2.4, the bed mount needs to be narrower. Unless you have a router or a bench that can perfectly drill corners, the bed mount holes must be moved narrower in about half in order to make sure it is easily mounted.
2. Another reason is that as you see the past renders of the printer, one of the chain needs to be changed. Instead of using the chain for the Z axis, XY chain is used on the Z axis.
### Can OITSWILLIAMV2 be the first printer?
No, it is made for tinkerers, although it is intended to be an do-it-anywhere printer. Users who are interested doing this should be supposed to have a larger printer.

* Some people said with the help of 250mm spec is the best, this project agrees.

If you have built a shrunk-down printer first (i.e. V0, with or no mods, smaller than Spec V1 / VT, V2 or Switchwire, excluding Z height), you may need to build a bigger printer for your bigger projects. Most necessary parts can be fit and can be printed on the tiny build plates.

For any other questions you can join [OITSWILLIAM PANG Discord server](https://discord.gg/Cu6e9ra) for the mod packages or [VORONDesign Discord server](https://discord.gg/voron) on the original elements.

## Special Thanks
* Thanks to Razer for making back-side magical flying colors and RealEstate chin RGB possible with Razer Chroma.
* Thanks to [VORONDesign](https://github.com/VoronDesign) for the Voron 2 CAD model.

[^chaosdruckersv2.4serial]: Voron 2.4 „the Mini“ 150x150x120 Serial Request - https://www.youtube.com/watch?v=LAnUCyFEdlc
[^v2.4150mmframevideo]: Voron 2.4 - Mythos 150er - https://www.youtube.com/watch?v=uyalMGhz0xY
