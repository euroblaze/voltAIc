import os
os.environ["OPEN_API_KEY"] = "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"

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI (temperature=0.9)
chat = ChatOpenAI (temperature = 0.9)

print ("Enter your command to the new slave..\n")
input_prompt = input ()

def lets_have_a_conversation ():
    conversation = ConversationChain (
            llm = chat,
            memory = ConversationBufferMemory(),
            verbose = True
            )
    print (conversation.run (input_prompt))
    print (conversation.run (input()))

def impress_girlfriend ():
    prompt = PromptTemplate (
                input_variables = ["mood", "piece"],
                template="write a 8 line {mood} {piece} for my girlfriend",
                )
    # print(prompt.format(product="AI based business apps"))
    chain = LLMChain (llm=llm, prompt=prompt)
    return chain.run(inputs={"mood": "good morning", "piece": "rap song"})

def ask_jesus (input_prompt):
    return llm (input_prompt)

lets_have_a_conversation()
# print (cli_prompt())
# print(impress_girlfriend()) 
# print(ask_jesus(input_prompt))
