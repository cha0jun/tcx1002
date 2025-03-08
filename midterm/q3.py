match_results = [
    ('Alice', 'Bob'),
    ('Charlie', 'Bob'),
    ('Alice', 'Charlie'),
]

def top_n_players(match_results, N):
    res = {}
    for winner, loser in match_results:
      if winner in res:
        res[winner] = (res[winner][0]+1, res[winner][1])
      else:
        res[winner] = (1, 0)
      if loser in res:
        res[loser] = (res[loser][0], res[loser][1]+1)
      else:
        res[loser] = (0, 1)

    for key in res:
      res[key] = res[key][0]/(res[key][0]+res[key][1])

    sorted_players = sorted(res.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_players)
    res = sorted_players[:N]
    for x in sorted_players[N:]:
      if x[1] == sorted_players[N-1][1]:
        res.append(x)
      else:
        break
    return [x[0] for x in res]