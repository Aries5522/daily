data = [[1, 'B'], [1, 'A'], [2, 'A'], [0, 'B'], [0, 'a']]
#利用参数key来规定排序的规则
result = sorted(data,key=lambda x:(x[0]))

print(data) #结果为 [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
print(result) #结果为 [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]
