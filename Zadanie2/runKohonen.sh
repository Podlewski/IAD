#!/usr/bin/env bash

# Zadanie 1A
./Program.py -ak -lp 0.02 0 -sc 0 0 5 222 -n 2 4 6 8 10 12 14 16 18 20 -ce ResultsK/1A
./Program.py -ak -lp 0.02 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 4 6 8 10 12 14 16 18 20 -ce ResultsK/1A


# Zadanie 1B
tekst="Normalnie:\n"
printf $tekst >> ResultsK/1B_Koh_20_1_D.txt
printf $tekst >> ResultsK/1B_Koh_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ak -lp 0.02 0 -sc 0 0 5 222 -n 20 -d ResultsK/1B
  ./Program.py -ak -lp 0.02 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsK/1B
done

tekst="\nWieksza_waga:\n"
printf $tekst >> ResultsK/1B_Koh_20_1_D.txt
printf $tekst >> ResultsK/1B_Koh_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ak -lp 0.1 0 -sc 0 0 5 222 -n 20 -d ResultsK/1B
  ./Program.py -ak -lp 0.1 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsK/1B
done

tekst="\nSasiedztwo:\n"
printf $tekst >> ResultsK/1B_Koh_20_1_D.txt
printf $tekst >> ResultsK/1B_Koh_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ak -lp 0.02 1 -sc 0 0 5 222 -n 20 -d ResultsK/1B
  ./Program.py -ak -lp 0.02 1 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsK/1B
done

tekst="\nWieksza_waga_+_sasiedztwo:\n"
printf $tekst >> ResultsK/1B_Koh_20_1_D.txt
printf $tekst >> ResultsK/1B_Koh_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ak -lp 0.1 1 -sc 0 0 5 222 -n 20 -d ResultsK/1B
  ./Program.py -ak -lp 0.1 1 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsK/1B
done

tekst="\nRownoodlegle_na_srodkowej_lini:\n"
printf $tekst >> ResultsK/1B_Koh_20_1_D.txt
printf $tekst >> ResultsK/1B_Koh_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ak -rl -lp 0.02 0 -sc 0 0 5 222 -n 20 -d ResultsK/1B
  ./Program.py -ak -rl -lp 0.02 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsK/1B
done

tekst="\nRownoodlegle_na_symetrycznych_liniach:\n"
printf $tekst >> ResultsK/1B_Koh_20_1_D.txt
printf $tekst >> ResultsK/1B_Koh_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ak -rs -lp 0.02 0 -sc 0 0 5 222 -n 20 -d ResultsK/1B
  ./Program.py -ak -rs -lp 0.02 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsK/1B
done


# Zadanie 1C
./Program.py -ak -lp 0.02 0 -sc 0 0 5 222 -n 2 -ch ResultsK/1C -cv ResultsK/1C
./Program.py -ak -lp 0.02 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 -ch ResultsK/1C -cv ResultsK/1C
./Program.py -ak -lp 0.02 1 -sc 0 0 5 222 -n 10 -nc -ch ResultsK/1C -cv ResultsK/1C
./Program.py -ak -lp 0.02 1 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 10 -nc -ch ResultsK/1C -cv ResultsK/1C
