def find_first_slot(task1_result, room, day_of_week, duration):
  for i in range(12):
    if task1_result[room][day_of_week][i:i+duration] == [False]*duration:
      return i+9
  return None


