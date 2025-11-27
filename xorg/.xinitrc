#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then

  xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
  xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then

  xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
  xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/?*.sh; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile

export XDG_CURRENT_DESKTOP=dwm

setxkbmap fi       #fix for xdotool bug (corrects keyboard layout)
xset r rate 300 50 #key repeat (xset r rate delay Hz)

xbacklight -set 10 &
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
syncthing &
nm-applet &
/usr/libexec/xdg-desktop-portal-termfilechooser -r &
slstatus &

#exec qtile start
#exec dbus-run-session -- qtile start
#exec dbus-run-session -- ~/.config/chadwm/scripts/run.sh
exec dbus-run-session -- dwm
