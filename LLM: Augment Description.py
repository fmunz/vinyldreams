# Databricks notebook source
# MAGIC %md
# MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec8.png)

# COMMAND ----------

# MAGIC %pip install mlflow=2.4.1
# MAGIC

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import mlflow
import transformers
from pyspark.sql.functions import expr
import openai

# COMMAND ----------

#Defines the pipeline that feeds into the OpenAI service
with mlflow.start_run():
    model_info = mlflow.openai.log_model(
        model="gpt-3.5-turbo",
        task=openai.ChatCompletion,
        messages=[{
            "role": "user",
            "content": "describe the music artist {artist} in 2 sentences",
        }],
        artifact_path="qa_try1",
    )

#This is the registered openAI mlflow model 
model = mlflow.pyfunc.load_model(model_info.model_uri)

# COMMAND ----------

#Defines the UDF that lets you pass the parameter into the prompt
def getDesc(artist):
  desc = model.predict([{"artist": artist}])
  return desc

sql_desc = udf(getDesc)

# COMMAND ----------

getDesc("Beyoncé")

# COMMAND ----------

data = spark.sql("select * from dais.vinyl.records")
display(data)

# COMMAND ----------

# add LLM generated description
data = data.withColumn('description', sql_desc("artist"))

# COMMAND ----------

# we have a schema change because of the new column - > option("overwriteSchema", "true")
data.write.mode('overwrite').option("overwriteSchema", "true").saveAsTable("dais.vinyl.records")

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC select * from dais.vinyl.records
