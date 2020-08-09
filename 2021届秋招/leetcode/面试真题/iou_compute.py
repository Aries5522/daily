def compute_iou(rec1, rec2):
    """
    :param rec1: (x0,y0,x1,y1)(left,top,riht,bottom)
    :param rec2: equal rec1
    :return:  value of iou
    """
    s_rec1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
    s_rec2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
    sum_area = s_rec1 + s_rec2
    print(sum_area)
    left_line_max = max(rec1[0], rec2[0])
    right_lin_min = min(rec1[2], rec2[2])
    top_line_max = max(rec1[1], rec2[1])
    bottom_line_min = min(rec1[3], rec2[3])
    print("{},{},{},{}".format(left_line_max, right_lin_min, top_line_max, bottom_line_min))
    commen_area = max(0, (left_line_max - right_lin_min) * (top_line_max - bottom_line_min))
    print("commen_area:{}".format(commen_area))
    return commen_area / (sum_area - commen_area)

def IOU(matrix):
    pass

def NMS(list_reference, threshold):
    """
    :param list_reference: point and confidence-->(x0,y0,x1,y1,confidence),shape:n*5
    :return: NMS result
    """
    n = len(list_reference)
    if not list_reference:
        return []
    list_reference = sorted(list_reference, key=lambda x: x[4], reverse=True)  ##按照置信度排序大到小
    res = []
    while list_reference:
        point1 = list_reference[0][0:4]
        res.append(list_reference.pop(0))
        list_left = []
        while list_reference:
            point2 = list_reference[0][0:4]
            if compute_iou(point1, point2) > threshold:
                list_reference.pop(0)
            else:
                list_left.append(list_reference.pop(0))
        list_reference = list_left
    return res


if __name__ == '__main__':
    rec1 = (1, 1, 3, 3)
    rec2 = (2, 2, 4, 4)
    rec3 = (1, 1, 3, 3)
    print(compute_iou(rec1, rec2))

    list_test = [(1, 1, 3, 3, 0.99), (1, 1, 3, 3, 0.8), (2, 2, 4, 4, 0.3)]
    print(NMS(list_test, threshold=0.6))
