
fun main(args:Array<String>){
  (1..999).map { 
    if( it%3 == 0  || it%5 == 0 ) it
    else 0
  }.sum().let { println(it) }
}
