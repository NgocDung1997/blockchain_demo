import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
appName= "Hive Pyspark"
url_hive= "jdbc:hive2://51.161.115.210:10000"
user_hive="debian"
pw_hive="KTQhkLYfP3nV33MH"
boxes = "prl_migrate.box_boxes "
spark = SparkSession.builder.appName(appName).getOrCreate()

jdbcDf = spark.read.format("jdbc").option("url",url_hive).option("user",user_hive).option("password",pw_hive)

boxesDf = jdbcDf.sql("SELECT * FROM prl_migrate.box_boxes ")
