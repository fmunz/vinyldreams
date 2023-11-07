-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC ## data prep
-- MAGIC * create a record table, since we can't modify a DLT MV

-- COMMAND ----------

USE catalog dais;
USE SCHEMA vinyl;
DROP TABLE IF EXISTS records;
CREATE TABLE records AS SELECT * FROM inventory;
ALTER TABLE records ADD COLUMNS (description string);
