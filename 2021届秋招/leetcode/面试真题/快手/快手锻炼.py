# N = int(input())
# distance = input().split()
# exp = input().split()
N=5
distance=[1,2,3,4,6,8]
exp=[1,2,3,4,5,4]


max_to_choose = []
for i in range(0, N):
    info = {'dist': int(distance[i]), 'exp': int(exp[i])}
    max_to_choose.append(info)
max_exp = sorted(max_to_choose, key=lambda info: info['exp'], reverse=True)  # 按照健身效果排序，由于排序保证是稳定的。所以健身效果相同时，距离大的在后面

max_dist = 0
kmax_save = 0
kmax_exp = []
save_index = 0
for i in range(0, N):
    if (i > 0):
        kmax_save = kmax_save + max_exp[i - 1]['exp']
        kmax_exp.append(kmax_save)
        if (max_exp[i - 1]['dist'] > max_dist):
            max_dist = max_exp[i - 1]['dist']
    else:
        kmax_exp.append(0)
    maxval = 0
    value = 0
    if (save_index <= i):
        for k in range(i, N):
            value = max_exp[k]['exp'] + max_exp[k]['dist'] * 2
            if (value > maxval):
                maxval = value
                save_index = k
    # 从剩下的里找出2d+V最大的的器材A
    if (max_dist < max_exp[save_index]['dist']):
        kmax_exp[i] = kmax_exp[i] + 2 * max_exp[save_index]['dist'] + max_exp[save_index]['exp']
    else:
        kmax_exp[i] = kmax_exp[i] + 2 * max_dist + max_exp[i]['exp']

for km in kmax_exp:
    print(km)