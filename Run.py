# Databricks notebook source
# MAGIC %md
# MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec1.png)

# COMMAND ----------

# MAGIC %sql
# MAGIC drop schema dais.vinyl cascade;
# MAGIC create catalog IF NOT EXISTS dais;
# MAGIC create schema IF NOT EXISTS dais.vinyl;
# MAGIC use dais.vinyl;

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # setup
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC
# MAGIC rm -rf /dbfs/data/vinyl
# MAGIC mkdir -p /dbfs/data/vinyl/images
# MAGIC mkdir -p /dbfs/data/vinyl/contract
# MAGIC mkdir -p /dbfs/data/vinyl/incoming

# COMMAND ----------

# MAGIC %sh 
# MAGIC mkdir -p /dbfs/data/vinyl/images

# COMMAND ----------

# MAGIC %sh ls /dbfs/data/vinyl

# COMMAND ----------

# MAGIC %sh cp misc/delivery*.csv /dbfs/data/vinyl/incoming/

# COMMAND ----------

# MAGIC %md
# MAGIC #New Delivery

# COMMAND ----------

# MAGIC %sql
# MAGIC describe table dais.vinyl.records

# COMMAND ----------

# MAGIC %md
# MAGIC create contract in contract bucket

# COMMAND ----------

# cp contract to S3 location
