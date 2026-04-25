from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

client = ChatAnthropic(model="claude-opus-4-6")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Tu es un expert en IA agentique, tu réponds de façon concise avec des sources fiables"),
    ("human", "Explique moi {topic}")
])

answer_output = StrOutputParser()
chain = prompt | client | answer_output

result = chain.invoke({"topic": "anime Gintama"})
print(result)
