#include<bits/stdc++.h>
using namespace std;

int main(){

    // Binary Search
    // int a[]={1,2,3,4,5,7};
    // int n=sizeof(a)/sizeof(a[0]);
    // bool res=binary_search(a,a+n,2);
    // cout<<res<<endl;
    // res=binary_search(a,a+n,10);
    // cout<<res<<endl;

    vector<int> v={1,3,5,7};
    // LOWER BOUND - first occurence of element if it occurs or else position of element that is just greater than the current element
    cout<<lower_bound(v.begin(),v.end(),3)-v.begin()<<endl;
    cout<<lower_bound(v.begin(),v.end(),4)-v.begin()<<endl;
    // UPPER BOUND - Position of element the is greater than the element given as the parameter 
    cout<<upper_bound(v.begin(),v.end(),3)-v.begin()<<endl;
    cout<<upper_bound(v.begin(),v.end(),4)-v.begin()<<endl;
    return 0;

    // Syntax while using array
    //int ind=lower_bound(a,a+n,num)-a
}