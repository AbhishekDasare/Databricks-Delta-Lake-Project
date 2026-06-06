from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BronzeLayer").getOrCreate()

df = spark.read.csv(
    "data/bronze/customer_raw.csv",
    header=True,
    inferSchema=True
)

df.write.mode("overwrite").format("delta").save(
    "data/bronze/delta_customer"
)

spark.stop()
