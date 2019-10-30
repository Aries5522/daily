sys = {'name': '1',
       'age': '2',
       'gender': '3'}

#对键排序
#  单独打印出排序后的key值
new_sys = sorted(sys)
print(new_sys)

# 根据key的升序排列，把key value都打印出来
new_sys1 = sorted(sys.items(), key=lambda d: d[0], reverse=False)
print(new_sys1)


#对值排序
# 单独打印出排序后的value值
new_sys1 = sorted(sys.values())
print(new_sys1)

# 打印出根据value排序后的键值对的具体值
new_sys2 = sorted(sys.items(),  key=lambda d: d[1], reverse=False)
print(new_sys2)
