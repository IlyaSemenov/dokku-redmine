#!/bin/bash
set -e
eval "$(dokku-vars.py)"
/sbin/entrypoint.sh "$@"
