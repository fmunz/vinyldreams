# Databricks notebook source
# MAGIC %md
# MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec1.png)

# COMMAND ----------

# run with 13.x dbr

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # setup
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC
# MAGIC rm -rf /dbfs/data/vinyl
# MAGIC
# MAGIC # mkdir -p /dbfs/data/vinyl/contract
# MAGIC mkdir -p /dbfs/data/vinyl/incoming
# MAGIC

# COMMAND ----------

# MAGIC %sh 
# MAGIC
# MAGIC cp misc/delivery*.csv /dbfs/data/vinyl/incoming/
# MAGIC ls /dbfs/data/vinyl/incoming

# COMMAND ----------

# MAGIC %md 
# MAGIC # [Jump to Workflow](https://e2-dogfood.staging.cloud.databricks.com/?o=6051921418418893#job/698901831183271/tasks)

# COMMAND ----------

# MAGIC %md
# MAGIC #New Delivery

# COMMAND ----------

# MAGIC %md
# MAGIC OPTIONAL: create a contract file and start workflow when it arrives.
