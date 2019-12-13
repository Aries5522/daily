//
// Created by aries on 2019/9/12.
//
#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <cmath>
#include "hello_world.h"
using namespace std; //命名空间
//
//int main() {
//    cout << "hello world!" << endl;
//    cout<< INT8_MAX<<endl;
//    printf("hello world!");
//    int name=8;
//    cout<<name<<endl;
//    return 0;
//}

/*
int main() {
    int salary1 = 20;
    int salary2 = 25;
    cout << "小明的月薪是:" << salary1 << endl;
    printf("小明的月薪是：%d", salary1);
    float num = 123465.211566;
    cout << num << endl; //print 8 位数，float的精度不高少用
}
 */
/*
int main()
{
    //已知圆柱体的高，求圆柱体的体积
    const float  pi=3.14f;
    float r=4.5f;
    float h=90.0f;
    double volume=pi*pow(r,2)*h;
    cout<<"体积是："<<volume<<endl;
}
*/
#include <iomanip>

//int main() {
//    cin.get();
//    getchar(); //得到用户输入的单个字符
//
//    //输出double类型的数据
//    //控制输出精度
//    //第一步首先强制以小数的方式显示
//    cout << fixed;
//    //第二步控制输出的精度小数位后面2位
//    cout << setprecision(2);
//
//    double doubelnum = 1000.0 / 3.0;
//    cout << "|" << setw(8) << doubelnum << "|" << endl;
//}



//int main() {
//    cout << sizeof(double) <<
//         endl;
//    cout << sizeof(long double) <<
//         endl;
//    cout << sizeof(3.14f) <<
//         endl;
//    float numFLoat=10/3.0;
//    double numDouble=10/3.0;
//    cout<<fixed;
//    cout<<setprecision(2);
//    cout<<numFLoat*100000000<<endl;
//    cout<<numDouble*100000000
//    <<endl;


//    cout<<"\a"<<endl;
//    int num;
//    char ch;
//    char ch1, ch2, ch3;
//    cout << "请输入一个数字:" << endl;
//    cin >> num;
//    ch1 = cin.get();
//    ch2 = cin.get();
//    ch3 = cin.get();
//    cout << num << endl;
//    cout << "\t" << ch1 << "\t" << ch2 << "\t" << ch3
//    << endl;


//    string str="你好我是";
//    cout<<str<<endl;
//    //给类型起别名
//    typedef int zhengxing;
//    zhengxing num=20;
//    int num1=20;


//    double attack1 = 225;
//    double attack2 = 235;
//    double attack3 = 245;
//    int num1 = 5, num2 = 2;
//    double num3 = num1 / num2; //计算时候从右边到左边所以先等于2之后赋值给num3
//    cout << num3 << endl;
//面向过程:机械形式的思维
//握手（a和b）
//面向对象，一种管理代码的方式
//a.握手()
//b.握手()


//逻辑运算符
// “&& ” 与运算
// “||” 或运算
// “！”  非运算

//位运算符（先转为8位二进制数再按位操作）
//按照位与运算“&”
//按照位或运算“|”
//按照位非运算“~”
//按位异或“^”
//左移“<<”  例如2<<3,2转换为2二进制后左移三位，（通常运用在2的倍数中）在cout中的情况，cout<<3;运算符重载
//cout<<(2<<3)<<endl;//2*2^3,a<<n=a*2^n
//右移“>>”  空位补零

//sizeof()或者数据类型占用字节位数

//运算符优先级
//单目运算符  ~ ! ++ -- sizeof这些优先级较高
//剩下从高到低是
//算术运算符
//关系运算符
//逻辑运算符
//赋值运算符
//三元运算符
//int num= 5>6 ? 10:12;
//cout<<num<<endl;

//    (先判断5是否大于6，然后按照这个给num赋值)
//int main(){
//int a=1,b=10;
//do{
//
//    b-=a;
//    a++;
//
//}while(b--<0);
// cout<<b<<endl;
//
// //while 和do while执行顺序不一样
//
//// for (表达式1;表达式2;表达式3;)
////    {}
//
////表达式1：循环变量初值
////表达式2：循环变量极值
////表达式3：循环方式，如i++
//const  int N=20;
//
//for (int i =0;i<20;i++)
//{
//    cout<<i<<endl;
//
//}
//}
//
//int  main()
//{
//
//
//
//}

