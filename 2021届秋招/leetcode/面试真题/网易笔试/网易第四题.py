def distance(point1,point2):
    x0,y0,x1,y1=point1
    p0,q0,p1,q1=point2
    x_distance=min(0,max(x0,p0)-min(x1,p1))
    y_distance=min(0,max(y0,q0)-min(y1,q1))
    return x_distance+y_distance