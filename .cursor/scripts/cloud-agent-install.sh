#!/usr/bin/env bash
# Idempotent Cloud Agent bootstrap for the TPL Personal Assistant workspace.
#
# This repository is a PMO / delivery-tracking workspace (no application build).
# The only runtime toolchain the skills and hooks depend on is:
#   - Python 3 (standard library only) for the docx / Jira-export helper scripts
#   - PowerShell (pwsh) for the Cursor hooks and the send-daily-timelog scripts
#   - git / curl (already present in the base image)
#
# It is safe to run repeatedly: PowerShell is only installed when missing.
set -euo pipefail

log() { printf '[cloud-agent-install] %s\n' "$*"; }

require() {
  if ! command -v "$1" >/dev/null 2>&1; then
    log "ERROR: required tool '$1' is not available"
    return 1
  fi
  log "found $1 -> $(command -v "$1") ($("$1" --version 2>&1 | head -n1))"
}

install_powershell() {
  if command -v pwsh >/dev/null 2>&1; then
    log "pwsh already installed -> $(pwsh --version)"
    return 0
  fi

  log "pwsh not found; installing PowerShell from the Microsoft apt repository"
  # shellcheck disable=SC1091
  . /etc/os-release
  local deb="/tmp/packages-microsoft-prod.deb"
  curl -fsSL "https://packages.microsoft.com/config/ubuntu/${VERSION_ID}/packages-microsoft-prod.deb" -o "$deb"
  sudo dpkg -i "$deb"
  rm -f "$deb"
  sudo apt-get update -qq
  sudo apt-get install -y -qq powershell
  log "installed $(pwsh --version)"
}

main() {
  cd "$(dirname "$0")/../.."
  log "workspace root: $(pwd)"

  # Base toolchain (must already be present in the image).
  require git
  require curl
  require python3

  # PowerShell for hooks + send-daily-timelog scripts.
  install_powershell
  require pwsh

  # Sanity-check that the repo's helper scripts still parse with this toolchain.
  log "compiling Python helper scripts"
  python3 -m py_compile .cursor/skills/pattern-data-daily-progress/scripts/*.py

  log "parsing PowerShell scripts"
  while IFS= read -r -d '' ps1; do
    pwsh -NoProfile -Command \
      "\$null=[System.Management.Automation.Language.Parser]::ParseFile('$ps1',[ref]\$null,[ref]\$null)" \
      && log "parsed OK: $ps1"
  done < <(find .cursor -name '*.ps1' -print0)

  log "environment ready"
}

main "$@"
