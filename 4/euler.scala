


object main{
  def check(line: String):Boolean = {
    val carray  = line.toCharArray
    val len     = carray.length/2
    val heads   = carray.take(len)
    val tail    = carray.takeRight(len).reverse
    if(heads.mkString == tail.mkString)
      return true
    else
      return false
  }
  var source = List[Long]()
  var result = List[Long]()
  def main(args: Array[String]){
    for(i <- 100 to 999){
      source = i :: source
    }
    source.combinations(2).foreach( e => {
      val raw = e.reduce(_ * _).toString()
      if( check(raw) ){
        result = raw.toInt :: result
      }
    })
    println("ans," + result.sorted.takeRight(1).toString())
  }
}
