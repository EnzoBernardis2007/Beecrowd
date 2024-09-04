import math

point1 = list(map(float, input().split(" ")))
point2 = list(map(float, input().split(" ")))

print(f"{math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)):.4f}")
