#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for file in *.jump; do
  ./jump2remmina.py -i ${file} >  `basename ${file} .jump`.remmina
done
IFS=$SAVEIFS
