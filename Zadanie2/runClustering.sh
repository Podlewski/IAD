#!/usr/bin/env bash

# Zadanie 2A
./Program.py -ac -sc 0 0 5 222 -n 2 4 6 8 10 12 14 16 18 20 -ce ResultsC/2A
./Program.py -ac -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 4 6 8 10 12 14 16 18 20 -ce ResultsC/2A


# Zadanie 2B
tekst="Normalnie:\n"
printf $tekst >> ResultsC/2B_KMC_20_1_D.txt
printf $tekst >> ResultsC/2B_KMC_20_2_D.txt
for i in {0..25}
do
  ./Program.py -ac -sc 0 0 5 222 -n 20 -d ResultsC/2B
  ./Program.py -ac -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsC/2B
done

tekst="\nMniejszy_zakres_losowania:\n"
printf $tekst >> ResultsC/2B_KMC_20_1_D.txt
printf $tekst >> ResultsC/2B_KMC_20_2_D.txt
for i in {0..25}
do
  ./Program.py -ac -r 5 5 -sc 0 0 5 222 -n 20 -d ResultsC/2B
  ./Program.py -ac -r 5 5 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsC/2B
done

tekst="\nRownoodlegle_na_srodkowej_lini:\n"
printf $tekst >> ResultsC/2B_KMC_20_1_D.txt
printf $tekst >> ResultsC/2B_KMC_20_2_D.txt
for i in {0..25}
do
  ./Program.py -ac -rl -sc 0 0 5 222 -n 20 -d ResultsC/2B
  ./Program.py -ac -rl -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsC/2B
done

tekst="\nRownoodlegle_na_symetrycznych_liniach:\n"
printf $tekst >> ResultsC/2B_KMC_20_1_D.txt
printf $tekst >> ResultsC/2B_KMC_20_2_D.txt
for i in {0..25}
do
  ./Program.py -ac -rs -sc 0 0 5 222 -n 20 -d ResultsC/2B
  ./Program.py -ac -rs -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsC/2B
done


# Zadanie 2C
./Program.py -ac -sc 0 0 5 222 -n 2 -ch ResultsC/2C -cv ResultsC/2C
./Program.py -ac -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 -ch ResultsC/2C -cv ResultsC/2C
./Program.py -ac -sc 0 0 5 222 -n 10 -ch ResultsC/2C -cv ResultsC/2C
./Program.py -ac -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 10 -ch ResultsC/2C -cv ResultsC/2C
