import sys
import math
x,y,w,h = map(int, input().split())


x_list = []
y_list = []

points = []
min_ = 99999
for i in range(w+1):
    points.append([i,h])
    points.append([i,0])
for i in range(h+1):
    points.append([0,i])
    points.append([w,i])

for i in range(len(points)):
    dis_temp = math.sqrt(((x-points[i][0])**2) + ((y-points[i][1])**2))
    if dis_temp < min_:
        min_ = dis_temp

print(int(min_))

