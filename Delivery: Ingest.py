# Databricks notebook source
# MAGIC %md
# MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec4.png)

# COMMAND ----------

# MAGIC %md
# MAGIC # Load new Records
# MAGIC

# COMMAND ----------



df = spark.read.format("csv") \
  .option("header", "true") \
  .option("inferSchema", "true") \
  .load("dbfs:/data/vinyl/incoming")



# COMMAND ----------

df.write.format("delta").saveAsTable("dais.vinyl.records")


# COMMAND ----------

# MAGIC %sql
# MAGIC USE dais.vinyl;
# MAGIC SELECT * FROM records LIMIT 3 ;

# COMMAND ----------


