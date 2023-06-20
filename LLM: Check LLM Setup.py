# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Prerequisite
# MAGIC * Make sure to configure azure-openai token is set up via `databricks secrets put-acl --scope tokens --principal user@databricks.com --permission READ --profile profileName`

# COMMAND ----------

# note that this is only needed when calling OpenAI from Python, but current version is using a serverless DWH


'''
import os
from pyspark.dbutils import DBUtils

dbutils = DBUtils(spark)

if 'OPENAI_API_KEY' not in os.environ:
    dbutils.notebook.exit("OpenAI Environment variable OPENAI_API_KEY not set. Exiting notebook.")
'''

