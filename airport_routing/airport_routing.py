from collections import defaultdict


def find_routes():
    visit_list = set(airport_src)
    path = [airport_src]

    for next_airport in routes[airport_src]:
        find_routes_recursive(path, next_airport, visit_list)


def find_routes_recursive(path, current, visit_list):
    path_local = path[:]
    path_local.append(current)

    #print "path so far", path_local, "at", current, "visit_list = ", visit_list
    if current == airport_dst:
        print " ".join(path_local)
        return

    visit_list_local = visit_list.copy()
    visit_list_local.add(current)
    for i in routes[current]:
        if i not in visit_list_local:
            find_routes_recursive(path_local, i, visit_list_local)


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

for x in range(numRoutes):
    route = f.readline().split(' ')
    src = route[0].strip()
    dst = route[1].strip()
    routes[src].append(dst)
    routes[dst].append(src)


#print numRoutes
#print airport_src, airport_dst
#print routes


find_routes()