#!/usr/bin/env bash

if [[ ${#} -ne 1 ]]; then
    echo -e "Usage:\n\x20\x20${0} /path/to/json/config"
else
    python3 worker.py "${1}"
fi
