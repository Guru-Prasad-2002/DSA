#include<bits/stdc++.h>
using namespace std;

// NOTE : By defalt ARRAYS are passed by values in c++,everything else like vectors and maps
// we need to explcitly specify & sign to pass by reference 

void doSomething(int &val){
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