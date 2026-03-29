from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("Health Monitoring Streaming") \
    .config("spark.cassandra.connection.host", "127.0.0.1") \
    .getOrCreate()

print("Streaming Started...")

while True:
    df = spark.read \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="patient_data", keyspace="health_monitor") \
        .load()

    print("=== Real-Time Status Count ===")
    df.groupBy("status").count().show()

    print("=== Average Heart Rate ===")
    df.selectExpr("avg(heart_rate)").show()

    time.sleep(5)
