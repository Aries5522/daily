////
//// Created by aries on 2019/10/9.
////
//
//#include <iostream>
//#include <string.h>
//#include <ctype.h>
//#define maxn 1000
//using namespace std;
//
//int main()
//{
//    int T;
//    scanf("%d",&T);
//    while(T--) {
//        int m=0,l;
//        char fenzishi[maxn];
//        double sum=0,a=0,b=1;
//        scanf("%s",fenzishi);
//        l=strlen(fenzishi);
//        for (int i=0;i<l;i++)
//        {
//            if (isalpha(fenzishi[i])){
//                sum=sum+a*b;
//                b=1;
//                if (fenzishi[i]=='C') a=12.01;
//                else if (fenzishi[i]=='H') a=1.008;
//                else if (fenzishi[i]=='O') a=16.00;
//                else if (fenzishi[i]=='N') a=14.01;
//            }
//            else if(isdigit(fenzishi[i])) //判断是否数字
//            {
//                if(isdigit(fenzishi[i-1]))  //如果前一位也是数字
//                    b=b*10+fenzishi[i]-'0';
//                else                 //如果前一位不是数字
//                    b=fenzishi[i]-'0';
//            }
//        }
//        printf("%.3f\n",sum+a*b);
//    }
//    return 0;
//}