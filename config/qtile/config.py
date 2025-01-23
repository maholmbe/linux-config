# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import EzKey as Key, EzClick as Click, EzDrag as Drag, Group, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

myTerm = "wezterm"
myBrowser = "qutebrowser"
myFileManager = "wezterm -e yazi"
myMarkdown = "wezterm -e nvim"
myMusicPlayer = "spotify"
myPDFReader = "zathura"
myTextEditor = "wezterm -e nvim"

@lazy.function
def float_to_front(qtile):
    logging.info("bring floating windows to front")
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()

keys = [
    # Qtile Controls
    Key("M-C-r", lazy.restart()),
    Key("M-C-q", lazy.shutdown()),

    # Window and Layout Controls
    Key("M-k", lazy.layout.down()),
    Key("M-j", lazy.layout.up()),
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    Key("A-<Tab>", lazy.layout.next()),
    Key("M-<Tab>", lazy.spawn("rofi -show window -icon-theme 'Papirus' -show-icons")),
    Key("M-S-k", lazy.layout.shuffle_down()),
    Key("M-S-j", lazy.layout.shuffle_up()),
    Key("M-S-h", lazy.layout.shuffle_left()),
    Key("M-S-l", lazy.layout.shuffle_right()),
    Key("M-A-k", lazy.layout.flip_down()),
    Key("M-A-j", lazy.layout.flip_up()),
    Key("M-A-h", lazy.layout.flip_left()),
    Key("M-A-l", lazy.layout.flip_right()),
    Key("M-C-k", lazy.layout.grow_down()),
    Key("M-C-j", lazy.layout.grow_up()),
    Key("M-C-h", lazy.layout.grow_left()),
    Key("M-C-l", lazy.layout.grow_right()),
    Key("M-S-n", lazy.layout.normalize()),
    Key("M-<Return>", lazy.layout.toggle_split()),
    Key("M-A-f", lazy.layout.flip()),
    Key("M-A-g", lazy.layout.grow()),
    Key("M-S-g", lazy.layout.grow_main()),
    Key("M-A-s", lazy.layout.shrink()),
    Key("M-S-s", lazy.layout.shrink_main()),
    Key("M-n", lazy.layout.normalize()),
    Key("C-A-S-<Tab>", lazy.next_layout()),
    Key("M-w", lazy.window.kill()),
    Key("M-f", lazy.window.toggle_floating()),
    Key("M-s", lazy.window.toggle_fullscreen()),
    Key("M-<period>", lazy.next_screen()),
    Key("M-<comma>", lazy.prev_screen()),
    Key("M-S-C-h", lazy.layout.swap_column_left()),
    Key("M-S-C-l", lazy.layout.swap_column_right()),

    # System Controls
    Key("<XF86AudioLowerVolume>", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+")),
    Key("<XF86AudioMute>", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),

    # Media keys
    Key("<XF86AudioPlay>",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.PlayPause"),
        desc='Audio play'
        ),
    Key("<XF86AudioNext>",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.Next"),
        desc='Audio next'
        ),
    Key("<XF86AudioPrev>",
        lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.Previous"),
        desc='Audio previous'
        ),

    Key("<XF86MonBrightnessUp>", lazy.spawn("brightnessctl -c backlight set +10%")),
    Key("<XF86MonBrightnessDown>", lazy.spawn("brightnessctl -c backlight set 10%-")),

    # Applications launcher
    Key("M-r", lazy.spawn("rofi -show combi -modes combi -combi-modes 'drun,run' -icon-theme 'Papirus' -show-icons")),
    # run apps with admin rights
    Key("M-A-r", lazy.spawn("rofi -show combi -modes combi -combi-modes 'drun,run' -icon-theme 'Papirus' -show-icons -run-command 'qt-sudo {cmd}'")),
    Key("M-A-i", lazy.spawn(myBrowser)),
    Key("M-e", lazy.spawn(myFileManager)),
    Key("M-A-d", lazy.spawn(myMarkdown)),
    Key("M-A-m", lazy.spawn(myMusicPlayer)),
    Key("M-A-p", lazy.spawn(myPDFReader)),
    Key("C-A-t", lazy.spawn(myTerm)),
    Key("M-A-t", lazy.spawn(myTextEditor)),
    Key("M-A-v", lazy.spawn("mpv")),
    Key("C-A-l", lazy.spawn("betterlockscreen -l dimblur")),
    Key("M-b", lazy.spawn("rbw-artflow.sh")),
    Key("M-S-b", lazy.spawn("rbw-jco.sh")),
    # bring floating windows to the front
    Key("M-S-f", float_to_front()),
]

groups = [
    Group("1", layout="max", matches=[Match(wm_class=["firefox", "vivaldi-stable", "qutebrowser"])]),
    Group("2", layout="bsp", matches=[Match(wm_class=["Spotify", "Slack"])]),
    Group("3", layout="max", spawn=["wezterm -e aerc"]),
    Group("4", layout="bsp", spawn=["wezterm -e yazi"]),
    Group("5", layout="bsp"),
    Group("6", layout="bsp", spawn=["wezterm"]),
    Group("7", layout="bsp", matches=[Match(wm_class=["Inkscape", "krita", "Gimp-2.10"])]),
    Group("8", layout="bsp", matches=[Match(wm_class=["FreeCAD", "Blender"])]),
    Group("9", layout="bsp", matches=[Match(title=["Fusion Studio"])]),
    Group("10", layout="bsp", matches=[Match(wm_class=["resolve"])]),
    Group("F1", layout="bsp"),
    Group("F2", layout="bsp"),
    Group("F3", layout="bsp"),
    Group("F4", layout="bsp")
]

for k, group in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<F1>", "<F2>", "<F3>", "<F4>"], groups):
    keys.append(Key("M-"+(k), lazy.group[group.name].toscreen(0)))   # Switch group on screen 0
    keys.append(Key("M-C-"+(k), lazy.group[group.name].toscreen(1)))  # Switch group on screen 1
    keys.append(Key("M-S-"+(k), lazy.window.togroup(group.name)))  # Send current window to another group

# Append scratchpads with dropdowns
groups.append(ScratchPad('scratchpad', [
    DropDown('calc', 'qalculate-gtk', height=0.4, width=0.4, x=0.3, y=0.1),
    DropDown('pyconsole', 'wezterm -e python', height=0.4, width=0.5, x=0.25, y=0.3),
]))

# Extend keys list with with keybindings for scratchpad
keys.extend([
    Key("C-"+"1", lazy.group['scratchpad'].dropdown_toggle('calc')),
    Key("C-"+"2", lazy.group['scratchpad'].dropdown_toggle('pyconsole')),
])

layout_defaults = dict(
    border_focus = "#61AFEF",
	border_normal = "#848484",
	margin = 1,
	border_width = 1
)

layouts = [
    layout.Columns(num_columns=2, **layout_defaults),
    layout.Max(**layout_defaults),
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_defaults),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Plasma(),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

widgets_primary = [
    
    widget.CurrentLayoutIcon(**widget_defaults),
    widget.CurrentLayout(**widget_defaults),
    widget.GroupBox(highlight_method="block", **widget_defaults),
    widget.TaskList(borderwidth=1, **widget_defaults),
#    widget.Chord(
#        chords_colors={
#            "launch": ("#ff0000", "#ffffff"),
#        },
#        name_transform=lambda name: name.upper(),
#    ),
]

widgets_secondary = [
    
    widget.CurrentLayoutIcon(**widget_defaults),
    widget.CurrentLayout(**widget_defaults),
    widget.GroupBox(disable_drag=True, highlight_method="block", **widget_defaults),
    widget.TaskList(borderwidth=1, **widget_defaults),
#    widget.Chord(
#        chords_colors={
#            "launch": ("#ff0000", "#ffffff"),
#        },
#        name_transform=lambda name: name.upper(),
#    ),
    widget.Systray(**widget_defaults),
    widget.Spacer(length=10, **widget_defaults),
    widget.Battery(charge_char="", discharge_char="", empty_char="󰅖", update_interval=5),
    widget.Spacer(length=10, **widget_defaults),
    widget.Clock(format="%d.%m.%Y %a %H:%M", **widget_defaults),
    widget.Spacer(length=30, **widget_defaults),
]

def status_bar(widgets): return bar.Bar(widgets, 24, opacity=0.8)

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 1:
    screens = [
        Screen(
            bottom=status_bar(widgets_primary)
        ),
        Screen(
            bottom=status_bar(widgets_secondary)
        )
    ]
else:
    screens = [
        Screen(
            bottom=status_bar(widgets_secondary)
        )
    ]

# Drag floating layouts.
mouse = [
    Drag("M-1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="notify"),
        Match(wm_class="popup_menu"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(title="Blender Preferences"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="pinentry-gtk"),  # GPG key password entry
        Match(title="rbw"),  # GPG key password entry
    ],
    **layout_defaults
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
