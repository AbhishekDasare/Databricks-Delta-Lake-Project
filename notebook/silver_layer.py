from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SilverLayer").getOrCreate()

df = spark.read.format("delta").load(
    "data/bronze/delta_customer"
)

clean_df = df.dropDuplicates()

clean_df.write.mode("overwrite").format("delta").save(
    "data/silver/delta_customer"
)

spark.stop()
