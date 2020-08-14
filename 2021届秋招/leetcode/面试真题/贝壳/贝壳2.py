# while True:
#     try:
#         a, b = map(int, input().split())
#         if b == a:
#             print("inf")
#             break
#         elif b > a:
#             print(0)
#             break
#         res = set()
#         c=a-b
#         i=1
#         while i<c:
#             if c % i == 0:
#                 if i > b:
#                     res.add(i)
#                 if c // i > b:
#                     res.add(c // i)
#                 c //= i
#             i+=1
#         print(len(res))
#         # for i in range(b + 1, a+1, 1):
#         #     if a % i == b:
#         #         res += 1
#         # print(res)
#     except:
#         break
# a=2
# b=3
# def f():
#     if a == b:
#         print('inf')
#         return
#     c = a - b
#     i = 1
#     res = set()
#     while i < c:
#         if c % i == 0:
#             if i > b:
#                 res.add(i)
#             if c // i > b:
#                 res.add(c // i)
#             c //= i
#         i += 1
#     print(len(res))
#
# f()


#
#
#
#
while True:
    try:
        a, b = map(int, input().split())
        def f():
            if a == b:
                print('inf')
                return
            c = a - b
            i = 1
            # res = set()
            d = c
            cnt = 0
            while i < d:
                if c % i == 0:
                    if i > b:
                        # res.add(i)
                        cnt += 1
                    if c // i > b and c // i != i:
                        # res.add(c // i)
                        cnt += 1
                    d = c // i
                i += 1
            print(cnt)
        f()
    except:
        break