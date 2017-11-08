#!/usr/bin/python3

from sys import stdin
import math

def sort_list(A):
    mindre = []
    lik = []
    mer = []
    if(len(A) > 1):
        pivot = A[0]
        for o in A:
            if(o < pivot):
                mindre.append(o)
            elif(o > pivot):
                mer.append(o)
            elif(o == pivot):
                lik.append(o)
        return sort_list(mindre)+ lik + sort_list(mer)
    else:
        return A



def find(A, lower, upper):
    lavIndex = intervallSok(A,lower)
    hoyIndex = intervallSok(A,upper)
    lav = 0
    hoy = 0
    if(A[lavIndex] <= lower):
        lav = A[lavIndex]
    elif(lavIndex > 0):
        lav = A[lavIndex - 1]
    else:
        lav = A[0]

    if(A[hoyIndex] >= upper):
        hoy = A[hoyIndex]
    elif(hoyIndex + 1 <= len(A)-1):
        hoy = A[hoyIndex + 1]
    else:
        hoy = A[len(A)-1]
    return [lav,hoy]





def intervallSok(A, o):
    slutt = len(A) - 1
    start = 0
    while(start <= slutt):
        midt = int((start + slutt)/2)
        if(A[midt] < o):
            start = midt + 1
        elif(A[midt] > o):
            slutt = midt - 1
        else:
            return midt
    return midt



def main():
    input_list = []
   # stdin = open("pipesortTest.txt","r+")
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
