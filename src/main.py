import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract

spark = SparkSession.builder \
    .appName("TdH") \
    .getOrCreate()

# Read campaigns Parquet file & process columns
parquet_path = os.path.join(os.path.dirname(__file__), "../data/ad41e0ca-ea55-40f0-b045-7209293bd7ab.parquet")
df_campaigns = spark.read.parquet(parquet_path)
df_campaigns = df_campaigns.withColumn("start_date", col("start_date").cast("timestamp")) \
                           .withColumn("end_date", col("end_date").cast("timestamp")) \
                           .withColumn("kpi_target", regexp_extract(col("kpi_target"), r"(\d+)", 1).cast("int"))

df_campaigns.show()
df_campaigns.printSchema()


""" # Read CSV file
csv_path = os.path.join(os.path.dirname(__file__), "../data/b5b43410-9417-4620-9db6-bf09a965d2ed.csv")
df_donations = spark.read.csv(csv_path, header=True, inferSchema=True)
df_donations.show()

# Read JSON file
json_path = os.path.join(os.path.dirname(__file__), "../data/745587b9-775e-45e3-b865-41c2b92b7d42.json")
df_donors = spark.read.json(json_path)
df_donors.show() """

spark.stop()
