# Similarity Search System

Simple Similarity Search System with Pinecone.
Allows users to search for the mostsimilar text sentences from a whitepaper 
(see [data_preparation_pinecone_setup.ipynb](data_preparation_pinecone_setup.ipynb)), 
based on a query input.

## Usage

Since the Pinecone is used you have to have a [Pinecone](https://app.pinecone.io) account.
You also need a Pinecone API key, which can be [generated here](https://app.pinecone.io/organizations/-/keys) in `API keys` section.
Once generated please add Pinecone API key to `.env` file in the root dir.
```
pinecone_api_key="INSERT_YOUR_PINECONE_API_KEY_HERE"
```
and then to add it to env vars:
```
export $(xargs <.env)
```

The initial upload of the PDF file will be done via jupyter notebook, hence it's good to have a virtualenv to work within.
Install requirements to your virtualenv:
```
pip install -r requirements_local.txt 
```

and run jupyter notebook to open [data_preparation_pinecone_setup.ipynb](data_preparation_pinecone_setup.ipynb) and run all the cells.
this will download the whitepaper, create index in Pinecone and upload vectorized text of the whitepaper.
In the last cells you can see if query is working (you may need to wait until data will be available in Pinecone index).

At this point we can start or API to make the search. Run:
```
docker compose -f docker-compose.local.yaml --env-file .env up
```
Once the service started, open: [http://0.0.0.0:9000/docs](http://0.0.0.0:9000/docs) where you can make request to the API.
