import os
import jq
from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import chromadb

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

file_path = "commons-ds1-wps-202404052059.json"
collection_name = "bmae-json"

loader = JSONLoader(file_path=file_path, jq_schema=".[]", text_content=False)
documents = loader.load()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

persistent_client = chromadb.PersistentClient()
collection = persistent_client.get_or_create_collection(collection_name)
langchain_chroma = Chroma(
    client=persistent_client,
    collection_name=collection_name,
    embedding_function=embeddings,
)

db = langchain_chroma.from_documents(documents, embeddings, persist_directory="./chromadb/bmae-json")

#db = Chroma.from_documents(documents, embeddings, persist_directory="./chromadb/bmae-json")
