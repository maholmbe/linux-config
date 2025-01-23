from libqtile.lazy import lazy
from libqtile.config import EzClick as Click, EzDrag as Drag, EzKey as Key

import default_apps


class keybindings:

    keys = []

    def init_keys(self):

        self.keys = [
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
            Key("<XF86AudioLowerVolume>", lazy.spawn("amixer -M set Master 5%- unmute")),
            Key("<XF86AudioRaiseVolume>", lazy.spawn("amixer -M set Master 5%+ unmute")),
            Key("<XF86AudioMute>", lazy.spawn("amixer -M set Master toggle")),

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

            Key("<XF86MonBrightnessDown>", lazy.spawn("light -U 10")),
            Key("<XF86MonBrightnessUp>", lazy.spawn("light -A 10")),
            # Key("A-j", lazy.spawn("brightnessctl set 10%-")),
            # Key("A-k", lazy.spawn("brightnessctl set 10%+")),

            # Applications launcher
            Key("M-r", lazy.spawn("rofi -show combi -modes combi -combi-modes 'window,drun,run' -icon-theme 'Papirus' -show-icons")),
            # Key("M-A-r", lazy.spawn("launcher_text")),
            # run apps with admin rights
            Key("M-A-r", lazy.spawn("rofi -show combi -modes combi -combi-modes 'drun,run' -icon-theme 'Papirus' -show-icons -run-command 'xfsudo {cmd}'")),
            Key("M-A-i", lazy.spawn(default_apps.myBrowser)),
            Key("M-e", lazy.spawn(default_apps.myFileManager)),
            Key("M-A-d", lazy.spawn(default_apps.myMarkdown)),
            Key("M-A-m", lazy.spawn(default_apps.myMusicPlayer)),
            Key("M-A-o", lazy.spawn(default_apps.myOfficeSuite)),
            Key("M-A-p", lazy.spawn(default_apps.myPDFReader)),
            Key("C-A-t", lazy.spawn(default_apps.myTerm)),
            Key("M-A-t", lazy.spawn(default_apps.myTextEditor)),
            Key("M-A-e", lazy.spawn(default_apps.myTerm + ' -e vifm')),
            Key("M-A-v", lazy.spawn("vlc")),
            Key("C-A-l", lazy.spawn("betterlockscreen -l dimblur")),
        ]

        return self.keys
