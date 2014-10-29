#include<vector>
#include<set>
#include<iostream>
namespace Sieve{

std::set<long long> makePrimes(long long n){
  std::vector<bool> sieve;
  for(long long i = 0; i < n; ++i){
    sieve.push_back(true);
  }
  long long i = 2;
  while(i*i <= n){
    if(sieve[i] == true){
      long long j = i + i;
      while(j <= n){
        sieve[j] = false;
        j += i;
      }  
    }
    i += 1;
  }
  std::set<long long> primes;
  for(long long i = 2; i <= n; ++i){
    if(sieve[i] != *sieve.end()) primes.insert(i);
    /*if(i == 7 and sieve[i] != *sieve.end() ){
      std::cout << "sieve has, " << i << std::endl;
    }*/
  }
  return primes;
}

}
