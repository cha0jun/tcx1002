data = {
    "lectures": [
        ("TCX1001", "LT9", 4, 13, 15),  # Course code, room name, day of week,                                     start time, end time
        ("TCX1002", "LT9", 4, 19, 21),
        ("TCX1003", "LT8", 2, 18, 20)
    ],
    "tutorials": [
        ("TCX1001-T1", "LT9", 0, 9, 11),
        ("TCX1001-T2", "LT8", 6, 9, 11),
        ("TCX1001-T3", "LT9", 6, 13, 15),
    ]
}

def combine_bookings(data):
  empty_schedule = [[False, False, False, False, False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False, False, False, False, False]]
  res = {}
  for course, room, day_of_week, start_time, end_time in data["lectures"] + data['tutorials']:
    if room not in res:
      res[room] = empty_schedule
    res[room][day_of_week][start_time-9:end_time-9] = [True,] * (end_time-start_time)
  return res

data_674677 = {
    "lectures": [
        ("TCX1001", "LT9", 1, 9, 15),  # Course code, room name, day of week,                                     start time, end time
        ("TCX1002", "LT9", 4, 10, 21),
        ("TCX1003", "LT8", 2, 10, 20)
    ],
    "tutorials": [
    ]
}

res = combine_bookings(data)
for key in res:
  print(key)
  for x in res[key]:
    print(x)
print()
res = combine_bookings(data_674677)
for key in res:
  print(key)
  for x in res[key]:
    print(x)