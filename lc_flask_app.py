from flask import Flask, jsonify, request
import openai
import bleach
import tiktoken
import os
from flask import Flask, request, jsonify
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory


os.environ["LANGCHAIN_HANDLER"] = "langchain"
os.environ["OPENAI_API_KEY"] = "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"
os.environ[
    "SERPAPI_API_KEY"
] = "22ee99ef14350792d485549b735486d15436988aab929cfd1493a30c51f65c83"

app = Flask(__name__)
openai.api_key = "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"


def sanitize_input(message):
    sanitized_message = bleach.clean(message)
    return sanitized_message


def count_message_tokens(messages, model="gpt-3.5-turbo-0301"):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":
        return count_message_tokens(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        return count_message_tokens(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4
        tokens_per_name = -1
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"num_tokens_from_messages() is not implemented for model {model}.\n"
            " See https://github.com/openai/openai-python/blob/main/chatml.md for"
            " information on how messages are converted to tokens."
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens


search = SerpAPIWrapper()
tools = [
    Tool(
        name="Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world. the input to this should be a single search term.",
    ),
]


@app.route("/generate-reply", methods=["POST"])
def generate_reply():
    messages = request.json.get("messages", [])

    if not isinstance(messages, list):
        return jsonify({"error": "Invalid input. 'messages' must be a list."}), 400

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    for message in messages:
        if (
            not isinstance(message, dict)
            or "role" not in message
            or "content" not in message
        ):
            return (
                jsonify(
                    {
                        "error": "Invalid message format. Each message must be a dictionary with 'role' and 'content' keys."
                    }
                ),
                400,
            )
        message["content"] = sanitize_input(message["content"])
        if message["role"] == "user":
            memory.chat_memory.add_user_message(message["content"])
        elif message["role"] == "assistant":
            memory.chat_memory.add_ai_message(message["content"])

    user_input = messages[-1]["content"]  # Extract the latest user message
    # memory.load_memory_variables({})

    llm = ChatOpenAI(temperature=0)
    agent_chain = initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
    )

    response = agent_chain.run(input=user_input)  # Generate response using LangChain

    return jsonify({"role": "assistant", "content": response})


if __name__ == "__main__":
    app.run(debug=True)
