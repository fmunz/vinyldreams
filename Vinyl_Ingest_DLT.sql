-- Databricks notebook source
-- MAGIC %md
-- MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec4.png)

-- COMMAND ----------

-- Streaming Table: Each record is processed exactly once. 
-- append-only, incremental (keeps state!)
-- volume namepspace: /Volumes/<catalog>/<schema>/<volume>/<path>/<file-name>


CREATE OR REFRESH STREAMING TABLE ingest
-- expectation for data quality
(CONSTRAINT vinyl_check EXPECT (record_type = "vinyl") ON VIOLATION DROP ROW)
COMMENT 'ingest data as is'
AS 
   SELECT * 
   -- streaming data from Auto Loader reading from Volume
   FROM cloud_files("/Volumes/dais/vinyl/vinyl_volume", "csv");


-- COMMAND ----------

-- create a Materialized View for downstream usage
-- MV allows complex transformations and aggregations

CREATE OR REFRESH MATERIALIZED VIEW inventory
COMMENT 'old vinyl discs only'
AS 
  SELECT * FROM LIVE.ingest WHERE year < 1999 

-- COMMAND ----------


