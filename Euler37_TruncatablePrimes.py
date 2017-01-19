#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:00:47 2017

@author: christophergreen

Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to
 continuously remove digits from left to right, and remain prime at each stage:
     3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right 
and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math;

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def list_primes(max):
    primes=[]; 
    j=11
    while j<=max:
        if is_prime(j):
            primes.append(j)
        j+=1
    return primes;

primes=list_primes(10**6);
    
def is_truncatable(x):
    truncs=[];
    i=0;
    while i<len(x):
        truncs.append(int(x[i:]));
        truncs.append(int(x[:(len(x)-i)]));
        i+=1;
    truncs=list(set(truncs));
    for t in truncs:
        if '1' in str(t) and len(str(t))==1:
            return False;
        if is_prime(int(t))==False:
            #print(x,"is not truncatable because",t,"is not prime");
            return False;
    print(x,"is truncatable becasue all of its",len(truncs),"unique truncations are prime:",truncs)
    return True;

def main(primes):
    i=0;
    truncatables=[];
    while i<len(primes):
        if is_truncatable(str(primes[i])):
            truncatables.append(primes[i]);
        i+=1;
    print("these",len(truncatables),"integers are truncatable:",truncatables);
    output=0;
    for t in truncatables:
        output+=t;
    print("the sum of these items is:",output);
    return;
    
main(primes); #--> these 11 integers are truncatable: [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
#the sum of these items is: 748317 CORRECT

