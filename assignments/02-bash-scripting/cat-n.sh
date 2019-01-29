
#!/usr/bin/env bash
if [[ $# -eq 1 ]]; then
  FILE=$1
else
  echo "Usage: cat-n.sh FILE"
  exit 1
fi

if [[ ! -f "$FILE" ]]; then
echo "$FILE is not a file"
exit 1
fi

i=0
while read -r LINE; do
i=$((i+1))
echo "$i $LINE"
done < "$FILE"
