def patterns(rows:int):
    downside = []
    pattern = []
    loops = rows//2
    x = 1
    for idx in range(loops):
        line = ' '* idx + '*' * (loops*2-x) + ' ' * idx
        downside.append(line*2)
        x += 2
    for i in downside:
        pattern.append(i)
    for k in downside[::-1]:
        pattern.append(k)
    return pattern
    
    
print(patterns(6))