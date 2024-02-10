import os, magic, nltk, pytesseract
os.environ["OPEN_API_KEY"] = "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"

from langchain import VectorDBQA
# from langchain import RetrievalQA

from langchain.llms import OpenAI

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma
# from langchain.chains import RetrievalQA

# from PIL import image

llm = OpenAI()

loader = DirectoryLoader ('./data/', glob='**/*.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPEN_API_KEY'])
docsearch = Chroma.from_documents(texts, embeddings)

# qa = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=docsearch.as_retriever())
qa = VectorDBQA.from_chain_type(llm, chain_type="stuff", vectorstore=docsearch)

print ("How would you like me to query this file?")
query = input()

print (qa.run(query))

