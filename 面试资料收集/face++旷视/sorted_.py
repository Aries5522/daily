
# 冒泡排序的思想：就是每次比较相邻的两个书，如果前面的比
# 后面的大，那么交换两个数，关键点在于，一次循环之后，
# 最大值必然放到最后一个去了，那么我men第二次循环的次数就
# 少了一个，如同程序所看。直到循环结束。冒泡排序是一种
# 稳定的排序
# numbs=[1,3,4,2]

def bubble_sort(numbs):
    for i in range (len(numbs)-1):
        for j in range (len(numbs)-i-1):
            if numbs[j]>numbs[j+1]:
                numbs[j],numbs[j+1]=numbs[j+1],numbs[j]
    return numbs

numbs=[3,1,4,2,33,5,8,42,5,41,7,6,6,12,134,44,6,9,1,2,3,2,1]
print("冒泡排序结果：")
print(bubble_sort(numbs))



##选择排序的思路：取第一个值为最小值，然后遍历后面所有值
#如果碰到更小值就让min为这个更小的，一次遍历后，找到最小值
#和第一个位置元素互换位置，第二次，从第二个元素开始，一样操作，
#直到整个列表遍历。时间复杂度(O(n^2))
def selection_sort(numbs):
    for i in range(len(numbs)-1):
        min_index=i 
        for j in range (i+1,len(numbs)-1):
            if numbs[j]<numbs[min_index]:
                min_index=j
        numbs[min_index],numbs[i]=numbs[i],numbs[min_index]

    return numbs
print("选择排序结果：")
print(selection_sort(numbs))


#插入排序的思想是：
#从第一个元素开始，该元素可以认为已经被排序；
#取出下一个元素，在已经排序的元素序列中从后向前扫描；
#如果该元素（已排序）大于新元素，将该元素移到下一位置；
#重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
#将新元素插入到该位置后；
#重复步骤2~5。
def insertion_sort(numbs):
    for i in range(1,len(numbs)-1):
        pre_index=i-1
        current=numbs[i]
        while pre_index>=0 and numbs[pre_index]>current:
            numbs[pre_index+1]=numbs[pre_index]
            pre_index-=1
        numbs[pre_index+1]=current
    return numbs

print("插入排序结果：")

print(insertion_sort(numbs))

## 希尔排序
"""

"""

def hear_sort(numbs):
    pass

"""
归并排序
 O(nlogn)
 额外空间


 思路是分组排序,比如有两个已经排好序的数组,
 那么对他使用merge函数进行排序,那么归并排序
 实际就是一直采用二分,将大的序列转为短的序列
 递归进行排序.
 #这一种排序是递归加二分的思想
"""
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

print("归并排序结果：")
print(merge_sort(numbs))


"""
快速排序
以第一个元素借界限,把剩下的元素分为两组
小的放左边,大的放右边
对于小的同样如此排序,对大的也是如此,递归下去
O(nlogn)

"""

def quick(array):
    if len(array)<=1:
        return array
    else:
        left=[item for item in array[1:] if item<=array[0]]
        right=[item for item in array[1:] if item>array[0]]
        return quick(left)+[array[0]]+quick(right)

quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
print("快速排序一行代码结果：")
print(quick_sort(numbs))
print("快速排序代码结果：")
print(quick(numbs))


#这一种排序是递归加二分的思想

a=map(lambda x: "pic_"+str(x)+".png",range(9))

b=[ "pic_%d.png" % (i) for i in range(20)]

print(b)