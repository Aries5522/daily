import sys
import math

data = [int(i) for i in input().split()]
r = data[0]
x1, y1 = data[1], data[2]
mid_x_point = (data[3] + data[5]) / 2
mid_y_point = (data[4] + data[6]) / 2
distance = math.sqrt((x1 - mid_x_point) ** 2 + (y1 - mid_y_point) ** 2)
if distance > r + abs(data[5]-data[3]) / 2:
    print(False)
else:
    print(True)
