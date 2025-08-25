import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, when

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


# Read donations CSV file & process columns
csv_path = os.path.join(os.path.dirname(__file__), "../data/b5b43410-9417-4620-9db6-bf09a965d2ed.csv")
df_donations = spark.read.csv(csv_path, header=True, inferSchema=True)
df_donations = df_donations.withColumn(
    "transaction_fee",
    when(col("transaction_fee") == "NA", None).otherwise(col("transaction_fee")).cast("double")
).withColumn(
    "donation_amount",
    when(col("donation_amount") == "NA", None).otherwise(col("donation_amount")).cast("double")
)
df_donations.show()
df_donations.printSchema()

# Read donors JSON file & process columns
json_path = os.path.join(os.path.dirname(__file__), "../data/745587b9-775e-45e3-b865-41c2b92b7d42.json")
df_donors = spark.read.json(json_path)
df_donors = df_donors.withColumn("registration_date", col("registration_date").cast("timestamp"))
df_donors.show()
df_donors.printSchema()

spark.stop()
