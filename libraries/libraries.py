from collections import defaultdict


def countNeighbors(visited, startCity, routes):
    toVisit = set()
    count = 0

    toVisit.add(startCity)
    visited.add(startCity)

    while len(toVisit) > 0:
        cur = toVisit.pop()
        for neighbor in routes[cur]:
            if neighbor not in visited:
                toVisit.add(neighbor)
                visited.add(neighbor)
                count += 1

    return count


def calcCost(n, clib, croad, routes):
    print("n", n, "clib", clib, "croad", croad, "routes", routes)
    if clib <= croad:
        return n * clib

    visited = set()
    roadCount = 0
    clusterCount = 0
    for i in range(n):
        if i not in visited:
            roadCount += countNeighbors(visited, i, routes)
            clusterCount += 1

    print("clusters", clusterCount, "road", roadCount)
    return clusterCount * clib + roadCount * croad



f = open("input.txt", "r")
queries = int(f.readline())
for i in range(queries):
    line = f.readline().split(" ")
    n = int(line[0])
    m = int(line[1])
    clib = int(line[2])
    croad = int(line[3])

    routes = defaultdict(set)
    for i in range(m):
        line = f.readline().split(" ")
        routes[int(line[0])-1].add(int(line[1])-1)
        routes[int(line[1])-1].add(int(line[0])-1)

    print(calcCost(n, clib, croad, routes))
