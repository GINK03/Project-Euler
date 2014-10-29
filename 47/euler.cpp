#include<string>
#include<iostream>
#include<tuple>
#include<set>
#include"../cpplib/makeSievePrimes.cpp"
#include<boost/lexical_cast.hpp>
using namespace boost;
using namespace std;
template<class Long, class Primes>
std::tuple<vector<Long>,Long> dividor(const Long l, const Primes& primes){
  vector<Long> vec;
  Long ltgt = l;
  Long buff = 1;
  for(auto prime : primes){
    while(true){
      if(prime > l) break;
      if(ltgt%prime==0){ 
        vec.push_back(prime);
        buff*= prime;
        ltgt /= prime;
      }
      else break;
    }
  }
  return std::make_tuple(vec, buff);
}
template<class Vec>
string mapToSome(const Vec& vec){
  string res;
  for(auto v: vec)
    res += to_string(v) + ",";
  return res;
}
template<class T>
long long reduce(const T& vec){
  long long buff = 1;
  for(auto v : vec)
    buff *= v;
  return buff; 
}
template<class T>
int countPrime(const T& vec){
  set<long long> setBuff;
  for(auto v: vec){
    setBuff.insert(v);
  } 
  return setBuff.size();
}
class DataHolder{
  public:
  vector<long long> index;
  set<long long> primes;
  void pushIndex(long long i){
    if( index.size() != 0 and index.back() == i-1){
      index.push_back(i);
    }
    else{
      //dispose index
      index = vector<long long>();
      index.push_back(i);
    }
  }
  int getIndexSize(){
    return index.size();
  }
  int getFirstEntry(){
    return *index.begin();
  }
};

template<class Vec>
void isSequential(long long i, const Vec& vec){
}

static int PRIMENUM = 4;
int main(){
  auto dataHolder = DataHolder();
  set<long long> primes = Sieve::makePrimes(100000);
  for(long long i = 1; true; i++){
    auto t = dividor(i, primes); 
    if(reduce(get<0>(t)) == i) {
      if( 4 == countPrime(get<0>(t)) ){
        dataHolder.pushIndex(i);
        if(dataHolder.getIndexSize() > 3){
          cout << "target" << i << ", first " << dataHolder.getFirstEntry() <<",primeNum " << countPrime(get<0>(t)) << ", prime-set, " << mapToSome(get<0>(t)) << endl;
          break;
        }
      }
      // toSet
    }
    else{
    }
  }
}




