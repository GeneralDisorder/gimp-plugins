#!/usr/bin/env python

# GIMP Python plug-in that combines a few filters for a faux-sepia-photo effect.

from gimpfu import *
import gimpcolor
import math

def do_stuff(img, layer, copy=1, border=20.0, opsepia=1, colorize=1, colorize_hue=36.396, colorize_sat=24.7, colorize_lig=3.1, tilt=0, dropshadow=1) :
    gimp.progress_init("Doing stuff to " + layer.name + "...")
    
    # Clamp some values
    border=min(max(border, 0.0),1000.0)
    colorize_hue=min(max(colorize_hue, 0.0), 360.0)
    colorize_sat=min(max(colorize_sat, 0.0), 100.0)
    colorize_lig=min(max(colorize_lig, -100.0), 100.0)
    
    # Work on new image if specified
    if copy:
        img=pdb.gimp_image_duplicate(img)
    
    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(img)

    # Do stuff here.
    layer = pdb.gimp_image_merge_visible_layers(img, 0)
    pdb.script_fu_old_photo(img,layer,1,border,opsepia,1,0)
    layer = img.active_layer
    if colorize:
        pdb.gimp_colorize(layer, colorize_hue, colorize_sat, colorize_lig)
    pdb.gimp_image_resize(img, img.width*2, img.height*2, img.width/2, img.height/2)
    if tilt != 0:
        item = pdb.gimp_item_transform_rotate(layer, math.radians(tilt), 1, 0, 0)
    if dropshadow:
        pdb.script_fu_drop_shadow(img, layer, 20, 20, 20, gimpcolor.RGB(0,0,0), 50.0, 0)
    layer = pdb.gimp_image_merge_visible_layers(img, 0)
    pdb.gimp_image_resize_to_layers(img)
    
    if copy:
        display=pdb.gimp_display_new(img)
    
    pdb.gimp_displays_flush()
    
    # Close the undo group.
    pdb.gimp_undo_push_group_end(img)

register(
    "python_fu_coc_handout",
    "CoC Handout",
    "Transform a picture into a faux-sepia-photo",
    "General Disorder",
    "General Disorder",
    "2021",
    "CoC Handoutify...",
    "*",      # Alternately use RGB, RGB*, GRAY*, INDEXED etc.
    [
        (PF_IMAGE,'image','Input image',None),
        (PF_DRAWABLE,'layer','Input layer',None),
        (PF_TOGGLE,'copy','Work on a copy?',1),
        (PF_FLOAT,'border','Border Width',20.0),
        (PF_TOGGLE,'opsepia','Old Photo Sepia?',1),
        (PF_TOGGLE,'colorize','Colorize?',1),
        (PF_FLOAT,'colorize_hue','Hue (0.0-360.0)',36.396),
        (PF_FLOAT,'colorize_sat','Saturation (0.0-100.0)',24.7),
        (PF_FLOAT,'colorize_lig','Lightness (-100.0-100.0)',3.1),
        (PF_SLIDER, 'tilt', 'How much tilt?', 0, (-45,45,1)),
        (PF_TOGGLE,'dropshadow','Drop Shadow?',1)
    ],
    [],
    do_stuff, menu="<Image>/Filters/CoC")

main()