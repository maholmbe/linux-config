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
#kdeconnect-indicator &
#copyq &
#system-config-printer-applet &
udiskie --tray &
solaar --window hide &
#rclone-browser &
#aw-qt &    <--ActivityWatch
qutebrowser &
syncthing &
nm-applet &
#syncthingtray &
# wal -i ~/git-repos/dotfiles/wallpapers/legion
# wal -R
