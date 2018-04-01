#!/usr/bin/env bash

# Zadanie 4.1
#./Program.py Dane/approximation_train_1.txt 1 1 -q Dane/approximation_test.txt --lino -n 1 5 9 13 17 -i 4 -b -spt Wyniki/Wykres4_A1.png
#./Program.py Dane/approximation_train_2.txt 1 1 -q Dane/approximation_test.txt --lino -n 1 5 9 13 17 -i 4 -b -spt Wyniki/Wykres4_A2.png
#./Program.py Dane/approximation_train_1.txt 1 1 -q Dane/approximation_test.txt --lino -n 1 5 9 13 17 -e 2 -b -spt Wyniki/Wykres4_A3.png
#./Program.py Dane/approximation_train_2.txt 1 1 -q Dane/approximation_test.txt --lino -n 1 5 9 13 17 -e 2 -b -spt Wyniki/Wykres4_A4.png


# Zadanie 4.2
./Program.py Dane/approximation_train_1.txt 1 1 -q Dane/approximation_test.txt -Q --lino -n 1 5 19 -i 4 -b -spe Wyniki/Wykres4_B1.png
./Program.py Dane/approximation_train_2.txt 1 1 -q Dane/approximation_test.txt -Q --lino -n 1 5 19 -i 4 -b -spe Wyniki/Wykres4_B2.png


# Zadanie 4.3
rm -rf Wyniki/Wyniki4_C1.txt
rm -rf Wyniki/Wyniki4_C1.txt
for (( i=1; $i <= 20; i++ ))
do
  for (( k=1; $k <= 5; k++ ))
  do
    ./Program.py Dane/approximation_train_1.txt 1 1 -q Dane/approximation_test.txt --lino -n $i -i 4 -b -sd Wyniki/Wyniki4_C1.txt
    ./Program.py Dane/approximation_train_2.txt 1 1 -q Dane/approximation_test.txt --lino -n $i -i 4 -b -sd Wyniki/Wyniki4_C2.txt
  done
done


# Zadanie 4.4
