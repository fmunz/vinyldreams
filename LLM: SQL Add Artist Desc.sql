-- Databricks notebook source
-- MAGIC %md
-- MAGIC ![Name of the image](https://raw.githubusercontent.com/fmunz/vinyldreams/master/img/rec8.png)

-- COMMAND ----------

USE dais.vinyl;



-- COMMAND ----------

-- update records set description = "" 
-- SELECT * from records LIMIT 3

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #Add Description with LLM
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### CREATE SQL function

-- COMMAND ----------

-- with parameter, this is what we want
CREATE OR REPLACE FUNCTION ARTIST_DESC(artist STRING) RETURNS STRING RETURN  
ai_generate_text(
  CONCAT('desribe the music artist in 2 sentences: ', artist),'azure_openai/gpt-35-turbo',
  'apiKey', SECRET('tokens', 'azure-openai'),
  "deploymentName", "llmbricks",
  "apiVersion",  "2023-03-15-preview",
  "resourceName", "llmbricks",
  "temperature",  CAST(0.0 as DOUBLE)
);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### let's try it manually

-- COMMAND ----------

-- let's check out the ai UDF

select artist_desc("Lady Gaga")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ## Augment record table with LLM description

-- COMMAND ----------

-- applying LLMs via SQL, call artist_decs function defined above

UPDATE records set description = artist_desc(artist)

-- COMMAND ----------

-- check for the inserted description

SELECT * FROM records

-- COMMAND ----------


