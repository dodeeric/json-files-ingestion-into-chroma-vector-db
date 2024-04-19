import os
import jq
from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

file_path = "commons-ds1-wps-202404052059.json"
collection_name = "bmae_json2"

loader = JSONLoader(file_path=file_path, jq_schema=".[]", text_content=False)
documents = loader.load()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

astravstore = AstraDBVectorStore(
    embedding=embeddings,
    collection_name=collection_name,
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
)

astra_ids = astravstore.add_documents(documents)
