from sys import stdin, stderr

# Capacities is the original capacity-matrix, which contains n x n elemensts (where n is the amount of nodes)
# start_room is an array with the indexes to the nodes which corresponds to the start rooms.
# Exits is an array with the indexes to the nodes which corresponds to the exits.

def isolated_paths_count(capacities, start_rooms, exits):
    # You can use the method find_flow_path to simplify the problem
    # SKRIV DIN KODE HER
    #Try to find flow-paths until there are none. Needs superSource, superExit, flow and new matrix as argument
    matrix, flow = setup(capacities, start_rooms, exits, len(capacities))
    n = len(matrix)
    superSource = 0
    superExit = n - 1
    count = 0
    morePaths = True
    while(morePaths):
        #Finds a path to increase flow
        path = find_flow_path(superSource, superExit, flow, matrix)
        if not (path == None):
            count += 1
            #Update flow in flow-matrix
            for i in range(len(path) - 1):
                flow[path[i]][path[i+1]] = 1
                flow[path[i+1]][path[i]] = -1
        else:
            morePaths = False
    return count




def setup(cap, sources, exits, lenght):
    #Making new matrix for duplicated nodes and superSource/superExit
    newCapacities = []
    flow = []
    for i in range(lenght*2+2):
        newCapacities.append([0] * (2*lenght+2))
        flow.append([0] * (2*lenght+2))
    #Connecting the superSource with other sources
    for k in sources:
        newCapacities[0][k*2+1] = 1
    #Connecting the superExit with other exits
    for j in exits:
        newCapacities[j*2+2][2*lenght+1] = 1
    #Connecting all divided nodes
    for o in range(lenght):
        newCapacities[2*o+1][2*o+2] = 1
    #Connecting all original nodes
    for t in range(lenght):
        for e in range(lenght):
            newCapacities[2*t+2][2*e+1] = cap[t][e]

    return newCapacities, flow




# Finds a path from the source_node to the drain_node
# with available capacity in a flow-network with flow F and capacity C.
# Returns an array where the first element is the index to omne of the start nodes,
# last element is the index to one of the exits and the elements between
# are the indexes of the nodes along the path, in the correct order.
# Example: A path from the start node 4 to node 3, node 9, node 7 and finally
# to the exit 12 will be represented as [4,3,9,7,12].

def find_flow_path(source, drain, F, C):
    n = len(F)
    discovered = [False] * n
    parent = [None] * len(F)
    queue = [source]
    while queue:
        node = queue.pop(0)
        if node == drain:
            # The drain is found, create an array of passed nodes.
            path = []
            i = node
            while True:
                path.append(i)
                if i == source:
                    break
                i = parent[i]
            path.reverse()
            return path;
        for neighbour in range(n):
            if not discovered[neighbour] and F[node][neighbour] < C[node][neighbour]:
                queue.append(neighbour);
                discovered[neighbour] = True;
                parent[neighbour] = node;
    return None

noder, _, _ = [int(x) for x in stdin.readline().split()]
start_rooms = [int(x) for x in stdin.readline().split()]
exits = [int(x) for x in stdin.readline().split()]
adjacency_matrix = []
for linje in stdin:
    naborad = [int(nabo) for nabo in linje.split()]
    adjacency_matrix.append(naborad)
print(isolated_paths_count(adjacency_matrix, start_rooms, exits))
