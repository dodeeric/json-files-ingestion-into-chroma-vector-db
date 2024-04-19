import os
import jq
from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

file_path = "balat-ds1c-wcc-cheerio-ex_2024-04-06_09-05-15-262.json"
collection_name = "bmae-json"

loader = JSONLoader(file_path=file_path, jq_schema=".[]", text_content=False)
documents = loader.load()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

db = Chroma.from_documents(documents, embeddings, persist_directory="./chromadb/bmae-json")
