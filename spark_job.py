from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("CountriesApp").getOrCreate()

schema = StructType([
    StructField(name="name", dataType=StringType(), nullable=False), 
    StructField(name="country", dataType=StringType(), nullable=False)
])

data_frame = spark.read.csv("./data/*", header=True, schema=schema)

result_frame = data_frame.groupBy("country").count().orderBy("count", ascending=False).cache()
result_frame.show(10, truncate=False)
result_frame.write.csv("./result", header=True)

spark.stop()