
// //Created by aries on 2019/9/26.




// #include <iostream>
// #include <string.h>
// #define maxn 8
// using namespace std;
// char chars[maxn];

// int main(){
//    int T;
//    scanf("%d",&T);
//    while(T--)
//    {
//    scanf("%s",chars);
//    int sum=0,k1=1;
//    cout<<sizeof(chars)<<endl;
//    cout<<strlen(chars)<<endl;

//    for (int i=0 ; i< strlen(chars);i++)
//        {   if (chars[i]=='O')
//            {sum=sum+k1;k1++;}
//            else if (chars[i]=='X')
//            {k1=1;}
//        }
//    cout<<sum<<endl;}
//    return 0;
// }

// #include"stdio.h"
// #include"string.h"
// #define maxn 80
// int main()
// {
//    int T,i,m,sum,c;
//    char s[maxn];
//    scanf("%d",&T);
//    while(T--)
//    {
//        scanf("%s",s);
//        m=strlen(s);
//        sum=0;
//        c=0;
//        for(i=0; i<m; i++)
//            if(s[i]=='O')
//            {
//                c++;
//                sum+=c;
//            }
//            else c=0;
//        printf("%d\n",sum);
//    }
//    return 0;
// }