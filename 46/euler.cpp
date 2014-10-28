#include"../cpplib/makeSievePrimes.cpp"

#include<iostream>
#include<cmath>
using namespace std;

template<class Primes>
bool isOddComposite(long long n, Primes primes){
  if(n%2 == 0) return false;
  if(primes.find(n) != primes.end()) return false;
  for(long long i = 3; i < n; i+= 2){
    if(n%i == 0){
      //cout << "base," << n << " divite by " << i << endl;
      return true;  
    }  
  }
  return false;
}
template<class Primes>
bool isGoldbach(long long n, Primes primes){
    for(long long i = 1; i < n; i+=1){
      for(auto prime : primes){
        long long eval = n - prime;
        if (eval < 0) break;
        double intpart;
        std::modf(sqrt(eval/2), &intpart);
        //cout << "prime," << prime << " eval," << eval << " intpart, " << intpart << "sqrt"<< sqrt(eval/2)<< endl;
        if(intpart == sqrt(eval/2) and eval+prime == n){
          cout << "Goldbach," << n <<" sqrt, "<< sqrt(eval/2) << " pow(raw)," << eval << ",prime " << prime << ", intpart(sqrt) " << intpart << ",target " << i <<endl;
          return true;
        }
    }
  }
  return false;
}
int main(){
  auto primes = Sieve::makePrimes(1000000);
  for(long long i = 2; i < 1000000; ++i){
    if(isOddComposite(i, primes)){
      //cout << "oddComposite" << i << endl;
      if(not isGoldbach(i, primes)){
        cout << "result," << i <<endl;
        break;
      }
    }
    if(i%100 == 0)
      cout << "iter,"<< i <<endl;
  }
  /*for(auto p : primes){
    cout << p << endl;
  }*/
  return 0;
};

