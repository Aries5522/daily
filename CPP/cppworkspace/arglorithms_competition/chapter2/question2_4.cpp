//
// Created by aries on 2019/9/25.
//

//subsequence

#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;
int  main(){
   int n,m;
   float sum=0;
   scanf("%d%d",&n,&m);
   for (int i=n;i<m+1;i++)
   {
       sum=sum+1/(pow(i,2));
   }
   cout<<fixed;
   cout<<setprecision(5)<<sum<<endl;
   printf("%.5f",sum);
   return 0;
}

