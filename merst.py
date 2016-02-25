#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
 MT19937 algorithm is being used to generate the mersenne twister pseudorandom numbers

"""
# List of length(624) 
MersT = [0 for i in xrange(624)]
index = 0

# 32 bits -last
bitmask_1 = (2 ** 32) - 1

# 32 bit
bitmask_2 = 2 ** 31

# 31 bits -last
bitmask_3 = (2 ** 31) - 1

def init_gen(seed):
    "generator initialized from seed"
    global MersT
    global bitmask_1
    MersT[0] = seed
    for i in xrange(1,624):
        MersT[i] = ((1812433253 * MersT[i-1]) ^ ((MersT[i-1] >> 30) + i)) & bitmask_1


def extraction():
   #Pseudorandom number generation based on index. Call func generation() in 624 num intervals

    global index
    global MersT
    if index == 0:
        generation()
    y = MersT[index]
    y ^= y >> 11
    y ^= (y << 7) & 2636928640
    y ^= (y << 15) & 4022730752
    y ^= y >> 18
    #y2=y/10000000000.0
    y2=y/(4294967295.0 - 1.0)

    index = (index + 1) % 624
    return y2

def generation():
    #Creating 624 num array
    global MersT
    for i in xrange(624):
        y = (MersT[i] & bitmask_2) + (MersT[(i + 1 ) % 624] & bitmask_3)
        MersT[i] = MersT[(i + 397) % 624] ^ (y >> 1)
        if y % 2 != 0:
            MersT[i] ^= 2567483615

#if __name__ == "__main__":
def myrandom():
    from datetime import datetime
    now = datetime.now()
    init_gen(now.microsecond)
    for i in xrange(1):
        "Print 1 random numbers between 0 and 1"
        return extraction()


if __name__ == "__main__":
    myrandom()