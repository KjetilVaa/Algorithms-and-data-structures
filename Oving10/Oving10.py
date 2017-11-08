from sys import stdin
from heapq import *

Inf = float(1e3000)


def mst(nList, n):
    # Prims
    heap = []
    tagged = [0] * n
    heaviest = 0

    for i in nList[0]:
        heappush(heap, i)
    tagged[0] = 1

    for i in range(1, n):
        if not 0 in tagged:
            break

        while heap:
            edge = heappop(heap)
            target = edge[1]
            if tagged[target]:
                continue
            tagged[target] = 1

            if heaviest < edge[0]:
                heaviest = edge[0]

            for e in nList[target]:
                if not tagged[e[1]]:
                    heappush(heap, e)
            break

    return heaviest


def read():
    linjer = stdin.readlines()
    n = len(linjer)
    node = 0
    nList = [None] * n

    for linje in linjer:
        cNode = []

        for k in linje.split():
            data = k.split(':')
            weight = int(data[1])
            target = int(data[0])
            edge = (weight, target)
            cNode.append(edge)
        nList[node] = cNode
        node += 1

    print(mst(nList, n))


read()
