def move(position, direction, ext_requests, int_requests):
    if direction == 1:
        idx = position
        for x in ext_requests[position:]:
            if x == True:
                int_requests.append(idx)
            idx += 1
        int_requests.sort()
        if not int_requests:
            return(0,position)
        for i in int_requests:
            if i > position:
                next_stop = i
                return (direction, next_stop)
        for k in int_requests[::-1]:
            next_stop = k
            direction = -1
            return (direction, next_stop)
            
        
    else:
        direction = -1
        qdx = position
        for q in ext_requests[position::-1]:
            if q == True:
                int_requests.append(qdx)
            qdx -= 1
        int_requests.sort()
        if not int_requests:
            return(0,position)
        for w in int_requests[::-1]:
            if w < position:
                next_stop = w
                return (direction, next_stop)
        for k in int_requests:
            next_stop = k
            direction = 1
            return (direction, next_stop)
    
    


def door_open(position, direction, ext_requests, int_requests):
    ext_requests[position] = False
    int_requests.remove(position)
    
    return (ext_requests, int_requests)

print(move(2, -1, [False, False, False, False, False], [4]))
##print(door_open(2, 1, [False, True, True, True, False], [2, 1]))