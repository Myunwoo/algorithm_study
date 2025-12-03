#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

from collections import deque

def bfs(start, visited, graph):
    dq = deque()
    dq.append(start)
    
    while dq:
        cur = dq.popleft()
        for i in range(n):
            if graph[cur][i] and not visited[i]:
                dq.append(i)
                visited[i] = True
    

def countIsolatedCommunicationGroups(links, n):
    answer = 0
    visited = [False for _ in range(n)]
    graph = [[False for _ in range(n)] for _ in range(n)]
    
    # bidirectional graph
    for link in links:
        graph[link[0]][link[1]] = True
        graph[link[1]][link[0]] = True
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, graph)
            answer += 1
            
    return answer
    

if __name__ == '__main__':
    links_rows = int(input().strip())
    links_columns = int(input().strip())

    links = []

    for _ in range(links_rows):
        links.append(list(map(int, input().rstrip().split())))

    n = int(input().strip())

    result = countIsolatedCommunicationGroups(links, n)

    print(result)
