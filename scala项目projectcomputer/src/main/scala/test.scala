import org.apache.spark.sql.SparkSession

object test {
  def main(args: Array[String]): Unit = {
    val sparkSession = SparkSession.builder().master("local").appName("wash")
      .enableHiveSupport().getOrCreate()
    sparkSession.sql("select * from ods.bike_info").show(5)
  }
}
