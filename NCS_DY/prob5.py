import random

def generate_points(n):
    center_x, center_y = 5, 5
    points = set()
    
    while len(points) < n:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        
        distance = ((x - center_x)**2 + (y - center_y)**2)**0.5
        
        if distance <= 2.5:  # 중심 (5, 5)로부터 거리 2.5 이내에 있는 좌표
            points.add((x, y))
    
    return points

# 20개의 좌표 생성
coordinate_count = 20
coordinates = generate_points(coordinate_count)

# 결과 출력
print("중심 (5, 5)에서 가까운 좌표:")
for coord in coordinates:
    print(coord)
