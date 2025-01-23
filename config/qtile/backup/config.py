import os
import socket
import subprocess

from libqtile import bar, hook, layout, qtile
from libqtile.config import EzClick as Click, EzDrag as Drag, EzKey as Key, Group, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

import default_apps
from keys import keybindings

powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash")
    ]
}

obj_keys = keybindings()

keys = obj_keys.init_keys()

groups = [
    Group("1.WEB", layout="max", matches=[Match(wm_class=["firefox"])]),
    Group("2.MUSIC", layout="bsp", matches=[Match(wm_class=["Spotify", "Slack"])]),
    Group("3.EMAIL", layout="max", spawn=["kitty -e neomutt"]),
    Group("4.FILE", layout="bsp", spawn=["kitty -e nnn -rd"]),
    Group("5.DEV", layout="bsp", matches=[Match(wm_class=["code-oss", "code"])], spawn=["kitty -e nvim"]),
    Group("6.TERM", layout="bsp", spawn=["kitty -e tmux"]),
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


layout_theme = {"border_focus": "#61AFEF",
                "border_normal": "#848484",
                "margin": 2,
                "border_width": 2
                }

layouts = [
    layout.Bsp(**layout_theme),
    layout.Columns(num_columns=2, **layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Slice(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    layout.Zoomy(columnwidth=300, **layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    )
]

colours = [["#141414", "#141414"],  # 0 Background
           ["#FFFFFF", "#FFFFFF"],  # 1 Foreground
           ["#ABB2BF", "#ABB2BF"],  # 2 Grey Colour
           ["#E35374", "#E35374"],  # 3
           ["#89CA78", "#89CA78"],  # 4
           ["#F0C674", "#F0C674"],  # 5
           ["#61AFEF", "#61AFEF"],  # 6
           ["#D55FDE", "#D55FDE"],  # 7
           ["#2BBAC5", "#2BBAC5"]]  # 8

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    background=colours[0],
    foreground=colours[1],
    font="Hack Nerd Font",
    fontsize=12,
    padding=1
)
extension_defaults = widget_defaults.copy()

widgets_primary = [
    widget.Sep(
        foreground=colours[0],
        linewidth=4,
    ),
    widget.Image(
        filename="~/.config/qtile/py.png",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun -icon-theme 'Papirus' -show-icons")},
        scale=True,
        # background="555555",
        # **powerline
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.GroupBox(
        active=colours[4],  # active group font color
        inactive=colours[6],  # inactive group font color
        other_current_screen_border=colours[2],  # Border or line colour for group on other screen when focused
        other_screen_border=colours[2],  # Border or line colour for group on other screen when unfocused
        this_current_screen_border=colours[7],  # Border or line colour for group on this screen when focused
        this_screen_border=colours[7],  # Border or line colour for group on this screen when unfocused
        urgent_border=colours[3],
        urgent_text=colours[3],
        disable_drag=True,
        highlight_method='line',
        borderwidth=2,
        # highlight_color = colours[8],
        invert_mouse_wheel=True,
        margin=2,
        padding=1,
        rounded=True,
        urgent_alert_method='text',
        # background="000000",
        # **powerline
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.CurrentLayout(
        foreground=colours[7],
        font="SF Pro Text Semibold",
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.Systray(
        icon_size=14,
        padding=4,
    ),
    widget.Cmus(
        noplay_color=colours[2],
        play_color=colours[1],
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    #    widget.WindowName(
    #        max_chars = 75,
    #    ),
    #    widget.TextBox(
    #        font = "JetBrainsMono Nerd Font Regular",
    #        fontsize = 14,
    #        padding = 0,
    #        text = ' '
    #    ),
    #    widget.Mpris2(
    #        display_metadata = ['xesam:title', 'xesam:artist'],
    #        name = "spotify",
    #        objname = "org.mpris.MediaPlayer2.spotify",
    #        stop_pause_text = "Stopped",
    #        padding = 4,
    #        scroll_chars = None
    #    ),
    #    widget.Sep(
    #        foreground = colours[2],
    #        linewidth = 1,
    #        padding = 10,
    #    ),
    widget.Spacer(),
    widget.TextBox(
        foreground=colours[3],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
        padding=0,
        text=' '
    ),
    widget.CPU(
        foreground=colours[3],
        format='{freq_current}GHz {load_percent}%',
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
        update_interval=1.0,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[4],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
        padding=0,
        text='󰘚 ',
    ),
    widget.Memory(
        foreground=colours[4],
        format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    #    widget.TextBox(
    #        foreground = colours[5],
    #        font = "JetBrainsMono Nerd Font Regular",
    #        fontsize = 14,
    #        padding = 0,
    #        text = ' ',
    #    ),
    #    widget.CheckUpdates(
    #        colour_have_updates = colours[5],
    #        colour_no_updates = colours[5],
    #        custom_command = 'checkupdates',
    #    #   custom_command = 'dnf updateinfo -q --list',
    #        display_format = '{updates} Updates',
    #    #   execute = "pkexec /usr/bin/dnf up -y",
    #        execute = "pkexec /usr/bin/pacman -Syu --noconfirm",
    #        no_update_string = 'Up to date!',
    #        update_interval = 900,
    #    ),
    #    widget.Sep(
    #        foreground = colours[2],
    #        linewidth = 1,
    #        padding = 10,
    #    ),
    widget.TextBox(
        foreground=colours[6],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        mouse_callbacks=({
            "Button1": lambda: qtile.cmd_spawn("amixer -M set Master toggle"),
            "Button3": lambda: qtile.cmd_spawn("pavucontrol-qt"),
            "Button4": lambda: qtile.cmd_spawn("amixer -M set Master 5%- unmute"),
            "Button5": lambda: qtile.cmd_spawn("amixer -M set Master 5%+ unmute"),
        }),
        padding=0,
        text=' ',
    ),
    widget.Volume(
        foreground=colours[6],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol-qt")},
        step=5,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[7],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        padding=0,
        text='󰖟 ',
    ),
    widget.Net(
        # width = 100,
        foreground=colours[7],
        # format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
        # prefix = 'M',
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.Battery(
        foreground=colours[7],
        low_foreground=colours[3],
        charge_char='󰂄 ',
        discharge_char='󰁿 ',
        empty_char='󰂎 ',
        full_char='󰁹 ',
        unknown_char='󰂑 ',
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        format='{char}',
        low_percentage=0.2,
        padding=0,
        show_short_text=False,
    ),
    widget.Battery(
        foreground=colours[7],
        low_foreground=colours[3],
        format='{percent:2.0%}',
        low_percentage=0.2,
        notify_below=20,
        background="000000",
        **powerline
    ),
    #    widget.Sep(
    #        foreground = colours[2],
    #        linewidth = 1,
    #        padding = 10,
    #    ),
    widget.TextBox(
        foreground=colours[8],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        # padding = 20,
        text='󱛡 ',
        background="222222",
    ),
    widget.Clock(
        foreground=colours[8],
        format='%a %b %d  %H:%M   ',
        background="222222",
    ),
]

widgets_secondary = [
    widget.Sep(
        foreground=colours[0],
        linewidth=4,
    ),
    widget.Image(
        filename="~/.config/qtile/py.png",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun -icon-theme 'Papirus' -show-icons")},
        scale=True,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.GroupBox(
        active=colours[4],  # active group font color
        inactive=colours[6],  # inactive group font color
        other_current_screen_border=colours[7],  # Border or line colour for group on other screen when focused
        other_screen_border=colours[7],  # Border or line colour for group on other screen when unfocused
        this_current_screen_border=colours[2],  # Border or line colour for group on this screen when focused
        this_screen_border=colours[2],  # Border or line colour for group on this screen when unfocused
        urgent_border=colours[3],
        urgent_text=colours[3],
        disable_drag=True,
        highlight_method='line',
        borderwidth=2,
        # highlight_color = colours[8],
        invert_mouse_wheel=True,
        margin=2,
        padding=1,
        rounded=True,
        urgent_alert_method='text',
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.CurrentLayout(
        foreground=colours[7],
        font="SF Pro Text Semibold",
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    #    widget.WindowName(
    #        max_chars = 75,
    #    ),
    widget.Spacer(),
    widget.Clock(
        foreground=colours[8],
        format='%a %b %d  %H:%M   ',
    ),
]

widgets_jco = [
    widget.Sep(
        foreground=colours[0],
        linewidth=4,
    ),
    widget.Image(
        filename="~/.config/qtile/jco-logo.svg",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun -icon-theme 'Papirus' -show-icons")},
        scale=True,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.GroupBox(
        active=colours[4],  # active group font color
        inactive=colours[6],  # inactive group font color
        other_current_screen_border=colours[2],  # Border or line colour for group on other screen when focused
        other_screen_border=colours[2],  # Border or line colour for group on other screen when unfocused
        this_current_screen_border=colours[7],  # Border or line colour for group on this screen when focused
        this_screen_border=colours[7],  # Border or line colour for group on this screen when unfocused
        urgent_border=colours[3],
        urgent_text=colours[3],
        disable_drag=True,
        highlight_method='line',
        borderwidth=2,
        # highlight_color = colours[8],
        invert_mouse_wheel=True,
        margin=2,
        padding=1,
        rounded=True,
        urgent_alert_method='text',
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.CurrentLayout(
        foreground=colours[7],
        font="SF Pro Text Semibold",
    ),
    widget.Systray(
        icon_size=14,
        padding=4,
    ),
    widget.Cmus(
        noplay_color=colours[2],
        play_color=colours[1],
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.WindowName(
        max_chars=75,
    ),
    widget.TextBox(
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        padding=0,
        text=' '
    ),
    widget.Mpris2(
        display_metadata=['xesam:title', 'xesam:artist'],
        name="spotify",
        objname="org.mpris.MediaPlayer2.spotify",
        stop_pause_text="Stopped",
        padding=4,
        scroll_chars=None
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[3],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
        padding=0,
        text=' '
    ),
    widget.CPU(
        foreground=colours[3],
        format='{freq_current}GHz {load_percent}%',
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
        update_interval=1.0,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[4],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
        padding=0,
        text='﬙ ',
    ),
    widget.Memory(
        foreground=colours[4],
        format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e bpytop')},
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[5],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        padding=0,
        text=' ',
    ),
    widget.CheckUpdates(
        colour_have_updates=colours[5],
        colour_no_updates=colours[5],
        custom_command='checkupdates',
        #   custom_command = 'dnf updateinfo -q --list',
        display_format='{updates} Updates',
        #   execute = "pkexec /usr/bin/dnf up -y",
        execute="pkexec /usr/bin/pacman -Syu --noconfirm",
        no_update_string='Up to date!',
        update_interval=900,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[6],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        mouse_callbacks=({
            "Button1": lambda: qtile.cmd_spawn("amixer -M set Master toggle"),
            "Button3": lambda: qtile.cmd_spawn("pavucontrol-qt"),
            "Button4": lambda: qtile.cmd_spawn("amixer -M set Master 5%- unmute"),
            "Button5": lambda: qtile.cmd_spawn("amixer -M set Master 5%+ unmute"),
        }),
        padding=0,
        text='墳 ',
    ),
    widget.Volume(
        foreground=colours[6],
        mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol-qt")},
        step=5,
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[7],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        padding=0,
        text='爵 ',
    ),
    widget.Net(
        foreground=colours[7],
        format='{interface}: U {up} D {down}',
        prefix='M',
    ),
    widget.Sep(
        foreground=colours[2],
        linewidth=1,
        padding=10,
    ),
    widget.TextBox(
        foreground=colours[8],
        font="JetBrainsMono Nerd Font Regular",
        fontsize=14,
        padding=0,
        text=' ',
    ),
    widget.Clock(
        foreground=colours[8],
        format='%a %b %d  %H:%M    ',
    ),
]


def status_bar(widgets): return bar.Bar(widgets, 20, opacity=0.8)


connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if socket.gethostname() == "asus-arch":  # if we are on asus-arch

    if connected_monitors > 1:
        # for i in range(1, connected_monitors):
        #   screens.append(Screen(top=status_bar(widgets)))
        screens = [
            Screen(
                top=status_bar(widgets_jco),
                wallpaper="/home/mats/git-repos/LinuxConf/dotfiles/wallpapers/wallhaven-m3zjx1.jpg",
                wallpaper_mode="fill"
            ),
            Screen(
                top=status_bar(widgets_secondary),
                wallpaper="/home/mats/git-repos/LinuxConf/dotfiles/wallpapers/wallhaven-m3zjx1.jpg",
                wallpaper_mode="fill"
            )
        ]
    else:
        screens = [
            Screen(
                top=status_bar(widgets_jco),
                wallpaper="/home/mats/git-repos/LinuxConf/dotfiles/wallpapers/wallhaven-m3zjx1.jpg",
                wallpaper_mode="fill"
            )
        ]

else:

    if connected_monitors > 1:
        # for i in range(1, connected_monitors):
        #   screens.append(Screen(top=status_bar(widgets)))
        screens = [
            Screen(
                top=status_bar(widgets_primary),
                wallpaper="/home/mats/git-repos/dotfiles/wallpapers/wallhaven-m3zjx1.jpg",
                wallpaper_mode="fill"
            ),
            Screen(
                top=status_bar(widgets_secondary),
                wallpaper="/home/mats/git-repos/dotfiles/wallpapers/wallhaven-m3zjx1.jpg",
                wallpaper_mode="fill"
            )
        ]
    else:
        screens = [
            Screen(
                top=status_bar(widgets_primary),
                wallpaper="/home/mats/git-repos/dotfiles/wallpapers/wallhaven-m3zjx1.jpg",
                wallpaper_mode="fill"
            )
        ]

mouse = [
    Drag("M-1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag("M-A-1", lazy.window.set_position(),
         start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front())
]

auto_fullscreen = True
auto_minimize = True
bring_front_click = False
cursor_warp = False
dgroups_app_rules = []  # type: List
dgroups_key_binder = None
floating_layout = layout.Floating(**layout_theme,
                                  float_rules=[
                                      *layout.Floating.default_float_rules,
                                      Match(title='Authentication'),
                                      Match(title='branchdialog'),
                                      Match(title='pinentry'),
                                      Match(wm_class='kcalc'),
                                      Match(wm_class='confirmreset'),
                                      Match(wm_class='makebranch'),
                                      Match(wm_class='maketag'),
                                      Match(wm_class='ssh-askpass'),
                                      Match(wm_class='vlc'),
                                      Match(wm_class='gwenview')
                                  ])
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
