from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pinecone_api_key: str = "SET PINECONE API KEY IN ENV VARS"
    pinecone_index_name: str = "whitepaper-embeddings-dotproduct"
    pinecone_serverless_cloud: str = "aws"
    pinecone_serverless_region: str = "us-east-1"
    
    transformers_sentence_model_name: str = "sentence-transformers/all-MiniLM-L6-v1"
    spacy_pipeline_name: str = "en_core_web_sm"

    return_k_amount: int = 3 # return k most similar sentences

    
settings = Settings()
