#!/usr/bin/env sh

# set variables
RELEASE_URL=https://github.com/pandoc/lua-filters/releases/latest
PANDOC_DIR=$HOME/Repositories/dotfiles/pandoc

# download and extract
curl -LSs $RELEASE_URL/download/lua-filters.tar.gz | \
    tar --strip-components=1 --one-top-level=$PANDOC_DIR -zvxf -
    
# run install if install has a glob link instead of a folder link
# currently a folder link
#bash $HOME/Repositories/dotfiles/install
