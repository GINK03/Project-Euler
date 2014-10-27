#include<set>
#undef _GLIBCXX_HAVE_GETS 
#include<iostream>
#include<initializer_list>
#include<vector>
#include<algorithm>
#include"../cpplib/next_combination.hpp"
//using namespace std;
long long generator(){
  static auto n = 0;
  while(true){
    n++;
    return n*(3*n-1)/2; 
  }
}

template<class T>
auto combine(T& v){
  T backup = T(v); 
  do{
    auto e1 = *v.begin();
    auto e2 = *(v.begin()+1);
    if(find(backup.begin(), backup.end(), (e1 + e2) ) != backup.end()){
      if(find(backup.begin(), backup.end(), abs(e1 - e2) ) != backup.end()){
        cout << "match" << (e1 + e2) << "," << abs(e1 - e2)<< endl;
        return true;
      }
    }
  }while(next_permutation(v.begin(), v.end()));
  return false;
}


int main(){
  auto i = 0;
  vector<long long> v;
  while( (i = generator()) and i > 0){
    v.push_back(i);
    if (v.size() > 2){
      if(combine(v)) break;
    }
    cout << "iter, " << i << endl;
  }
}
