#!/bin/bash

for((i = 1; i<=99; i++)); do
NUM=$[ $i & 1 ]
if [ $NUM -eq 0 ]; then
    continue
else
    echo $i
fi
done
