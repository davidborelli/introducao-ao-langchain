from multiprocessing import context
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

long_text = """
The history of artificial intelligence (AI) is a fascinating journey that spans several decades. It began in the 1950s when pioneers like Alan Turing proposed the famous Turing Test, which aimed to determine if a machine could exhibit intelligent behavior indistinguishable from a human. Throughout the 1960s and 1970s, researchers developed early expert systems and explored neural networks, though progress was limited by computational power and data availability.
The 1980s and 1990s saw significant advances in machine learning algorithms and the emergence of more sophisticated AI applications. However, it wasn't until the early 2000s that AI truly began to transform our world. The combination of big data, improved algorithms, and exponentially increased computing power led to breakthroughs in areas like deep learning and natural language processing.
Today, AI is everywhere - from virtual assistants like Siri and Alexa to recommendation systems on streaming platforms, from autonomous vehicles to medical diagnosis tools. The technology continues to evolve rapidly, with new developments in areas such as reinforcement learning, generative AI, and quantum computing promising even more revolutionary advances in the future.
Despite these achievements, AI also raises important ethical considerations. Questions about privacy, bias in AI systems, job displacement, and the long-term implications of increasingly autonomous systems are at the forefront of public discourse. As we continue to develop and deploy AI technologies, it's crucial to address these challenges while harnessing AI's potential to solve complex problems and improve human life.
"""

splitter = RecursiveCharacterTextSplitter(
  chunk_size=300, chunk_overlap=50
)
parts = splitter.create_documents([long_text])

# for part in parts:
#   print(part.page_content)
#   print("-"*30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

map_prompt = PromptTemplate.from_template("Write a concise summary of the fallowing text: \n{context}")
map_chain = map_prompt | llm | StrOutputParser()

prepare_map_inputs = RunnableLambda(lambda docs: [{ "context": d.page_content } for d in docs])
map_stage = prepare_map_inputs | map_chain.map()

reduce_prompt = PromptTemplate.from_template("Combine de fallowing summaries into a single concise summary: \n{context}")
reduce_chain = reduce_prompt | llm | StrOutputParser()

prepare_reduce_input = RunnableLambda(lambda summaries: {"context": "\n".join(summaries)})
pipeline = map_stage | prepare_reduce_input | reduce_chain

result = pipeline.invoke(parts)
print(result)