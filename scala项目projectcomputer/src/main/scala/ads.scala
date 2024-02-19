//package org.expmale

import com.huaban.analysis.jieba.JiebaSegmenter
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.{DataFrame, SaveMode, SparkSession}

import java.util.Properties
import scala.util.matching.Regex

object ads {
  def main(args: Array[String]): Unit = {
    val prop = new Properties()
    prop.setProperty("user", "root")
    prop.setProperty("password", "123456")

    val sparkSession = SparkSession.builder().master("local").appName("bike")
      .enableHiveSupport().getOrCreate()
    year_count_fun(sparkSession)
    //      weathersit_count_fun(sparkSession)
    //    comment_fields(sparkSession)
    //    brand_count_fun(sparkSession)
    //    price_count_fun(sparkSession)
    //    self_support_count_fun(sparkSession)
    comment_day_avg(sparkSession)
    //    avg_score(sparkSession)
    //    comment_day_count(sparkSession)
    // comment
    // sparkSession.sql("select * from wash_comment").show(5)
  }

  //  // 品牌统计
  def brand_count_fun(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select case " +
      "when season = '2' then '春天' " +
      "when season = '3' then '夏天' " +
      "when season = '4' then '秋天' " +
      "when season = '1' then '冬天' " +
      "end season from ods.bike_info").createOrReplaceTempView("s_1")
    sparkSession.sql("select season,count(season) from s_1 group by season")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "season")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }

  def weathersit_count_fun(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select case " +
      "when weathersit = '2' then '雾' " +
      "when weathersit = '3' then '小雪' " +
      "when weathersit = '4' then '大雨' " +
      "when weathersit = '1' then '晴' " +
      "end weathersit from ods.bike_info").createOrReplaceTempView("s_1")
    sparkSession.sql("select weathersit,count(weathersit) from s_1 group by weathersit")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "weathersit")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }

  // 统计
  def price_count_fun(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select cnt, case " +
      "when cnt<=1000 then '1k以下' " +
      "when cnt<=2000 then '1k-2k' " +
      "when cnt<=3000 then '2k-3k' " +
      "when cnt<=4000 then '3k-4k' " +
      "when cnt<=5000 then '4k-5k' " +
      "when cnt<=6000 then '5k-6k' " +
      "when cnt<=7000 then '6k-7k' " +
      "when cnt<=8000 then '7k-8k' " +
      "else '8k以上' end cnt_section " +
      "from ods.bike_info"
    ).createOrReplaceTempView("cnt")
    val cnt_count: DataFrame = sparkSession.sql("select cnt_section,count(cnt_section) count from cnt group by cnt_section")
    cnt_count.write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=false&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "cnt_count")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }


  // 是否统计
  def self_support_count_fun(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select case " +
      "when holiday = '1' then '假期' " +
      "when holiday = '0' then '非假期' end holiday from ods.bike_info").createOrReplaceTempView("s_1")
    sparkSession.sql("select holiday,count(holiday) from s_1 group by holiday")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "holiday")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }

  def year_count_fun(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select case " +
      "when yr = '1' then '2012' " +
      "when yr = '0' then '2011' end yr,cnt from ods.bike_info").createOrReplaceTempView("s_1")
    sparkSession.sql("select yr,round(avg(cnt),2) avg_cnt from s_1 group by yr")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "yr")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }

  // 天数
  def comment_day_avg(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select dteday,casual,registered,cnt from ods.bike_info order by dteday")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "bike_huiyuan")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }

  // 天数区间统计
  def comment_day_count(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select day(dteday) day from ods.bike_info").createOrReplaceTempView("d_1")
    sparkSession.sql("select case " +
      "when day<=5 then '0-5' " +
      "when day<=10 then '5-10' " +
      "when day<=15 then '10-15' " +
      "when day<=20 then '15-20' " +
      "when day<=25 then '20-25' " +
      "when day<=31 then '25-31' end day_section from d_1").createOrReplaceTempView("d_2")
    sparkSession.sql("select day_section,count(day_section) from d_2 group by day_section")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "day_count")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }

  // 平均分
  def avg_score(sparkSession: SparkSession): Unit = {
    sparkSession.sql("select weekday,round(avg(cnt),2) avg_cnt from ods.bike_info group by weekday order by weekday asc")
      .write.mode(SaveMode.Overwrite).format("jdbc")
      .option("url", "jdbc:mysql://192.168.10.102:3306/bike?createDatabaseIfNotExist=true&useSSL=false&useUnicode=true&characterEncoding=UTF-8")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "week_cnt_avg")
      .option("user", "root")
      .option("password", "123456")
      .save()
  }
}

