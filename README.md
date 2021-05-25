# GIMP Plugins

This is a repository for any GIMP 2 Python-Fu plugins I decide to publish.

## Installing the plugin(s)
Download the appropriate .py file(s), and place them in the 'plug-ins' folder of your GIMP installation.

To find your plug-ins folder(s), open GIMP and navigate to Edit -> Preferences -> Folders -> Plug-ins. That page will list all folders where GIMP looks for plug-ins.
For me, on Windows, this is two folders:
```
C:\Users\<MY-USER>\AppData\Roaming\GIMP\2.10\plug-ins
<MY-GIMP-INSTALL-FOLDER>\lib\gimp\2.0\plug-ins
```
By placing the .py scripts in any of these folders, they will be automatically loaded once GIMP is restarted.

## Scripts/Plug-ins
Here follows a description of all the scripts and plugins that are part of this repository.

### CoC Handoutify
This script was designed to convert any picture into a fairly unrealistic but thematic faux-sepia-photograph, for use in my Call of Cthulhu campaigns.
Works well on photographs, both black & white and color, as well as on digital media. 

It can be found in the menu `Filters/CoC`

**WARNING:** This filter will flatten and resize your image. To protect your work, use the "Work on a copy" option.

![Handoutified picture of Winston Churchill](https://github.com/GeneralDisorder/gimp-plugins/blob/main/Churchill.png)

The settings you can change are:
* Work on a copy?
  * This toggles wether to apply the filter to this image, or if it should copy it to another image first.
* Border Width
  * This is the width of the fuzzy white border applied to the image.
* Old Photo Sepia?
  * Toggles wether to apply the Sepia effect from the Old Photo filter. This fuzzies and lightens the image a bit.
* Colorize?
  * Toggles wether to colorize the image after applying the Old Photo filter.
* Colorize Hue
  * Sets the hue of the colorization. Clamped between 0.0 and 360.0
* Colorize Saturation
  * Sets the saturation of the colorization. Clamped between 0.0 and 100.0
* Colorize Lightness
  * Sets the lightness of the colorization. Clamped between -100.0 and 100.0
* How much tilt?
  * Sets the number of degrees to tilt the image. Doesn't tilt it at all if left at 0.
* Drop Shadow?
  * Toggles the drop shadow.
