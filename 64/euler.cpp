#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include"./base.cpp"
#include<sstream>
#include<regex>
using namespace std;

class ROOT{
  public:
  int index;
  string near_fomula;
  int iter_num;
  ROOT(int index)
    :index(index), near_fomula(""), iter_num(0){
    }
};
template<typename R>
string generate_fomula(R& r){
  if(r.iter_num == 0){
    stringstream stream;
    stream << str(sqrt(r.index)).at(0) << "+ROOT(" << to_string(r.index) << ")-" << str(sqrt(r.index)).at(0);
    r.iter_num += 1;
    stringstream stream2;
    
    stream2 << "ROOT(" << to_string(r.index) << ")-" << str(sqrt(r.index)).at(0);
    r.near_fomula = stream2.str();
    return stream.str();
  }
  //inverce mozi
  cout << "temp fomula = " << r.near_fomula << endl;
  regex pat("(.*?)"); 
  smatch m;
  while(regex_search(r.near_fomula, m, pat) ){
    for(auto s:m)
      cout << "match = " << s << endl;
  }
  return "";
}

int main(){
  auto root = ROOT(23);
  //cout << "resutl = " << generate_fomula(root) << endl;
  //generate_fomula(root);
}
