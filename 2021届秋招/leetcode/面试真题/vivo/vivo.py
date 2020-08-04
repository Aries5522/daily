# 牛客网输入输出模板

import sys
import math


def isprime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True





if __name__ == "__main__":

    num = 0
    N = 1
    product = 1
    temp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in range(num + 1):
        N = N * temp[i]
    N = N + 1
    if isprime(N):
        print('%d is a prime' % N)
    else:
        print('%d is not a prime' % N)
