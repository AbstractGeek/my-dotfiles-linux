type=$(loginctl show-session $(loginctl|grep $(whoami) |awk '{print $1}') -p Type)
wayland="Type=wayland"
if [ "$type" == "$wayland" ]; then
    source $HOME/.local/bin/wayland_env.sh
fi
