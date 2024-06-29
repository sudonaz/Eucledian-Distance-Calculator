import math

#Points
points = [(6, 1), (4, 6), (-1, 3), (11, 8), (3, 9)]

#Function for eucledian distance
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#Calculating distance
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

#Minimum distance
min_distance = min(distances)
print("Minimum distance:", min_distance)
