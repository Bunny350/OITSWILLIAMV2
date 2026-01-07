This folder consists of two models that must be grouped and "merged".
## Printing guide
The normal part can be printed with the current settings, but the infill modifier must have its settings changed:
* There should not be top or bottom layers, you may set them to 0 / 0mm in both top and bottom layers.
* You may add or deduct one wall layer.
* Infill density must be between 25% to 50%.

## Setup guide on slicers

### UltiMaker Cura (with workaround)
Based of [How to merge and group models in UltiMaker Cura from UltiMaker Support](https://support.makerbot.com/s/article/1667411295122)
* Drop or open the STL models into the plate.
* Select **Merge Models**.
* Lay the model down and position the model to what you want.
* Ungroup the models.
* On the *infill modifier* of the part, modify its top and bottom layers by using **Per-model settings**.
    * Open the options by clicking **Select settings**.
    * Check the **Top/Bottom Thickness**. **Infill Density** and **Infill Pattern** is optional and will depend on what you want.
    * Change the Top/Botom Thickness to 0, and if you like to change the Infill Density, you may set it to somewhere between 25% to 50%, depending on what you want.
* You may do the same for the other part.
* The part can be sliced and printed.

### PrusaSlicer, et cetera, including Bambu Studio
**You must be at least in advanced mode in order to do so.**
* Drop or open either STL or 3MF models, for PrusaSlicer and not BambuStudio, you may open the 3MF model. It must be placing both models in a single drop per folder.
* It will warn that there are multiple parts while trying to load, Choose **Yes** as these are intended so.
* 
**This section is used for PrusaSlicer users if the infill modifier is not ready, or has top / bottom layers.**

Based of [Modifier meshes from Prusa Knowledge Base](https://help.prusa3d.com/article/modifiers_1767#modifier-meshes).
* Select the infill modifier of the part through the object menu, then click the edit cogwheel next to the part name or right-click on the part name.
* It will pop up the menu, select **layers and perimeters**. You can optionally add **infill** as well.
* Change the infill modifier top and bottom layers to 0, perimeter may also be set to 0, if one of the mesh is turned into top or bottom layer.
* You can optionally change the sparse infill density of such part, you may set it somewhere between 25% to 50%, you can also change its infill pattern to something you like, such as honeycomb.

**This section is specific to BambuStudio.**

Based of [Object level parameters from Bambu Lab Wiki](https://wiki.bambulab.com/en/software/bambu-studio/how-to-set-slicing-parameters#object-level-parameters)
* After importing, toggle the process to **objects**.
* Select the mesh modifier *in the process menu*.
* In the strength section for the infill modifier, set both **top shell layers** and **bottom shell layers** to 0.
* You can optionally change the sparse infill density of such part, you may set it somewhere between 25% to 50%, you can also change its infill pattern to something you like, such as honeycomb.
