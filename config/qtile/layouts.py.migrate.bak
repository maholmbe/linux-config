from libqtile import layout
from libqtile.config import Match


layout_defaults = dict(
    border_focus = "#61AFEF",
	border_normal = "#848484",
	margin = 1,
	border_width = 1
)

# floating_layout_defaults = layout_defaults.copy()
# floating_layout_defaults["border_width"] = 0

layouts = [
    layout.Bsp(**layout_defaults),
    layout.Columns(num_columns=2, **layout_defaults),
    # layout.Matrix(**layout_defaults),
    # layout.MonadWide(**layout_defaults),
    # layout.RatioTile(**layout_defaults),
    # layout.Slice(**layout_defaults),
    # layout.Stack(num_stacks=2),
    # layout.Stack(stacks=2, **layout_defaults),
    # layout.Tile(shift_windows=True, **layout_defaults),
    # layout.VerticalTile(**layout_defaults),
    # layout.Zoomy(columnwidth=300, **layout_defaults),
    # layout.Floating(**layout_defaults),
    layout.Max(**layout_defaults),
    # layout.MonadTall(**layout_defaults),
    layout.MonadThreeCol(**layout_defaults),
    # layout.TreeTab(
    #     font="Ubuntu",
    #     fontsize=10,
    #     sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
    #     section_fontsize=10,
    #     border_width=2,
    #     bg_color="1c1f24",
    #     active_bg="c678dd",
    #     active_fg="000000",
    #     inactive_bg="a9a1e1",
    #     inactive_fg="1c1f24",
    #     padding_left=0,
    #     padding_x=0,
    #     padding_y=5,
    #     section_top=10,
    #     section_bottom=20,
    #     level_shift=8,
    #     vspace=3,
    #     panel_width=200
    # )
]

floating_layout = layout.Floating(
        float_rules = [# Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
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
            Match(wm_class="confirmreset"), # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(title="Blender Preferences"),
        ],
    **layout_defaults
)
    # float_rules=[
    #*layout.Floating.default_float_rules,
    # Match(title='Authentication'),
    # Match(title='branchdialog'),
    # Match(title='pinentry'),
    # Match(wm_class='kcalc'),
    # Match(wm_class='confirmreset'),
    # Match(wm_class='makebranch'),
    # Match(wm_class='maketag'),
    # Match(wm_class='ssh-askpass'),
    # Match(wm_class='vlc'),
    # Match(wm_class='gwenview')

    # {'wmclass': 'confirm'},
    # {'wmclass': 'dialog'},
    # {'wmclass': 'download'},
    # {'wmclass': 'error'},
    # {'wmclass': 'file_progress'},
    # {'wmclass': 'notification'},
    # {'wmclass': 'notify'},
    # {'wmclass': 'popup_menu'},
    # {'wmclass': 'splash'},
    # {'wmclass': 'toolbar'},
    # {'wmclass': 'confirmreset'},  # gitk
    # {'wmclass': 'makebranch'},  # gitk
    # {'wmclass': 'maketag'},  # gitkm
    # {'wname': 'branchdialog'},  # gitk
    # {'wname': 'pinentry'},  # GPG key password entry
    # {'wmclass': 'ssh-askpass'},  # ssh-askpass
#], **layout_defaults)
