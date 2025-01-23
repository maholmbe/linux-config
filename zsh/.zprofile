if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec startx
  #exec tbsm
fi

#[[ $XDG_VTNR -eq 1 ]] && tbsm
