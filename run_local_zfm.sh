#!/bin/zsh

# This script can be used to test with the local script without interfering with the system-wide one

set -e
script_home=$( dirname $(realpath "$0") )
source "${script_home}/zfm.zsh"

# In mac os, add fzf to path...
if [[ "$OSTYPE" == "darwin"* ]]; then
  export PATH="/opt/homebrew/bin:$PATH"
fi
eval "zfm $@"
