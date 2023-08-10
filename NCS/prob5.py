# 문제 5

import random

def generate_points(n):
    center_x, center_y = 5, 5
    points = set()
    
    while len(points) < n:
        x = random.randint(0, 10)
#       x = random.uniform(0, 10) 
        y = random.randint(0, 10)
#       y = random.uniform(0, 10)

        # 정수 값의 좌표를 출력할 경우 random.randint(0, 10) 사용
        # 소수점 값의 좌표를 출력할 경우 random.uniform(0, 10) 사용

        distance = ((x - center_x)**2 + (y - center_y)**2)**0.5
        
        if distance <= 2.5:
            points.add((x, y))
    
    return points

coord_count = 20
coordinates = generate_points(coord_count)

print("중심 (5, 5)에서 가까운 좌표:")
for coord in coordinates:
    print(coord)
