def compute_iou(rec1, rec2):
    """
    :param rec1: (x0,y0,x1,y1)(left,top,riht,bottom)
    :param rec2: equle rec1
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
    print("{}{}{}{}".format(left_line_max,right_lin_min,top_line_max,bottom_line_min))
    if left_line_max > right_lin_min or top_line_max > bottom_line_min:
        return 0
    else:
        commen_area = (left_line_max - right_lin_min) * (top_line_max - bottom_line_min)
        print("commen_area:{}".format(commen_area))
        return commen_area / (sum_area - commen_area)


if __name__ == '__main__':
    rec1 = (1, 1, 3, 3)
    rec2 = (2, 2, 4, 4)
    print(compute_iou(rec1, rec2))
