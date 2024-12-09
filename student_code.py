import heapq
import math

def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def shortest_path(M, start, goal):
    print("shortest path called")
    
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        current = heapq.heappop(frontier)[1]
        
        if current == goal:
            break
        
        for next in M.roads[current]:
            new_cost = cost_so_far[current] + heuristic(M.intersections[current], M.intersections[next])
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(M.intersections[next], M.intersections[goal])
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    
    return path