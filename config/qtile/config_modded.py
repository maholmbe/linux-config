import os
import socket
import subprocess

from libqtile import bar, hook, layout, qtile
from libqtile.config import EzClick as Click, EzDrag as Drag, EzKey as Key, Group, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from keys import keys, mouse
from groups import groups
from layouts import layouts, floating_layout


powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash")
    ]
}

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

config_dir = os.path.dirname(__file__)
images_path = os.path.join(config_dir, "images", "")

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
        filename=images_path + "py.png",
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
    widget.WindowName(
        max_chars = 120,
    ),
    widget.Spacer(),
    widget.TextBox(
        font = "JetBrainsMono Nerd Font Regular",
        fontsize = 14,
        padding = 0,
        text = ' '
    ),
    widget.Mpris2(
        display_metadata = ['xesam:title', 'xesam:artist'],
        name = "spotify",
        objname = "org.mpris.MediaPlayer2.spotify",
        stop_pause_text = "Stopped",
        scroll_chars = None
    ),
    widget.Sep(
        foreground = colours[2],
        linewidth = 1,
        padding = 10,
    ),
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
            "Button1": lambda: qtile.cmd_spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
            "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
            "Button4": lambda: qtile.cmd_spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
            "Button5": lambda: qtile.cmd_spawn("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"),
        }),
        padding=0,
        text=' ',
    ),
    widget.Volume(
        foreground=colours[6],
        # mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        step=5,
        get_volume_command="wpctl get-volume @DEFAULT_AUDIO_SINK@",
        volume_down_command="wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+",
        volume_up_command="wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-",
        mute_command="wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle",
        volume_app="pavucontrol",
        fmt="{}",
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
        filename=images_path + "py.png",
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
        filename=images_path + "py.png",
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
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e btop')},
        padding=0,
        text=' ',
    ),
    widget.Memory(
        foreground=colours[4],
        format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(default_apps.myTerm + ' -e btop')},
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
        text='󰚰 ',
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
            "Button1": lambda: qtile.cmd_spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
            "Button3": lambda: qtile.cmd_spawn("pavucontrol"),
            "Button4": lambda: qtile.cmd_spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
            "Button5": lambda: qtile.cmd_spawn("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"),
        }),
        padding=0,
        text=' ',
    ),
    widget.Volume(
        foreground=colours[6],
        # mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("pavucontrol")},
        step=5,
        get_volume_command="wpctl get-volume @DEFAULT_AUDIO_SINK@",
        volume_down_command="wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+",
        volume_up_command="wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-",
        mute_command="wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle",
        volume_app="pavucontrol",
        fmt="{}",
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
        text='󰸗 ',
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
                top=status_bar(widgets_jco)
            ),
            Screen(
                top=status_bar(widgets_secondary)
            )
        ]
    else:
        screens = [
            Screen(
                top=status_bar(widgets_jco)
            )
        ]

else:

    if connected_monitors > 1:
        screens = [
            Screen(
                top=status_bar(widgets_primary)
            ),
            Screen(
                top=status_bar(widgets_secondary)
            )
        ]
    else:
        screens = [
            Screen(
                top=status_bar(widgets_primary)
            )
        ]

auto_fullscreen = True
auto_minimize = True
bring_front_click = False
cursor_warp = False
dgroups_app_rules = []  # type: List
dgroups_key_binder = None
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
floats_kept_above = True


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
