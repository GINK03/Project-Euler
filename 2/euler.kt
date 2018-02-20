
fun main(args:Array<String>) { 
  val m = mutableListOf(1, 2)
  
  while( m.last() < 4000000 ) {
    val s = m.size
    val n = m[s-2] + m[s-1]
    if( n > 4000000 ) break
    m.add(n)
  }
  println(m.filter { it%2 == 0 }.sum() )
 }
