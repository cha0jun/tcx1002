import numpy as np

def shortest(list_of_points):
  points = np.array(list_of_points)
  d = np.linalg.norm(points - points[:, np.newaxis], axis=2)
  # print(d)
  visited, unvisited = [0], list(range(1, len(list_of_points)))
  while unvisited:
    min_distance, min_index = 1e20, 0
    for j in unvisited:
      if d[visited[-1]][j] < min_distance:
        min_distance = d[visited[-1]][j]
        min_index = j
    visited.append(min_index)
    unvisited.remove(min_index)
  return [tuple(x) for x in points[visited]]