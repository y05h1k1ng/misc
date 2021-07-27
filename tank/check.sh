#!/bin/bash
NUMS=(1 2 3 4 5 6 7)

for num in ${NUMS[@]}; do
    diff\
        <(cat data/data$num.in | python3 solver.py)\
        data/data$num.out\
        > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo "[+] passed (data"$num")"
    else
        echo "[-] failed (data"$num")"
    fi
done
