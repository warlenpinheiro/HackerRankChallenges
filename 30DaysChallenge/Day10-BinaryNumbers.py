#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    ntobin = int(bin(n)[2:])
    count = 0
    maximo = 0
    for i in list(str(ntobin)):
        if int(i) == 1:
            count += 1
        else:
            count = 0
        if(count > maximo):
            maximo = count

    print(maximo)
