
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    return s.count("a") * (n // len(s))+s[:n % len(s)].count("a")

if __name__ == '__main__':

    s = "bbbabaa"
    n = 20
        
    a = repeatedString(s, n)
    print(a)