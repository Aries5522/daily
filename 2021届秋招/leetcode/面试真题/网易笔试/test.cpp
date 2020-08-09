#include "bits/stdc++.h"

using namespace std;

void dfs(vector<int> &item,int index,int &min_value,int sumA,int sumB,int loss){
    if (index>=item.size()){
        if (sumA==sumB){
            min_value=min(min_value,loss);
        }
        return;
    }
    dfs(item,index+1,min_value,sumA+item[index],sumB,loss);
    dfs(item,index+1,min_value,sumA,item[index]+sumB,loss);
    dfs(item,index+1,min_value,sumA,sumB,loss+item[index]);
    







}