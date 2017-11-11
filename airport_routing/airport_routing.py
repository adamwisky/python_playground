from collections import defaultdict


def find_routes():
    visit_list = set(airport_src)
    path = [airport_src]

    for next_airport in routes[airport_src]:
        find_routes_recursive(path, next_airport, visit_list)


def find_routes_recursive(path, current, visitlist):
    print "path so far", path, "at", current, "visitList = ", visitlist
    if current == airport_dst:
        print " ".join(path)
        return

    visitlist.add(current)
    for i in routes[current]:
        if i not in visitlist:
            path.append(i)
            find_routes_recursive(list(path), i, set(visitlist))


routes = defaultdict(list)
numRoutes = 0
airport_src = ""
airport_dst = ""

f = open("input.txt", 'r')

#input format:
# n  (number of routes)
#airport_src airport_dst, global src, dst
#airport_src airport_dst, line separated

lineList = f.readline().split(' ')
numRoutes = int(lineList[0])

lineList = f.readline().split(' ')
airport_src = lineList[0].strip()
airport_dst = lineList[1].strip()

for i in range(numRoutes):
    route = f.readline().split(' ')
    src = route[0].strip()
    dst = route[1].strip()
    routes[src].append(dst)
    routes[dst].append(src)


print numRoutes
print airport_src, airport_dst
print routes


find_routes()