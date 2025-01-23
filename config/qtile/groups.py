from libqtile.config import EzKey as Key, Group, Match, ScratchPad, DropDown
from libqtile.lazy import lazy

from keys import keys


groups = [
    Group("1.WEB", layout="max", matches=[Match(wm_class=["firefox", "vivaldi-stable", "qutebrowser"])]),
    Group("2.MUSIC", layout="bsp", matches=[Match(wm_class=["Spotify", "Slack"])]),
    Group("3.EMAIL", layout="max", spawn=["kitty -e aerc"]),
    Group("4.FILE", layout="bsp", spawn=["kitty -e nnn -de"]),
    Group("5.DEV", layout="bsp", spawn=["kitty -e nvim"]),
    Group("6.TERM", layout="bsp", spawn=["kitty"]),
    Group("7.GFX", layout="bsp", matches=[Match(wm_class=["Inkscape", "krita", "Gimp-2.10"])]),
    Group("8.3D", layout="bsp", matches=[Match(wm_class=["FreeCAD", "Blender"])]),
    Group("9.COMP", layout="bsp", matches=[Match(title=["Fusion Studio"])]),
    Group("10.EDIT", layout="bsp", matches=[Match(wm_class=["resolve"])]),
    Group("F1.GFX_2", layout="bsp"),
    Group("F2.3D_2", layout="bsp"),
    Group("F3.COMP_2", layout="bsp"),
    Group("F4.EDIT_2", layout="bsp")
]

for k, group in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<F1>", "<F2>", "<F3>", "<F4>"], groups):
    keys.append(Key("M-"+(k), lazy.group[group.name].toscreen(0)))   # Switch group on screen 0
    keys.append(Key("M-C-"+(k), lazy.group[group.name].toscreen(1)))  # Switch group on screen 1
    keys.append(Key("M-S-"+(k), lazy.window.togroup(group.name)))  # Send current window to another group

# Append scratchpads with dropdowns
groups.append(ScratchPad('scratchpad', [
    DropDown('calc', 'qalculate-gtk', height=0.4, width=0.4, x=0.3, y=0.1),
    DropDown('pyconsole', 'kitty -e python', height=0.4, width=0.5, x=0.25, y=0.3),
]))

# Extend keys list with with keybindings for scratchpad
keys.extend([
    Key("C-"+"1", lazy.group['scratchpad'].dropdown_toggle('calc')),
    Key("C-"+"2", lazy.group['scratchpad'].dropdown_toggle('pyconsole')),
])
