#!/usr/bin/env bash

# Zadanie 1A
./Program.py -ak -lp 0.02 0 -sc 0 0 5 222 -n 2 4 6 8 10 12 14 16 18 20 -ce Results/1A
./Program.py -ak -lp 0.02 0 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 4 6 8 10 12 14 16 18 20 -ce Results/1A


# Zadanie 1B
tekst="Normalnie:\n"
printf $tekst >> Results/2B_Koh_G_20_1_D.txt
printf $tekst >> Results/2B_Koh_G_20_2_D.txt
for i in {0..19}
do
  ./Program.py -ak -lp 0.01 0.1 -sc 0 0 5 222 -n 20 -d Results/2B
  ./Program.py -ak -lp 0.01 0.1 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d Results/2B
done

tekst="\nWieksze_parametry:\n"
printf $tekst >> Results/2B_Koh_G_20_1_D.txt
printf $tekst >> Results/2B_Koh_G_20_2_D.txt
for i in {0..19}
do
  ./Program.py -ak -lp 0.03 0.3 -sc 0 0 5 222 -n 20 -d Results/2B
  ./Program.py -ak -lp 0.03 0.3 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -d Results/2B
done

tekst="\nMeczenie_neuronow:\n"
printf $tekst >> Results/2B_Koh_G_20_1_D.txt
printf $tekst >> Results/2B_Koh_G_20_2_D.txt
for i in {0..19}
do
  ./Program.py -ak -lp 0.03 0.3 -sc 0 0 5 222 -n 20 -t -d Results/2B
  ./Program.py -ak -lp 0.03 0.3 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -t -d Results/2B
done

tekst="\nRownoodlegle_na_srodkowej_lini_oraz_meczenie:\n"
printf $tekst >> Results/2B_Koh_G_20_1_D.txt
printf $tekst >> Results/2B_Koh_G_20_2_D.txt
for i in {0..19}
do
  ./Program.py -ak -rl -lp 0.03 0.3 -sc 0 0 5 222 -n 20 -t -d Results/2B
  ./Program.py -ak -rl -lp 0.03 0.3 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -t -d Results/2B
done

tekst="\nRownoodlegle_na_symetrycznych_liniach_oraz_meczenie:\n"
printf $tekst >> Results/2B_Koh_G_20_1_D.txt
printf $tekst >> Results/2B_Koh_G_20_2_D.txt
for i in {0..19}
do
  ./Program.py -ak -rs -lp 0.03 0.3 -sc 0 0 5 222 -n 20 -t -d Results/2B
  ./Program.py -ak -rs -lp 0.03 0.3 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 20 -t -d Results/2B
done


# Zadanie 1C
./Program.py -ak -lp 0.03 0.3 -sc 0 0 5 222 -n 2 -ch Results/1C -cv Results/1C
./Program.py -ak -lp 0.03 0.3 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 2 -ch Results/1C -cv Results/1C
./Program.py -ak -lp 0.03 0.5 -sc 0 0 5 222 -n 10 -nc -t -ch Results/1C -cv Results/1C
./Program.py -ak -lp 0.03 0.5 -sw -5 0 3 111 -sr 2 3 7 -3 111 -n 10 -nc -t -ch Results/1C -cv Results/1C
