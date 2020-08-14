#include <bits/stdc++.h>
using namespace std;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif
struct event{
    int id;
    int time;
    int type;
    event(int T,int I,int typ){
        id=I;
        time = T;
        type=typ;
    }
};
bool cmp(pair<int,int> &fir,pair<int,int> &las){
    if(fir.first>las.first)return true;
    if(fir.first<las.first)return false;
    return fir.second<las.second;
}
void solve(){
    int cas;cin>>cas;
    while(cas--){
        int n;cin>>n;
        vector<event> arrmv;
        for(int i=0;i<n;i++){
            int a,b,c;cin>>a>>b>>c;
            arrmv.push_back({a,b,c});
        }
        stack<pair<int,event>> sta;
        vector<pair<int,int>> ret_mv;
        for(int i=0;i<n;i++){
            if(arrmv[i].type == 0){
                sta.push({0,arrmv[i]});
            }else{
                assert(sta.size());
                assert(arrmv[i].id == sta.top().second.id);
                ret_mv.push_back({arrmv[i].time - sta.top().second.time - sta.top().first,sta.top().second.id});
                int tmp_time = sta.top().second.time;
                sta.pop();
                if(sta.size()){
                    sta.top().first+=arrmv[i].time - tmp_time;
                }
            }
        }
        sort(ret_mv.begin(),ret_mv.end(),cmp);
        cout<<ret_mv[0].second<<endl;
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    solve();
	return 0;
}


"""
#include<iostream>
#include<stack>
using namespace std;

int main() {
        int T;
        cin >> T;
        for (int i = 0; i < T; i++) {
                stack<pair<int, int>> S;
                int N;
                cin >> N;
                int res = 0;
                int front_id = 0;
                int front = 0;
                int id = 0;
                for (int j = 0; j < N; j++) {
                        int t, e, s;
                        cin >> t >> e >> s;
                        if (S.empty()) front = 0;
                        if (s == 0) {
                                S.push(pair<int, int>(t, e));
                                front_id = e;
                        }
                        else {
                                int m = S.top().first;
                                int n = S.top().second;
                                S.pop();
                                if (front_id == e) {
                                        int k = t - m;
                                        if (k > res) {
                                                res = k;
                                                id = e;
                                        }
                                        front += t - m;
                                }
                                else {
                                        int k = t - m - front;
                                        if (k > res) {
                                                res = k;
                                                id = e;
                                        }
                                        front += k;
                                }
                        }
                }
                cout << id << endl;
        }

        return 0;
}



"""