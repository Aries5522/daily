'''

##19

'''

from typing import List

#
# class Solution:
#     def array_element_insert(self, array: List, array_length, element_num, element_insert):
#         '''
#
#         :param array:   List
#         :param array_length:  max_length
#         :param element_num:    nums of element
#         :param element_insert:   target
#         :return:   array
#         ##插入排序 O(n)   O(1)
#         '''
#         if len(array) == 0:
#             return array.append(element_insert)
#         if element_insert <= array[0]:
#             array.insert(0, element_insert)
#         array.append(element_insert)
#         i = element_num - 1
#         while i >= 0:
#             if array[i + 1] < array[i]:
#                 array[i + 1], array[i] = array[i], array[i + 1]
#                 i -= 1
#             else:
#                 break
#         return array


"""
##20
"""
import numpy as np


def midfilter(src_image, w=0, h=0):
    '''
    均值滤波器
    :param src_image: 输入图像
    :return: 输出图像
    注：此实现滤波器大小必须为奇数且 >= 3
    '''
    filter_size = 3
    input_image = np.array(src_image)
    input_image_cp = np.copy(input_image)  # 输入图像的副本
    filter_template = np.ones((filter_size, filter_size))  # 空间滤波器模板
    pad_num = int((filter_size - 1) / 2)  # 输入图像需要填充的尺寸
    input_image_cp = np.pad(input_image_cp, (pad_num, pad_num), mode="constant", constant_values=0)  # 填充输入图像
    m, n = input_image_cp.shape  # 获取填充后的输入图像的大小
    output_image = np.copy(input_image_cp)  # 输出图像
    # 空间滤波
    for i in range(pad_num, m - pad_num):
        for j in range(pad_num, n - pad_num):
            output_image[i, j] = np.sum(
                filter_template * input_image_cp[i - pad_num:i + pad_num + 1, j - pad_num:j + pad_num + 1]) / (
                                             filter_size ** 2)

    dst_image = output_image[pad_num:m - pad_num, pad_num:n - pad_num]  # 裁剪

    return dst_image


# src_image=[[1,2,3],[3,4,5],[7,8,9]]
# print(midfilter(src_image=src_image))


class Solution:
    def array_element_insert(self, array, array_length, element_num, element_insert):
        """
        :param array:输入数组
        :param array_length:最大长度
        :param element_num:当前元素个数
        :param element_insert:待插入的元素
        :return array:插入之后的数组
        """
        if len(array) == 0:
            return array.append(element_insert)
        if element_insert <= array[0]:
            array.insert(0, element_insert)
            return array
        array.append(element_insert)
        i = element_num - 1
        while i >= 0:
            if array[i + 1] < array[i]:
                array[i + 1], array[i] = array[i], array[i + 1]
                i -= 1
            else:
                break
        return array


array = [1, 2, 3, 5, 6, 8]

print(Solution().array_element_insert(array, 1000, 6, 9))

import numpy as np


def midfilter(src_image, w, h):
    """
    #均值滤波器实现
    :param src_image:输入图像
    :param h,w :输入图像高和宽
    :return dst_image:输出图像
    """
    filter_size = 3
    input_image = np.array(src_image)
    input_image_cp = np.copy(input_image)  # 输入图像的副本
    filter_template = np.ones((filter_size, filter_size))  # filter 模板
    pad_num = int((filter_size - 1) / 2)
    input_image_cp = np.pad(input_image_cp, (pad_num, pad_num), mode="constant", constant_values=0)
    m, n = input_image_cp.shape
    output_image = np.copy(input_image_cp)
    for i in range(pad_num, m - pad_num):
        for j in range(pad_num, n - pad_num):
            output_image[i, j] = np.sum(
                filter_template * input_image_cp[i - pad_num:i + pad_num + 1, j - pad_num:j + pad_num + 1]) / (
                                             filter_size ** 2)
    dst_image = output_image[pad_num:m - pad_num, pad_num:n - pad_num]
    return dst_image


src_image = [[1, 2, 3,4], [ 4, 5,6,4], [7, 8, 9,9]]
print(midfilter(src_image=src_image, w=3, h=3))
