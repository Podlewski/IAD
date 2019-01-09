#!/usr/bin/env bash

START=$(date +%s.%N)
for i in $( ls in*.txt ); do
    ./Program.py $i
done
wait
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo "Ended after $DIFF seconds"
