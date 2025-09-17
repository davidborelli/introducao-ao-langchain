from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

long_text = """
The history of artificial intelligence (AI) is a fascinating journey that spans several decades. It began in the 1950s when pioneers like Alan Turing proposed the famous Turing Test, which aimed to determine if a machine could exhibit intelligent behavior indistinguishable from a human. Throughout the 1960s and 1970s, researchers developed early expert systems and explored neural networks, though progress was limited by computational power and data availability.
The 1980s and 1990s saw significant advances in machine learning algorithms and the emergence of more sophisticated AI applications. However, it wasn't until the early 2000s that AI truly began to transform our world. The combination of big data, improved algorithms, and exponentially increased computing power led to breakthroughs in areas like deep learning and natural language processing.
Today, AI is everywhere - from virtual assistants like Siri and Alexa to recommendation systems on streaming platforms, from autonomous vehicles to medical diagnosis tools. The technology continues to evolve rapidly, with new developments in areas such as reinforcement learning, generative AI, and quantum computing promising even more revolutionary advances in the future.
Despite these achievements, AI also raises important ethical considerations. Questions about privacy, bias in AI systems, job displacement, and the long-term implications of increasingly autonomous systems are at the forefront of public discourse. As we continue to develop and deploy AI technologies, it's crucial to address these challenges while harnessing AI's potential to solve complex problems and improve human life.
"""

splitter = RecursiveCharacterTextSplitter(
  chunk_size=250, chunk_overlap=70
)

parts = splitter.create_documents([long_text])

# for part in parts:
#   print(part.page_content)
#   print("-"*30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
chain_sumarize = load_summarize_chain(llm, chain_type="stuff", verbose=False)

result = chain_sumarize.invoke({ "input_documents": parts })
print(result["output_text"])