#!/usr/bin/env bash

if [[ $# -eq 0 ]] || [[ $# -gt 2 ]]; then
  echo "Usage: hello.sh GREETING [NAME]"
  exit 1
fi

if [[ $# -eq 1 ]]; then
  GREETING=$1
  NAME="Human"
fi

if [[ $# -eq 2 ]]; then
  GREETING=$1
  NAME=$2
fi
echo "$GREETING, $NAME!"
