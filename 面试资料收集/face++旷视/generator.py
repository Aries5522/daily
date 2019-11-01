# generator_ex = (x*x for x in range(10))
# print(generator_ex)
# for i in generator_ex:
#     print(i)

def gen(max):
    n, a, b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return "done"
a=gen(10)
print(a)