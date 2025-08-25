# 0층에는 1, 2, 3, 4, 5... 호에는 각 호의 인원만큼 거주하고 있음.
def _create_data(floor, ho):
    arr = []
    for x in range(0, floor + 1, 1):
        ho_arr = []
        for y in range(0, ho, 1):
            if(x == 0):
                ho_arr.append(y + 1)
            else:
                temp_arr = (list)(arr[x - 1])
                sum = 0
                for z in range(0, y + 1, 1):
                    sum += temp_arr[z]
                ho_arr.append(sum)
        arr.append(ho_arr)
    return arr[floor][ho - 1]

case = (int)(input())
req = []
for i in range(0, case, 1):
    floor = (int)(input())
    ho = (int)(input())
    req.append(_create_data(floor, ho))

for i in range(0, len(req), 1):
    print(req[i])

# 1, 4, 10, 20, 35    
# 1, 3, 6, 10, 15
# 1, 2, 3, 4, 5