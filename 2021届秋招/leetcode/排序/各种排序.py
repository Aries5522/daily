def merge_sort(list0):
    import math
    if len(list0)<2:
        return list0
    mid=math.floor(len(list0)/2)
    left,right=list0[0:mid],list0[mid:]
    return merge(merge_sort(left),merge_sort(right))
def merge(list1,list2):
    list3=[]
    while list1!=[] and list2!=[]:
        if list1[0]<list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    while list1!=[]:
        list3.append(list1.pop(0))
    while list2!=[]:
        list3.append(list2.pop(0))
    return list3

numbs=[3,1,4,2,33,5,8,42,5,41,7,6,6,12,134,44,6,9,1,2,3,2,1]
print("归并结果为:{}".format(merge_sort(numbs)))

quick_sort = lambda array: array if len(array) <= 1 else \
    quick_sort([item for item in array[1:] if item <= array[0]]) + \
    [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

def quick(array):
    if len(array)<=1:
        return array
    else:
        left=[item for item in array[1:] if item<=array[0]]
        right=[item for item in array[1:] if item>array[0]]
        return quick(left)+[array[0]]+quick(right)

print("快排结果为:{}".format(quick(numbs)))