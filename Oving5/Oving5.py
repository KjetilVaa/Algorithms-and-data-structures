#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict
import string
alfa = " abcdefghijklmnopqrstuvwxyz"
bokstavIndex = dict([ (x[1],x[0]) for x in enumerate(alfa) ])


def flexradix(A, d):
    ut = A
    for i in range(d-1,-1,-1):
        ut = countingSort(ut,i)
    return ut

def countingSort(A,p):
    amount = [0] * 27
    sortert =[""]*(len(A))
    for word in A:
        if(len(word) > p):
            amount[indSok(word[p])]+=1
        else:
            amount[0]+=1

    for i in range(1, 27):
        amount[i]+= amount[i-1]


    for i in range(len(A)-1,-1,-1):
        if(len(A[i])> p):
            sortert[amount[indSok(A[i][p])]-1] = A[i]
            amount[indSok(A[i][p])]-=1
        else:
            sortert[amount[0]-1] = A[i]
            amount[0]-=1

    return sortert

def indSok(C):
        return bokstavIndex[C]

def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
