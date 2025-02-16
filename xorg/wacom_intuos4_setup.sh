#!/bin/sh

# More info on https://wiki.archlinux.org/title/Graphics_tablet

# Get device IDs to use
#xsetwacom list

# Map stylus to screen (can also use the argument "next")
xsetwacom set 11 MapToOutput HEAD-0

# Reduce tablet drawing area height (make aspect ratio correct)
# xsetwacom get stylus Area
# xsetwacom set stylus Area 0 0 tablet_width height
# where height is tablet_width * screen_height / screen_width

# correction for 2560x1440 display
xsetwacom set 11 Area 0 0 65024 36576
