#include<bits/stdc++.h>
using namespace std;

void pairr(){
    pair<int,int> p={1,3};
    cout<<p.first<<"\t"<<p.second<<endl;
}
void explainVector(){
    // Implemented using Singly LL in Backend 
    vector<int> v;
    v.push_back(5);
    v.emplace_back(10);//Genreally emplace_back is faster than push_back
    v.push_back(15);
    v.push_back(20);
    // for(vector<int>:: iterator it=v.begin();it!=v.end();it++){
    //     cout<<*(it)<<endl;
    // }
    // for(auto it=v.begin();it!=v.end();it++){
    //     cout<<*(it)<<endl;
    // }
    // for Each loop
    // for(auto it:v){
    //     cout<<it<<endl;
    // }
    v.erase(v.begin()+2,v.end());
    for(auto it:v){
        cout<<it<<endl;
    }
    v.insert(v.end(),100);
    for(auto it:v){
        cout<<it<<endl;
    }
    cout<<v.size()<<endl;
    for(auto it:v){
        cout<<it<<endl;
    }
    // POP BACK REMOVES THE LAST ELEMENT THAT IS INSERTED
    v.pop_back();
    cout<<"AFTER POP BACK"<<endl;
    for(auto it:v){
        cout<<it<<endl;
    }
    v.clear();//Clears the vector
    // v.empty() - returns true if vector is empty else false
}
void explainlist(){
    // Implemented using Doubly LL in Backend 
    // similar to vector but there is push front and emplace front available 
    list<int> ls;
    ls.push_back(1);
    ls.emplace_back(2);
    for(auto it:ls){
        cout<<it<<"\t";
    }    
    cout<<endl;
    ls.push_front(3);
    ls.emplace_front(4);
    for(auto it:ls){
        cout<<it<<"\t";
    }   
}

void explainStack(){
// All operations happen in big oh of 1 time complexity...constant time complexity
    stack<int> st;
    st.push(1);
    st.push(2);
    st.push(3);
    while(st.size()!=0){
        cout<<st.top()<<"\t";
        st.pop();
    }
    cout<<endl;
}

void explainSet(){
    //operations happen in logarithmic time complexity 
    set<int> st;
    //unique and sorted;
    st.insert(1);
    st.insert(1);
    st.insert(2);
    st.insert(3);
    for(auto it1:st){
        cout<<it1<<"\t";
    }
    cout<<endl;
    set<int>::iterator it=st.find(2);
    cout<<*it<<" Hello";
    cout<<endl;
    st.erase(it);//Erasing with help of iterator
    st.erase(1);//erasing with the help of value
    for(auto it2:st){
        cout<<it2<<"\t";
    }
}

void explainmap(){
    map<int,int> mpp;
    mpp[1]=1;
    mpp.insert({3,3});
    for(auto it:mpp){
        cout<<it.first<<" "<<it.second<<endl;
    }
    auto it=mpp.find(1);
}

int main(){
    // pairr();
    // explainVector();
    // explainlist();
    // explainStack();
    // explainSet();
    explainmap();
    return 0;
}