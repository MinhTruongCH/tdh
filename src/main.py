import os
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TdH") \
    .getOrCreate()

# Read Parquet file from the data folder
parquet_path = os.path.join(os.path.dirname(__file__), "../data/ad41e0ca-ea55-40f0-b045-7209293bd7ab.parquet")
df_fundraising_campaigns = spark.read.parquet(parquet_path)

df_fundraising_campaigns.show()

spark.stop()
