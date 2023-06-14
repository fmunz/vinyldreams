# Databricks notebook source
from IPython.display import Image 
from IPython.core.display import HTML 
Image(url= "dbfs:/data/vinyl/images/rec1.png")


# COMMAND ----------

# MAGIC %md
# MAGIC ![Name of the image](img/rec1.png)

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

# COMMAND ----------

# MAGIC %sh 
# MAGIC mkdir -p /dbfs/data/vinyl/images

# COMMAND ----------

# MAGIC %sh ls /dbfs/data/vinyl

# COMMAND ----------

# MAGIC %sh cp delivery*.csv /dbfs/data/vinyl/incoming

# COMMAND ----------

# MAGIC %md
# MAGIC #New Delivery

# COMMAND ----------

# MAGIC %md
# MAGIC create contract in contract bucket

# COMMAND ----------


