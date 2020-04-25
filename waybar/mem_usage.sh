#!/usr/bin/env sh

pid=$(ps aux | grep alacritty | grep  htop | grep MEM | awk '{print $2}')
if (( ${pid} )); then
    kill $pid
else
    alacritty -t 'floating_term_htop' -e htop --sort-key=PERCENT_MEM
fi
