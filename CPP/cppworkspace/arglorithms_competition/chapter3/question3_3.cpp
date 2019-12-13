////
//// Created by aries on 2019/10/9.
////
//
////习题3-3数数字(UVa1225)
//
//#include <bits/stdc++.h>
//
//using namespace std;
//
//int main(){
//    int T;
//    scanf("%d", &T);
//    while (T--)
//    {
//        string a;
//        string str;
//        int num[10]={0,0,0,0,0,0,0,0,0,0},l,n,c;
//        scanf("%d",&n);
//        for (int k=1;k<=n;k++)
//            str=str+to_string(k);
//        l=str.length();
//        for (int i = 0; i < l; i++) {
//            a=str[i];
//            c=stoi(a,0,10);
//            num[c]++;}
//        for (int j =0 ;j<10;j++)
//            printf("%d ",num[j]);
//    }
//    return 0;
//}