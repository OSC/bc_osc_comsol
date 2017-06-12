#!/bin/bash -l

# Get current working directory
export OUTPUT_ROOT="${PWD}"

# Get source directory of this script
export STAGED_ROOT="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

# Set working directory to home directory
cd "${HOME}"

#
# Launch Fluxbox
#

FLUXBOX_RC_FILE="${OUTPUT_ROOT}/fluxbox.rc"
FLUXBOX_ASSETS_ROOT="${STAGED_ROOT}/fluxbox"

# Create Fluxbox root or it will override the below init file
(
  umask 077
  mkdir -p "${HOME}/.fluxbox"
)

# Build Fluxbox init file
cat > "${FLUXBOX_RC_FILE}" << EOT
session.configVersion: 13
session.screen0.toolbar.widthPercent: 60
session.screen0.toolbar.tools: prevworkspace, workspacename, nextworkspace, iconbar, systemtray, prevwindow, nextwindow, clock
session.menuFile: $FLUXBOX_ASSETS_ROOT/menu
session.keyFile: $FLUXBOX_ASSETS_ROOT/keys
session.styleOverlay: $FLUXBOX_ASSETS_ROOT/overlay
EOT

# Export the module function for the terminal
[[ $(type -t module) == "function" ]] && export -f module

# Start the Fluxbox window manager (it likes to crash on occassion, make it
# persistent)
(
  export FLUXBOX_ASSETS_ROOT="${FLUXBOX_ASSETS_ROOT}"
  until fluxbox -display "${DISPLAY}.0" -rc "${FLUXBOX_RC_FILE}"; do
    echo "Fluxbox crashed with exit code $?. Respawning..." >&2
    sleep 1
  done
) &

#
# Start COMSOL Multiphysics
#

# Restore the module environment to avoid conflicts
module restore

# Load the COMSOL module
module load ${COMSOL_MODULE}

# Launch COMSOL Multiphysics
if [[ ${ENABLE_VIS} ]]; then
  module load virtualgl
  vglrun comsol
else
  comsol -3drend sw
fi
