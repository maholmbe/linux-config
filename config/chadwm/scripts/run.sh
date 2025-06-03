#!/bin/sh

xrdb merge ~/.Xresources
xbacklight -set 10 &
#feh --bg-fill ~/Pictures/wall/gruv.png &
xset r rate 200 50 &
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

dash ~/.config/chadwm/scripts/bar.sh &
while type chadwm >/dev/null; do chadwm && continue || break; done
