#!/usr/bin/env bash
# HRBUST ACM-ICPC XeLaTeX package. See --help for options.
set -euo pipefail
cd "$(dirname "$0")"
exec python3 pack_overleaf.py "$@"
