"""
全排列 leetcode46

"""


def quanpailie(nums):
    res=[]
    path=[]
    size=len(nums)
    used=[False]*size
    def dfs(depth,nums,path,size,used,res):
        if depth==size:                       #终止条件
            res.append(path.copy())           #满足终止要干啥
            return                            #是否要返回
        for i in range(size):
            if not used[i]:
                used[i]=True
                path.append(nums[i])
                dfs(depth+1,nums,path,size,used,res)
                used[i]=False
                path.pop()
    dfs(0,nums,path,size,used,res)
    return res
print(quanpailie(nums=[1,2,3]))
