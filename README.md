<p align=center>
    <a>
        <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Logo/2022/Logo-whitetext.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Logo/2022/Logo.svg">
  <img alt="OITSWILLIAMV2" src="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Logo/2022/Logo.svg">
</picture>
    </a>
</p>

Project is being constantly updated. 

# OITSWILLIAMV2

<img alt="Voron 2.4 with 150mm mod and OITSWILLIAMV2 mods" src="https://raw.githubusercontent.com/Bunny350/OITSWILLIAMV2/main/Media/Renders/5th-anniversary.png">

* Currently featured in V2.3347[^config-on-other-side]!

[View BOM](https://docs.google.com/spreadsheets/d/1hI7gKyXv_dqwRoAh5GxhNzBPyU9dn64bGJ1oHiKoa74/edit?usp=sharing)

OITSWILLIAMV2 is a Voron 2 mod project with unique features, and sometimes breakthrough or stupidly insane features you will stop regretting slowly. It is modded by Oitswilliam Pang and the [original design](https://github.com/VoronDesign/Voron-2) is by the members of Voron Design.

This project is for those who already had a normal and big Voron printer (can be from friends or relatives), with the exception of original parts and skirts.

## Goal
The goal for this mod is:
* Make it unified,
* Make it safer to use,
* And make it intuitive for years to come.

## Feature development status

| Feature  | Status |
| ------------- | ------------- |
| Exhaust Lite Generation 2 | Released |
| RealEstate Generation 2 | Released |
| Tracker mount / AirTag mount G4 | Released |
| Tracker mount / Galaxy SmartTag2 mount G2 | Released |
| Replacement / 150mm build 60mm fan mount | Released |
| Replacement / Banger speaker skirts | Released |
| Electronics mounts / Replacement skirts made specifically for SBCs | Released |
| Electronics mounts / Replacement skirts made specifically for NUC PCs (12 Pro to 15 Pro) | Early access |

## Features
This repository includes V2 150mm, which is basically Voron 2, but smaller. It includes skirts made for such printing dimensions.

### Using OITSWILLIAMV2 Mod components

When using OITSWILLIAMV2 mod components to modify the printer, you can take either one or more with:
* Sleek yet tiltable touchscreen mount called RealEstate.
    * Touch screen support after having OctoScreen / OctoDash (for OctoPrint users) or KlipperScreen (for Moonraker / lightweight WebUI users)
* Full DC input (no AC). (150mm mod only)
* Smaller version of chamber exhaust called Exhaust Lite.
* Zero limits, indefinite possibilities, through NUC.
* Installing Windows / Debian Linux SBC (single-board computer) or NUC requires replacing the display for the better experience.
* Flying colors (RGB LEDs) via Exhaust Lite.
* Webcam from the back facing at the build plate.
* Make the printer trackable through an item tracker.
* Modular vent port to exhaust hose.
* Some mods even extend to Voron Trident. See STLs Readme for explanation.

### Building from start

OITSWILLIAMV2 is a mod for shrunk-down Voron 2.4 with 150x150x130mm build area except that can be a powerhouse of magical flying colors. Other features including:
* It has a DC power input and power output.
* Will have LED bars for users who are interested in putting "flying colors" in back panel.
* Panel clips can be printed in TPU, to prevent scratching on surfaces prone to scratching.

For the repository creator, it is because he originally did not have enough space to put a proper Voron 2.4.

Check out [parts printing Markdown file](https://github.com/Bunny350/OITSWILLIAMV2/blob/For-Voron-2.4/Parts%20printing.md) on what mod parts should be printed based on your preference. It could entertain, or just be a printer.

#### Recommended BOM changes required when compared normal V2.4 with V2.4 150mm:
| Standard V2.4  | V2.4 150mm |
| ------------- | ------------- |
| Z chain - IGUS E2-15-10-028-0 Chain | X/Y chain - IGUS E2i-10-10-018-0 Chain |
| Z chain end - IGUS E2-150-10-12PZ Chain Ends | X/Y chain end - IGUS E2-100-10-12PZ Chain Ends |
| 2x SKR 1.3 | 1x BTT Octopus, FYSETC Spider or MKS Monster8 |

* Z chains should be replaced with X/Y chains due to off-distance towards left.
* Stripping 1kg of weight in such small printer requires usage of 4 Clockwork 1 motors (NEMA17 Motor 17HS08-1004S or equivalent) to replace Z axis stepper motors.

#### Recommended BOM changes required when compared normal V2.4 with the mod when build from start:
| Standard V2.4 recommended | V2.4 150mm + OITSWILLIAMV2 Mod Project |
| ------------------------- | ------------------------- |
| Coroplast panels as bottom, back and Deck panels |   Acrylic panels as bottom, back and Deck panels|
| Internal power supply | External / dedicated power supply |
| AC heated bed | 24V DC heated bed |
| AC input | 24V DC input |

## Kit promotion guidelines
If you want to sell the kits of this mod project, please call it "Voron 2.4 with OITSWILLIAMV2 Mod" or related means that mentions Voron 2 and OITSWILLIAMV2. Do not call it "Voron 2.4 enhanced version" or any other means.

## Questions
### How powerful is OITSWILLIAMV2?
It's more powerful than the average home computers, at least on V2.3347. The only thing that's behind is a computer that has RTX 2060 (desktop) / RTX 2070 Mobile GPU and / or 12th generation Intel Core i7 desktop CPU. However that normally doesn't count if the printer's XY axes motors are not running on 48V power.
### Is 150mm an official spec size of Voron 2.4?
No. There are speculative reasons on why 150mm is not the spec size.
1. The spacing of the mounts between themselves needs to be changed, which means, like for example standard size (from 250mm to 350mm) has 150mm spacing between the bed mounts, but on a 150mm Voron 2.4, the bed mount needs to be narrower. Unless you have a router or a bench that can perfectly drill corners, the bed mount holes must be moved narrower in about half in order to make sure it is easily mounted.
2. Another reason is that one of the chain needs to be changed. Instead of using the chain intended for the Z axis, XY chain is used on the Z axis.
### Can OITSWILLIAMV2 be the first printer?
No, it is made for tinkerers, although it is intended to be an do-it-anywhere or living printer. Users who are interested doing this should have a larger printer. Unless if fairytale is real, except that could never.
### Is this project suggested, built or vibe-designed by generative AI?
No, none at all, and generative AI can get out.

* Some people said with the help of 250mm spec is the best, this project may agree. Although right now most important parts (from the original and from this repo) are compatible and to be printed on a smaller printer, and then some other parts, except the bottom panel, can be printed within a 150mm print volume.

If you have built a shrunk-down or small printer first (i.e. V0, with or no mods, smaller than Spec V1 / VT, V2 or Switchwire, excluding Z height), you may need to build a bigger printer, or **ask someone or service** for your bigger projects.

For any other questions, you can visit [Oitswilliam Pang support](https://oitswilliam.com/support), where you can contact, email or join the groups for the mod packages, or [VORON Design Discord server](https://discord.gg/voron) and [VORON Forum](https://forum.vorondesign.com) on the original elements.

## Special Thanks
* Thanks to [VORON Design](https://github.com/VoronDesign) for the Voron 2 CAD model.
* The NUC mount is vaguely inspired by [NucDeck by CNCDan](https://github.com/dmcke5/NucDeck), Oitswilliam watched the video before his own research and final decision. 

[^config-on-other-side]: The configuration files for the following printers are not included in this repository, only organized, specific and cleaned-up. To get V2.3347's exact configuration files, you must be a follower of Oitswilliam Pang and then get follower-exclusive features through [this form](https://docs.google.com/forms/d/e/1FAIpQLSe9aEM7jyf0lV2PUAgOg0_tz9F7GI91byWFxUzvXsLlXambJA/viewform?usp=header). Other steps are provided from the form.
