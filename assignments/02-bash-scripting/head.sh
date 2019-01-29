#!/usr/bin/env bash
#need to make file executable chmod +x head.sh

if [[ $# -eq 1 ]]; then
  FILE=$1
  N=3
fi
if [[ $# -eq 2 ]]; then
  FILE=$1
  N=$2
fi
if [[ $# -eq 0 ]]; then
  echo "Usage: head.sh FILE [N]"
  exit 1
fi


if [[ ! -f "$FILE" ]]; then
echo "$FILE is not a file"
exit 1
fi


i=0
while read -r LINE; do
echo $LINE
i=$((i+1))
if [[ $i -eq $N ]]; then
break
fi
done < "$FILE"
