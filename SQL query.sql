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


-- applying LLM via SQL, call artist_decs function defined above
UPDATE records set description = artist_desc(artist);

