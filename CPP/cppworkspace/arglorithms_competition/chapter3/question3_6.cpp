//
// Created by aries on 2019/10/9.
//

#include <bits/stdc++.h>

using namespace std;

//int main()
//{
//    int r,c;
//    char s[r][c];
//    cin>>r;cin>>c;
//}

void swap(int *a,int *b)
{
    int t=*a;*a=*b;*b=t;
}

int sum(int a[],int n)
{
    int sum=0;
    for (int i=0;i<n;i++)
        sum=sum+a[i];
    return sum;
}

int main (){
    int a=3,b=4;
    swap(a,b);
    cout<<a<<b<<endl;
    int k[4]={1,2,3,4},sum1;
    sum1=sum(k,4);
    cout<<sum1<<endl;
    return 0;
}