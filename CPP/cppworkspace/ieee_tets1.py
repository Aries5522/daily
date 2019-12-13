import numpy
import scipy

# k = input("k")
# j= input("j")
n=0
def dlt(k,j,n):
    if k<1 or j<1 or (k+j)<3:
        return n
    if k>=j:
        return dlt(k-2,j-1,n+1)
    else:

        return dlt(k-1,j-2,n+1)



if __name__ == '__main__':
    print(dlt(15,3,0))