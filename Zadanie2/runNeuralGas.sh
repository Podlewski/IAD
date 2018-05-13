#!/usr/bin/env bash

# Zadanie 1A
./Program.py -ag -lp 0.005 0.01 -sc 0 0 5 222 -n 2 4 6 8 10 12 14 16 18 20 -ce ResultsG/1A
./Program.py -ag -lp 0.001 0.01 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 4 6 8 10 12 14 16 18 20 -ce ResultsG/1A


# Zadanie 1B
tekst="Normalnie:\n"
printf $tekst >> ResultsG/1B_NG_20_1_D.txt
printf $tekst >> ResultsG/1B_NG_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ag -lp 0.005 0.01 -sc 0 0 5 222 -n 20 -d ResultsG/1B
  ./Program.py -ag -lp 0.001 0.01 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsG/1B
done

tekst="\nWieksza_waga_1:\n"
printf $tekst >> ResultsG/1B_NG_20_1_D.txt
printf $tekst >> ResultsG/1B_NG_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ag -lp 0.05 0.01 -sc 0 0 5 222 -n 20 -d ResultsG/1B
  ./Program.py -ag -lp 0.01 0.01 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsG/1B
done

tekst="\nWieksza_waga_2:\n"
printf $tekst >> ResultsG/1B_NG_20_1_D.txt
printf $tekst >> ResultsG/1B_NG_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ag -lp 0.005 0.1 -sc 0 0 5 222 -n 20 -d ResultsG/1B
  ./Program.py -ag -lp 0.001 0.1 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsG/1B
done

tekst="\nWagi_ze_wzoru:\n"
printf $tekst >> ResultsG/1B_NG_20_1_D.txt
printf $tekst >> ResultsG/1B_NG_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ag -olp -sc 0 0 5 222 -n 20 -d ResultsG/1B
  ./Program.py -ag -olp -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsG/1B
done

tekst="\nRownoodlegle_na_srodkowej_lini:\n"
printf $tekst >> ResultsG/1B_NG_20_1_D.txt
printf $tekst >> ResultsG/1B_NG_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ag -rl -lp 0.005 0.01 -sc 0 0 5 222 -n 20 -d ResultsG/1B
  ./Program.py -ag -rl -lp 0.001 0.01 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsG/1B
done

tekst="\nRownoodlegle_na_symetrycznych_liniach:\n"
printf $tekst >> ResultsG/1B_NG_20_1_D.txt
printf $tekst >> ResultsG/1B_NG_20_2_D.txt
for i in {0..12}
do
  ./Program.py -ag -rs -lp 0.005 0.01 -sc 0 0 5 222 -n 20 -d ResultsG/1B
  ./Program.py -ag -rs -lp 0.001 0.01 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d ResultsG/1B
done


# Zadanie 1C
./Program.py -ag -olp -sc 0 0 5 222 -n 2 -ch ResultsG/1C -cv ResultsG/1C
./Program.py -ag -olp -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 -ch ResultsG/1C -cv ResultsG/1C
./Program.py -ag -olp -sc 0 0 5 222 -n 10 -ch ResultsG/1C -cv ResultsG/1C
./Program.py -ag -olp -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 10 -ch ResultsG/1C -cv ResultsG/1C
