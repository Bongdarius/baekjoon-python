#벌집
'''
1까지는 1칸
7까지는 2칸  
19까지는 3칸
37까지는 4칸
61까지는 5칸
91까지는 6칸
127까지는 7칸
169까지는 8칸

6 12 18 24 30 36 42

6, 18, 36, 60, 90, 126, 168

1   3   6   10  15  21  28


6
6+6
6+6+6
6+6+6+6
6+6+6+6+6
6+6+6+6+6+6
'''
def find_min_rooms(location):
    layer = 1
    rooms = 1
    
    while rooms < location:
        rooms += layer * 6  # 다음 층의 방의 개수를 계산합니다.
        layer += 1
    
    return layer

location = int(input())
print(find_min_rooms(location))
