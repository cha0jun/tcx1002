steps, sn = [], 1
def display(disc_lst):
  global steps, sn
  steps.append([r.copy() for r in disc_lst])
  print(f'step{sn}: {disc_lst}')
  sn += 1

def tower(disc_lst, n, source, dest, spare):

    if n == 0:
        return

    tower(disc_lst, n - 1, source, spare, dest)

    # Move the top disk
    disk = disc_lst[source].pop(0)
    disc_lst[dest].insert(0, disk)
    display(disc_lst)

    tower(disc_lst, n - 1, spare, dest, source)

tower([[1,2,3], [], []], 3, 0, 2, 1)