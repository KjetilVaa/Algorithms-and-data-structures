#!/usr/bin/python3

from sys import stdin
from itertools import repeat

def mergeSort(decks):
    result, svar = mergeSort(decks)
    return svaret



def merge(decks):
    if(len(decks) > 1):
        result = []
        svar = ""
        mid = int(len(decks)/2)
        left, leftString = merge(decks[:mid])
        right, rightString = merge(decks[mid:])
        i = 0
        j = 0
        while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    result.append(right[j])
                    svar+=right[j][1]
                    j += 1
                else:
                    result.append(left[i])
                    svar+=left[i][1]
                    i += 1
        result += left[i:]
        result += right[j:]
        svar+=leftString[i:]
        svar+=rightString[j:]


    else:
        return decks,decks[0][1]
    return  result, svar


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.extend(deck)
    # Merge the decks and print result.
    print(merge(decks)[1])


if __name__ == "__main__":
    main()
