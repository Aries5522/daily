
//Created by aries on 2019/9/25.


//daffodil(水仙花数)

#include <iostream>
#include <math.h>
using namespace std;
int  main(){

   for (int i=100;i<=999;i++)
   {
       int A,B,C;
       A=i/100;B=i/10%10;C=i%10;
       if (i==pow(A,3)+pow(B,3)+pow(C,3))
           cout<<i<<endl;
   }

}


//out:
//153
//370
//371
//407