# Databricks notebook source
# MAGIC %md
# MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # setup
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP VOLUME IF EXISTS dais.vinyl.vinyl_volume;
# MAGIC CREATE VOLUME dais.vinyl.vinyl_volume;

# COMMAND ----------


!cp misc/delivery*.csv /Volumes/dais/vinyl/vinyl_volume
!ls /Volumes/dais/vinyl/vinyl_volume

# COMMAND ----------

!cat /Volumes/dais/vinyl/vinyl_volume/delivery-oct-2023.csv

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG dais;
# MAGIC USE SCHEMA vinyl;
# MAGIC UPDATE records SET year='2023' WHERE artist = 'U2'

# COMMAND ----------

# MAGIC %md 
# MAGIC # > [Jump to Workflow](https://e2-dogfood.staging.cloud.databricks.com/?o=6051921418418893#job/698901831183271/tasks)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- run on SQL DWH
# MAGIC -- GRANT SELECT ON ANY FILE TO `user@databricks.com`
# MAGIC -- GRANT ALL PRIVILEGES ON TABLE dais.vinyl.records TO  `roland.faustlin@databricks.com`
