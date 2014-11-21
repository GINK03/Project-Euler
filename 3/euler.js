

TGT_NUM = 600851475143;

var primeArray = [];
for(var i = 2; i<=TGT_NUM; ++i){
  if(TGT_NUM%i == 0){
    primeArray.push(i);
    TGT_NUM /= i;
  }
}

console.log(primeArray.pop());
