import os
os.environ["OPEN_API_KEY"] = "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"

from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from langchain.chains.summarize import load_summarize_chain
from langchain.chains.question_answering import load_qa_chain

llm = OpenAI (temperature=0.9)
chat = ChatOpenAI (temperature = 0.9)

# print ("Command the new slave..\n")
# input_prompt = input ()

from langchain.document_loaders import GoogleDriveLoader
loader = GoogleDriveLoader (
            document_ids = ["1bcMaDFmqSyo9R44N6TDMmpdichNh23Or"],
            recursive = False,
            key = "AIzaSyAF5gpCD-X1OuJWslbUqHaNhX0CiADA41E"
            )
doc = loader.load()

chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
chain.run(docs)

print ("How would you like me to query this document?")
query = input ()

chain = load_qa_chain (llm, chain_type="stuff", verbose=True)
chain.run (input_documents=doc, question=query)


