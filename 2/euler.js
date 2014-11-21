

var MAX = 4000000

var fib = {
  head: 1,
  tail: 0,
  inc: function(){
    var temp = this.head;
    this.head = this.head + this.tail;
    this.tail = temp;
  },
}

var result = 0;
while(true){
  //lconsole.log(fib.head, fib.tail);
  if(fib.head > MAX) break;
  if(fib.head%2 == 0) result += fib.head;
  fib.inc();
}
console.log('result,', result);
