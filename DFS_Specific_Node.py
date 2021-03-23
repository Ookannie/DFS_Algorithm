
"""
Created on Mon Mar 22 20:25:27 2021

@author: Zannie
"""

graph = {
  'H' : ['P','D', 'M'],
  'P' : ['N'],
  'N' : ['I', 'K', 'O'],
  'I' : [],
  'K' : ['F','B'],
  'O' : [],
  'F' : [],
  'B' : [],
  'D' : ['L','E'],
  'L' : ['Q','R','G'],
  'Q' : ['A'],
  'A' : [],
  'R' : [],
  'G' : [],
  'E' : [],
  'M' : ['J', 'C'],
  'J' : [],
  'C' : []
}


def DFS(graph, start, find):
    visited = []

    recursive_DFS(start, visited, graph, find)    
        
    return visited


def recursive_DFS(current, visited, graph, find):
    if find in visited: return
    if current in visited: return
    visited.append(current)
    neighbors = graph[current]

    for neighbor in neighbors:
        recursive_DFS(neighbor, visited, graph, find)
    
    
    


print(DFS(graph, 'H', 'L'))