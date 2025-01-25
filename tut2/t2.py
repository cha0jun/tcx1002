from math import sin, cos, sqrt, atan2, radians

def get_distance(geo_p1, geo_p2):
  # Approximate radius of earth in km
  R = 6373.0

  lat1 = radians(geo_p1[0])
  lon1 = radians(geo_p1[1])
  lat2 = radians(geo_p2[0])
  lon2 = radians(geo_p2[1])

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))

  distance = R * c
  return distance

  
# Add your code below
bus143 = [(1.33222, 103.84691),  (1.33255, 103.74065),(1.332638, 103.846606),(1.330295, 103.845952) ] # Add more turning points

def calc_distance(bus_no:list):
    distance = 0
    for idx in range(len(bus_no)-1):
        distance = distance + get_distance(bus_no[idx],bus_no[idx+1])
    return distance

print(calc_distance(bus143))