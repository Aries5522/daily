class Solution:
    def bool_cal(self, s):
        label = []
        data = []
        dict_ = {"t": True, "f": False}
        new_dict = {v: k for (k, v) in dict_.items()}
        n = len(s)
        nums = ["t", "f", "("]
        # print(new_dict)
        def cal():
            if label and len(data) >= 2:
                k1 = data.pop()
                label_i = label.pop()
                if label_i == "!":
                    k1 = new_dict[not dict_[k1]]
                else:
                    while data and data[-1] in ["t", "f"]:
                        temp = data.pop()
                        if label_i == "&":
                            k1 = new_dict[dict_[k1] and dict_[temp]]
                        elif label_i == "|":
                            k1 = new_dict[dict_[k1] or dict_[temp]]
                data.append(k1)
        for i in range(n):
            if s[i] in ["!", "&", "|"]:
                label.append(s[i])
            elif s[i] in nums:
                data.append(s[i])
            elif s[i] == ")":
                cal()
                del data[-2]
            else:
                pass
        return data[0]


print(Solution().bool_cal(s="!(|(t,f,&(t,f,t),!(t)))"))
