#!/usr/bin/env sh

pid=$(ps aux | grep alacritty | grep  khal | grep interactive | awk '{print $2}')
if (( ${pid} )); then
    kill $pid
else
    alacritty -t 'floating_term_khal' -e khal interactive
fi
