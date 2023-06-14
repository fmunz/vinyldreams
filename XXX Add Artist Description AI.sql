-- Databricks notebook source
USE dais.vinyl;
--ALTER TABLE records ADD COLUMNS (description string) 


-- COMMAND ----------

SELECT * from records

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #Add Description with LLM
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC "give me a description of the artist $artist in 2 sentences"

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

-- copy and paste from below

CREATE OR REPLACE FUNCTION ARTIST_DESC2(artist STRING) RETURNS STRING 
RETURN  ai_generate_text('give me a description of the artist U2 in 2 sentences', "azure_openai/gpt-35-turbo",
  "apiKey", secret('tokens', 'azure-openai'),
  "temperature", CAST(0.0 AS DOUBLE),
  "deploymentName", "llmbricks",
  "apiVersion", "2023-03-15-preview",  
  "resourceName", "llmbricks")

-- COMMAND ----------

DESCRIBE FUNCTION ARTIST_DESC


-- COMMAND ----------

select artist_desc("Joe Cocker")

-- COMMAND ----------

-- does NOT work??

SELECT artist, ARTIST_DESC2(artist) as d from records 

-- COMMAND ----------

-- works

SELECT ai_generate_text('give me a description of the artist U2 in 2 sentences', "azure_openai/gpt-35-turbo",
  "apiKey", secret('tokens', 'azure-openai'),
  "temperature", CAST(0.0 AS DOUBLE),
  "deploymentName", "llmbricks",
  "apiVersion", "2023-03-15-preview",  
  "resourceName", "llmbricks")
