#include<bits/stdc++.h>
using namespace std;
void doSomething(int val){
    val+=5;
    cout<<val<<endl;
}
int main(){
    int val=500;
    cout<<val<<endl;
    doSomething(val);
    cout<<val<<endl;
    return 0;
}