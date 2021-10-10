from collections import defaultdict
from heapq import heappop, heappush

def shortest_path(edges, start,destination):
  graph = defaultdict(list)
  
  for point1, point2, weight in edges:
    graph[point1].append((weight,point2))
  
  q, visited = [(0,start,())], set()
  
  while q:
    cost, v1, path = heappop(q)
    if v1 not in visited:
      visited.add(v1)
      path = (v1,path)
      
      if v1 == destination:
        return (cost,path)
      for c, v2 in graph.get(v1,()):
        if v2 not in visited:
          heappush(q,(cost+c,v2,path))
      
    print(q)
  return q    
  
  
if __name__ == "__main__":
  
  edges = [
      ("A", "B", 7),
      ("A", "D", 5),
      ("B", "C", 8),
      ("B", "D", 9),
      ("B", "E", 7),
      ("C", "E", 5),
      ("D", "E", 7),
      ("D", "F", 6),
      ("E", "F", 8),
      ("E", "G", 9),
      ("F", "G", 11)
  ]
  
  print ("=== Dijkstra ===")
  print ("A >> G:")
  print (shortest_path(edges, "A", "G"))