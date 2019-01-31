DATAPATH="../../data/gapminder/"
if [[ $# -eq 0 ]]; then
  i = 0
  for FILE in $DATAPATH/*; do
    let i++
    printf "%d %s\n" $i "$(basename $FILE '.cc.txt')"
  done
  exit 0
fi

REGEX="^"$1 #Why did I have to remove the space around the '='???

i=0
for FILE in $DATAPATH/*; do
  MATCH="$(basename $FILE '.cc.txt' | grep -i $REGEX)"
  if [[ ${#MATCH} -eq 0 ]]; then  #Check if the length of the string is 0
    continue # if it is skip
  fi
  let i++ #increment i after check
  printf "%d %s\n" $i $MATCH
done

 if [[ $i -eq 0 ]] ;then
  echo 'There are no countries starting with "'$1'"'
 fi

