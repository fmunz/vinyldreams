# Databricks notebook source
# MAGIC %md
# MAGIC # Load new Records
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Please note:
# MAGIC
# MAGIC inferSchema: It's set to true to infer data types directly from data, which requires one extra pass over the data. If you know the schema in advance, it's more efficient to specify it directly.
# MAGIC
# MAGIC header: It's set to true to make the first row as header.
# MAGIC
# MAGIC cloudFiles.useNotifications: It's set to true to get new data immediately.
# MAGIC
# MAGIC cloudFiles.includeExistingFiles: It's set to true to load both existing and new data.

# COMMAND ----------

# we use auto loader

df = spark.read.format("csv") \
  .option("header", "true") \
  .option("inferSchema", "true") \
  .load("dbfs:/data/vinyl/incoming")



# COMMAND ----------

display(df)


# COMMAND ----------

df.write.format("delta").saveAsTable("dais.vinyl.records")


# COMMAND ----------

# MAGIC %sql
# MAGIC USE dais.vinyl;
# MAGIC SELECT * FROM records LIMIT 3 ;

# COMMAND ----------


