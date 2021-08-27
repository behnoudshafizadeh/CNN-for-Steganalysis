#!/bin/bash

python train-gui.py

i=0
input="sample.txt"
while IFS= read -r line
do
  array+=($line)
  echo ${array[i]}
  i=$(($i+1))
done < "$input"


python main.py --ctrp ${array[0]} --ctep ${array[1]} --strp ${array[2]}  --step ${array[3]} --model_version 1.0.0 --nc ${array[5]} --ne ${array[6]} --bs ${array[7]} --shuffle  --op saved_weights -v 1

#rm sample.txt
