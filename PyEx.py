import math

points = [(1, 2), (7, 14), (3, 8), (2, 11)]

def func(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = func(points[i], points[j])
        distances.append(distance)

if distances:  
    min_distance = min(distances)
    print(f"Minimum mesafe: {min_distance}")
else:
    print("Hesaplanan mesafe yok")
