
def reverse(x):
    return (int((x+0.1)//abs(x+0.1)) * int(str(abs(x))[::-1])) if -1<<31 < ((x+0.1)//abs(x+0.1) * int(str(abs(x))[::-1])) < (1<<31)-1 else 0

print(reverse(-1233345))
