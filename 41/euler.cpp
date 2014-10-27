// Hack around stdlib bug with C++14.
// End hack.
#include<iostream>
#include<list>
#include<vector>
#include<string>
#include<set>
#include<algorithm>
#include<boost/lexical_cast.hpp>
using namespace boost;
using namespace std;
set<long long> primeVector(long long n){
  vector<bool> sieve;
  for(long long i = 0; i <= n; ++i) sieve.push_back(true);
  long long i = 2;
  while( i*i <= n ){
    if(sieve[i]){
      long long j = i+i;
      while(j <= n){
        sieve[j] = false;
        j += i;
      }
    }
    i += 1;
  }
  set<long long> res;
  for(long long i = 0; i <= n; ++i){
    if(sieve[i] and i >= 2 and i >= 99999999) { //<- 8digit over
      res.insert(i);
    }
  }
  return res;
}

int main(){
  //auto primes = primeVector(999999999);
  auto primes = primeVector(999999999);
  vector<long long> result;
  std::string s = "123456789";
  //string base = "123456789";
  do{
    if(primes.find(lexical_cast<long long>(s)) != primes.end()){
      cout << s << ", is prime and permutation" << endl;
      result.push_back(lexical_cast<long long>(s));
    }
  }while(std::next_permutation(s.begin(), s.end()));
  //sort(result.begin(), result.end());
  //cout <<  "anser is," << result.back() << endl;
  return 0;
}
