import spark_session
import random as r

df = spark_session.spark.createDataFrame([[r.random()]], schema=["id"])

df.show()