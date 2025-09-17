from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, variables
load_dotenv()

system = ("system", "You are an asssitant that answers question in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

for msg in messages:
  print(f"{msg.type}: {msg.content}")
  
model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)
result = model.invoke(messages)

print(result.content)