def bubble_sort(numbs):
    for i in range (len(numbs)-1):
        for j in range (len(numbs)-i-1):
            if numbs[j]>numbs[j+1]:
                numbs[j],numbs[j+1]=numbs[j+1],numbs[j]
    return numbs


# 冒泡排序的思想：就是每次比较相邻的两个书，如果前面的比
# 后面的大，那么交换两个数，关键点在于，一次循环之后，
# 最大值必然放到最后一个去了，那么我men第二次循环的次数就
# 少了一个，如同程序所看。直到循环结束。冒泡排序是一种
# 稳定的排序
# numbs=[1,3,4,2]
numbs=[3,1,4,2,33,5,8,42,5,41,7,6,6,12,134,44,6,9,1,2,3,2,1]
print("冒泡排序结果：")
print(bubble_sort(numbs))

def selection_sort(numbs):
    for i in range(len(numbs)-1):
        min =numbs[i] 
        for j in range (i+1,len(numbs)-1):
            if numbs[j]<min:
                numbs[j],min=min,numbs[j]
    return numbs
##选择排序的思路：取第一个值为最小值，然后遍历后面所有值
#如果碰到更小值就让min为这个更小的，一次遍历后，找到最小值
#和第一个位置元素互换位置，第二次，从第二个元素开始，一样操作，
#直到整个列表遍历。时间复杂度(O(n^2))
print("选择排序结果：")
print(selection_sort(numbs))

def insertion_sort(numbs):
    for i in range(1,len(numbs)-1):
        for j in range(0,i):
            if numbs[i]<numbs[j]:
                numbs[j],numbs[i]=numbs[i],numbs[j]
    return numbs
print("插入排序结果：")

print(insertion_sort(numbs))

#插入排序的思想是：
#从第一个元素开始，该元素可以认为已经被排序；
#取出下一个元素，在已经排序的元素序列中从后向前扫描；
#如果该元素（已排序）大于新元素，将该元素移到下一位置；
#重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
#将新元素插入到该位置后；
#重复步骤2~5。

def quick_sort(numbs):
    pass

def merge_sort(list1,list2):
    list3=[]
    i=0
    j=0
    # for i in range(len(list1)):
    #     for j in range(len(list2)):
    while ((i+j)<(len(list1)+len(list2)-1)):
        if list1[i]<list2[j]:
            list3.append(list1[i])
            i=i+1
        else:
            list3.append(list2[j])
            j=j+1
    return list3

list1=[1,3,4,5,6,10]
list2=[2,5,8,12]
print("归并排序结果：")
print(merge_sort(list1,list2))


quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
print("快速排序结果：")
print(quick_sort(numbs))





def quick_sorted(array,l,r):
    if l < r:
        q=partition(array,l,r)
        quick_sorted(array,l,q-1)
        quick_sorted(array,q+1,r)
def partition(array,l,r-1):
    i=l-1
    x=array[r-1]
    for j in range(l,r-1):
        if array[j]<=x:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[r-1]=array[r],array[i+1]
    return i+1
        
    #着一种排序是递归加二分的思想
quick_sorted(array=numbs,l=0,r=len(numbs))
print(numbs)
    


a=map(lambda x: "pic_"+str(x)+".png",range(9))
b=[ "pic_%d.png" % (i) for i in range(20)]
print(b)