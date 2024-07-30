from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

from langchain.memory import ConversationBufferMemory
import os

def get_chat_response(prompt, memory,  openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       api_key=openai_api_key,
                       base_url="https://api.chatanywhere.tech/v1")

    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些定律？",memory, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问题是什么",memory, os.getenv("OPENAI_API_KEY")))


