def P(n=100000):
    for i in range(1,n):
        print(1-0.5**(i-1))
print(P())