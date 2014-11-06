#include<string>
#include<vector>
#include<boost/lexical_cast.hpp>
#include<boost/algorithm/string.hpp>
using namespace std;
template<typename T>
string str(T t){
  string buff = boost::lexical_cast<string>(t);
  return buff;
}

vector<string> split_with(const string& str, const string& splitter){
  vector<string> res;
  boost::algorithm::split(res, str, boost::is_any_of(splitter));
  return res;
}
