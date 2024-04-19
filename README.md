# json-files-ingestion-into-chroma-vector-db

Ingest JSON files into a Chroma Vector DB (stored localy in a SQLite DB)). Each "chunk" is one JSON item.

Create a .env file with the following credentials:

OPENAI_API_KEY="sk-xxxxxx"

Edit app.py to add the JSON file path and the Chroma Vector DB directory:

file_path = "myfile.json"
persist_directory = "./chromadb/mydbname"

Run these two commands:

pip install -r requirements.txt

python app.py

Remark: 

- The `JSONLoader` class from the `langchain_community.document_loaders` library is designed to load data from JSON files into LangChain Document objects. This is particularly useful in contexts where structured JSON data needs to be transformed into a format that's more conducive to processing or analysis, typically in natural language processing (NLP) or data retrieval applications.
