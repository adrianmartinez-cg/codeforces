
def addNeighborsToQ(q,visited,grid,currentPoint,point1_coord):
    steps = -1
    for i in range(-1,2):
        for j in range(-1,2):
            neighbor = ((currentPoint[0][0]+i,currentPoint[0][1]+j),currentPoint[1]+1)
            neighbor_coord = neighbor[0]
            if grid.has_key(neighbor_coord): # valid neighbor
                if not visited.has_key(neighbor_coord): #not visited yet
                    visited[neighbor_coord] = True
                    q.append(neighbor)
                    if neighbor_coord == point1_coord:
                        steps = neighbor[1]
                        break
        if steps != -1:
            break
    return steps

if __name__ == "__main__":
    coords = list(map(int,raw_input().split()))
    point0 = ((coords[0],coords[1]),0)
    point1_coord = (coords[2],coords[3])
    n = int(raw_input())
    grid = {}
    q = []
    q.append(point0)
    visited = {}
    visited[point0[0]] = True

    for _ in range(n):
        seg = list(map(int,raw_input().split()))
        for j in range(seg[1],seg[2]+1):
            point = (seg[0],j)
            grid[point] = True

    while True:
        currentPoint = q.pop(0)
        steps = addNeighborsToQ(q,visited,grid,currentPoint,point1_coord)
        if len(q)==0 or steps != -1: 
            break
    print(steps)