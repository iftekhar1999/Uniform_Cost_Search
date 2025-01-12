import math

adj = {'A': {'B': 3, 'J': 4, 'G': 1},
       'B': {'A': 3, 'D': 10},
       'C': {'H': 3},
       'D': {'B': 10, 'J': 3, 'H': 11},
       'E': {'G': 14, 'F': 2, 'I': 1},
       'F': {'G': 8, 'E': 2, 'I': 2, 'H': 4},
       'G': {'A': 1, 'J': 6, 'F': 8, 'E': 14},
       'H': {'D': 11, 'F': 4, 'I': 6, 'C': 3},
       'I': {'E': 1, 'F': 2, 'H': 6},
       'J': {'A': 4, 'G': 6, 'D': 3}
       }

source = 'A'
destination = 'C'

visited = []

path = []

mapping1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
mapping2 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}

for i in range(1, 12):
    path.append(i)

stack = [source]

i = 0

while True:
    if len(stack) == 0:
        break;
    curNode = stack.pop()
    visited.append(curNode)
    if curNode == destination:
        break;
    for i in adj[curNode]:
        if i not in visited:
            stack.append(i)
            path[mapping1[i]] = mapping1[curNode]

ans = [destination]

if destination in visited:
    while True:
        ans.append(mapping2[path[mapping1[destination]]])
        destination = mapping2[path[mapping1[destination]]]
        if destination == source:
            break;

ans.reverse()

for i in ans:
    print(i, end='->')

priorityQueue = {}

priorityQueue['B'] = 3
priorityQueue['J'] = 4
priorityQueue['G'] = 1
priorityQueue['D'] = 3
priorityQueue['E'] = 1
priorityQueue['F'] = 2
priorityQueue['H'] = 3
priorityQueue['I'] = 1
priorityQueue['C'] = 3

minValue = math.inf
minNode = ''
for key in priorityQueue.keys():
    if priorityQueue[key] < minValue:
        minValue = priorityQueue[key]
        minNode = key

print('Min Node: ', minNode, minValue)



