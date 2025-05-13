#!/bin/sh

xss-lock -- betterlockscreen -l &
autorandr -c
pipewire &
/usr/libexec/polkit-gnome-authentication-agent-1 &
numlockx on
picom -b
nitrogen --restore
dunst &
flameshot &
blueman-applet &
udiskie --tray &
solaar --window hide &
qutebrowser_container_start gmail &
syncthing &
nm-applet &
#system-config-printer-applet &
#aw-qt &    <--ActivityWatch
#rclone-browser &
#syncthingtray &
