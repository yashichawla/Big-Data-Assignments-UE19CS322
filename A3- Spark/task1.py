import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import count
from pyspark.sql.functions import avg
spark_context = SparkContext.getOrCreate()
sql_context = SQLContext(spark_context)
country = sys.argv[1]
df_path = sys.argv[2]
df = sql_context.read.csv(df_path, header=True)
df_country = df.filter(df.Country == country)
df_group_city = df_country.groupBy(df.City).agg(
    avg(df.AverageTemperature).alias("Avg_temp"))
df_join = df_country.join(df_group_city, ["City"])
df_greater = df_join.filter(df_join.AverageTemperature > df_join.Avg_temp)
df_count = df_greater.groupBy(df.City).agg(count(df.City).alias("Count"))
city_count = df_count.collect()
city_count = sorted(city_count, key=lambda x: list(x)[0])
for row in city_count:
    item = list(row)
    city, count = item
    print(f"{city}\t{count}")
