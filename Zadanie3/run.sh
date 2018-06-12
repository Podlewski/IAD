#!/usr/bin/env bash

# Zadanie 3.1
./Program.py Data/train.txt Data/test.txt 1 11 21 31 41 -i 3 -s 0.1 -p Results/3_1_A
# ./Program.py Data/train.txt Data/test.txt 1 11 21 31 41 -i 3 -p Results/3_1_B
./Program.py Data/train.txt Data/test.txt 1 11 21 31 41 -i 3 -s 4 -p Results/3_1_C

# Zadanie 3.2
./Program.py Data/train.txt Data/test.txt 21 -i 3 -s 0.1 -pr Results/3_2_A
./Program.py Data/train.txt Data/test.txt 21 -i 3 -pr Results/3_2_B
./Program.py Data/train.txt Data/test.txt 21 -i 3 -s 4 -pr Results/3_2_C

# Zadanie 3.3
for j in 1 6 11 16 21 26 31 36 41
do
  for i in {0..11}
  do
    ./Program.py Data/train.txt Data/test.txt $j -i 3 -sr Results/3_3
  done
done

# Zadanie 3.4
./Program.py Data/train.txt Data/test.txt 21 -i 3 -ph Results/3_4
