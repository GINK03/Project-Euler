





object main{
  def check(line: String){
    val carray  = line.toCharArray
    val len     = carray.length/2
    val heads   = carray.take(len)
    val tail    = carray.takeRight(len)
    println(heads.mkString + " " + tail.mkString)
    return true
  }
  var source = List[Long](1,2,3)
  def main(args: Array[String]){
    for(i <- 100 to 999){
      source = i :: source
    }
    source.combinations(2).foreach( e => {
      val raw = e.reduce(_ * _).toString()
      check(raw)
      println(raw)
    })
    println("Hello World")
  }
}
