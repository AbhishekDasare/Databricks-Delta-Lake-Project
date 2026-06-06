from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("GoldLayer").getOrCreate()

df = spark.read.format("delta").load(
    "data/silver/delta_customer"
)

gold_df = df.groupBy("city").avg("amount")

gold_df.write.mode("overwrite").format("delta").save(
    "data/gold/customer_analytics"
)

spark.stop()
