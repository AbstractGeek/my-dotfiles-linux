# Firefox doesn't use wayland by default yet:
export MOZ_ENABLE_WAYLAND=1
export MOZ_DBUS_REMOTE=1
# Older versions of Qt always show window decorations. To hide them:
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
# Some Java AWT apps would not display properly unless you set the following:
export _JAVA_AWT_WM_NONREPARENTING=1
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK
