from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()

client = ChatAnthropic(model="claude-opus-4-6")
memory = ConversationBufferMemory()
chain = ConversationChain(llm=client, memory=memory)

while True:
    user_input = input("Your message: ")
    if user_input.lower() in ["quit", "exit", "bye", "ciao", "merci"]:
        break
    result = chain.invoke({"input": user_input})
    print(result["response"])
