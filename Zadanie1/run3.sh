#!/usr/bin/env bash

# Zadanie 3.1
./Program.py Dane/transformation.txt 4 4 -n 1 2 3 -b -a 0.1 -i 4 -sp Wyniki/Wykres3_A1.png
./Program.py Dane/transformation.txt 4 4 -n 1 2 3 -a 0.1 -i 4 -sp Wyniki/Wykres3_A2.png


# Zadanie 3.2
rm -rf Wyniki/Wyniki3_B.txt
for i in 0.1 0.25 0.5 0.75 1
do
  for j in 0 0.0001 0.001 0.01
  do
    for (( k=1; $k <= 5; k++ ))
    do
      ./Program.py Dane/transformation.txt 4 4 -n 2 -b -a $i -m $j -e 5 -sd Wyniki/Wyniki3_B.txt
    done
  done
done


# Zadanie 3.3
rm -rf Wyniki/Wyniki3_C1.txt Wyniki/Wyniki3_C2.txt
./Program.py Dane/transformation.txt 4 4 -n 2 -b -i 6 -sh Wyniki/Wyniki3_C1.txt
./Program.py Dane/transformation.txt 4 4 -n 2 -i 6 -sh Wyniki/Wyniki3_C2.txt
