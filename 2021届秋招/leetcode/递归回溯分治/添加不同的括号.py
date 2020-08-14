class Sulotion:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, char in enumerate(input):
            if char in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        if char == "+":
                            res.append(l + r)
                        elif char == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


print(Sulotion().diffWaysToCompute("2-1-1"))
