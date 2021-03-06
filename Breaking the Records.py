#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest = [max(scores[:i]) for i in range(1,len(scores)+1)]
    lowest = [min(scores[:i]) for i in range(1,len(scores)+1)]
    return (len(set(highest))-1, len(set(lowest))-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
