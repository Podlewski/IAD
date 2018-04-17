#!/usr/bin/env bash

# Zadanie 3.1
#./Program.py Data/transformation.txt 4 4 -n 1 2 3 -a 0.1 -i 4 -pe Wyniki/Wykres3_A1.png --bias
#./Program.py Data/transformation.txt 4 4 -n 1 2 3 -a 0.1 -i 4 -pe Wyniki/Wykres3_A2.png

# Zadanie 3.2
rm -rf Wyniki/Wyniki3_B.txt
for i in 0.01 0.05 0.1 0.5 1.0
do
  for j in 0 0.0001 0.001 0.01
  do
    for (( k=1; $k <= 5; k++ ))
    do
      ./Program.py Data/transformation.txt 4 4 -n 2 -e 4 --bias -a $i -m $j -e 4 -sr Wyniki/Wyniki3_B.txt
    done
  done
done

# Zadanie 3.3
# rm -rf Wyniki/Wyniki3_C1.txt Wyniki/Wyniki3_C1.txt
# rm -rf Wyniki/Wyniki3_C1.txt Wyniki/Wyniki3_C2.txt
# ./Program.py Data/transformation.txt 4 4 -n 2 -i 6 -sh Wyniki/Wyniki3_C1.txt --bias
#./Program.py Data/transformation.txt 4 4 -n 2 -i 6 -sh Wyniki/Wyniki3_C2.txt
