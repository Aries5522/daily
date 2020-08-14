#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    string str[3]={"147","369","258"};
    while(T--){
        vector<char> a[3];
        vector<bool> vis(3,false);
        for(int i=0;i<7;i++){
            string s;cin>>s;
            char c=s[1];
            if(c=='T') a[0].push_back(s[0]);
            else if(c=='B') a[1].push_back(s[0]);
            else a[2].push_back(s[0]);
        }
        int flag=1;
        for(int i=0;i<3;i++){
            if(a[i].size()>3 || a[i].empty()){
                cout<<"NO"<<endl;
                flag=0;
                break;
            }
            int f=0;
            for(int k=0;k<3;k++)
                if(!vis[k] && str[k].find(a[i][0])!=str[k].npos){
                    f=k;
                    vis[k]=true;
                    break;
                }
            for(int j=1;j<a[i].size();j++){
                if(str[f].find(a[i][j])==str[f].npos){
                    cout<<"NO"<<endl;
                    flag=0;
                    break;
                }
            }
        }
        if(flag) cout<<"YES"<<endl;
    }
    return 0;
}