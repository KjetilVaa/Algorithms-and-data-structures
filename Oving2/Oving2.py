#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    rootNode = Node()
    currentNode = rootNode

    for tuppel in ordliste:
        currentNode = rootNode
        i = 0
        for bokstav in tuppel[0]:
            bokstav = bokstav
            if (bokstav not in currentNode.barn):
                currentNode.barn[bokstav] = Node()
            i+=1
            currentNode = currentNode.barn[bokstav]
            if (len(tuppel[0]) == i):
                currentNode.posi.append(tuppel[1])
    return rootNode



def posisjoner(ord, indeks, node):
    currentNode = node
    i = indeks
    if i == len(ord):
        return currentNode.posi
    bokstav = ord[i]
    if not bokstav == "?":
        if bokstav in currentNode.barn:
            return posisjoner(ord, i + 1, currentNode.barn[bokstav])
    elif bokstav == "?":
        flereSvar = []
        for o in currentNode.barn:
            flereSvar.extend(posisjoner(ord, i+1,currentNode.barn[o]))
        return flereSvar
    else:
        return []

    return currentNode.posi



def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)



if __name__ == "__main__":
    main()
