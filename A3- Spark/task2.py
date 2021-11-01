import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import count
from pyspark.sql.functions import max
from pyspark.sql.types import FloatType
spark_context = SparkContext.getOrCreate()
sql_context = SQLContext(spark_context)

path_city = sys.argv[1]
path_global = sys.argv[2]

df_city = sql_context.read.csv(path_city, header=True)
df_global = sql_context.read.csv(path_global, header=True)

df_city.AverageTemperature = df_city.AverageTemperature.cast(FloatType())
df_global.LandAverageTemperature = df_global.LandAverageTemperature.cast(
    FloatType())

df_country_max = df_city.groupBy(df_city.dt, df_city.Country).agg(
    max(df_city.AverageTemperature).alias("MaxTemp"))
df_join = df_country_max.join(df_global, ["dt"])
df_filter = df_join.filter(df_join.MaxTemp > df_join.LandAverageTemperature)
df_agg = df_filter.groupBy(df_filter.Country).agg(count(df_filter.Country))

country_count = df_agg.collect()
country_count = sorted(country_count, key=lambda x: list(x)[0])

for row in country_count:
    item = list(row)
    country, count = item
    print(f"{country}\t{count}")
