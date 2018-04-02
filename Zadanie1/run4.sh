#!/usr/bin/env bash

# Zadanie 4.1
./Program.py Data/approximation_train_1.txt 1 1 -q Data/approximation_test.txt --lino -n 1 5 9 13 17 -i 5 -b -pt Wyniki/Wykres4_A1.png
./Program.py Data/approximation_train_2.txt 1 1 -q Data/approximation_test.txt --lino -n 1 5 9 13 17 -i 5 -b -pt Wyniki/Wykres4_A2.png


# Zadanie 4.2
./Program.py Data/approximation_train_1.txt 1 1 -q Data/approximation_test.txt -Q --lino -n 1 5 19 -i 5 -b -pe Wyniki/Wykres4_B1.png
./Program.py Data/approximation_train_2.txt 1 1 -q Data/approximation_test.txt -Q --lino -n 1 5 19 -i 5 -b -pe Wyniki/Wykres4_B2.png


# Zadanie 4.3
rm -rf Wyniki/Wyniki4_C1.txt
rm -rf Wyniki/Wyniki4_C1.txt
for (( i=1; $i <= 20; i++ ))
do
  for (( k=1; $k <= 5; k++ ))
  do
    ./Program.py Data/approximation_train_1.txt 1 1 -q Data/approximation_test.txt --lino -n $i -i 4 -b -sd Wyniki/Wyniki4_C1.txt
    ./Program.py Data/approximation_train_2.txt 1 1 -q Data/approximation_test.txt --lino -n $i -i 4 -b -sd Wyniki/Wyniki4_C2.txt
  done
done


# Zadanie 4.4
./Program.py Data/approximation_train_1.txt 1 1 -q Data/approximation_test.txt -Q --lino -n 5 -i 5 -b -pl Wyniki/Wykres4_D1.png
./Program.py Data/approximation_train_2.txt 1 1 -q Data/approximation_test.txt -Q --lino -n 5 -i 5 -b -pl Wyniki/Wykres4_D2.png
