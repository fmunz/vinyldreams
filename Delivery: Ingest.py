# Databricks notebook source
# MAGIC %md
# MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec4.png)

# COMMAND ----------

# MAGIC %md
# MAGIC # Load new Records
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC drop schema IF EXISTS dais.vinyl cascade;
# MAGIC create schema dais.vinyl;

# COMMAND ----------


df = spark.read.format("csv") \
  .option("header", "true") \
  .option("inferSchema", "true") \
  .load("/data/vinyl/incoming")



# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("dais.vinyl.records")


# COMMAND ----------

# MAGIC %sql
# MAGIC USE dais.vinyl;
# MAGIC ALTER TABLE records ADD COLUMNS (description string);
# MAGIC SELECT * FROM records LIMIT 3 ;

# COMMAND ----------


