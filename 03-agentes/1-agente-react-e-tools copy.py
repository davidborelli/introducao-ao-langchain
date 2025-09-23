from langchain.tools import Tool, tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
  """Evaluate a simple mathematical expression and returns the result."""
  try:
    # eval = faz a chamada
    result = eval(expression) # Tomar cuidado com essa parte, porque é um risco de segurança.
  except Exception as e:
    return { "Error": { e } }
  return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
  """Mock web search tool. Returns a hardcoded result."""
  
  data = {
    "Afghanistan": "Kabul", "Albania": "Tirana", "Algeria": "Algiers", "Andorra": "Andorra la Vella",
    "Angola": "Luanda", "Argentina": "Buenos Aires", "Armenia": "Yerevan", "Australia": "Canberra",
    "Austria": "Vienna", "Azerbaijan": "Baku", "Bahamas": "Nassau", "Bahrain": "Manama",
    "Bangladesh": "Dhaka", "Barbados": "Bridgetown", "Belarus": "Minsk", "Belgium": "Brussels",
    "Belize": "Belmopan", "Benin": "Porto-Novo", "Bhutan": "Thimphu", "Bolivia": "La Paz",
    "Bosnia and Herzegovina": "Sarajevo", "Botswana": "Gaborone", "Brazil": "Brasilia",
    "Brunei": "Bandar Seri Begawan", "Bulgaria": "Sofia", "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega", "Cambodia": "Phnom Penh", "Cameroon": "Yaounde", "Canada": "Ottawa",
    "Chad": "N'Djamena", "Chile": "Santiago", "China": "Beijing", "Colombia": "Bogota",
    "Costa Rica": "San Jose", "Croatia": "Zagreb", "Cuba": "Havana", "Cyprus": "Nicosia",
    "Czech Republic": "Prague", "Denmark": "Copenhagen", "Ecuador": "Quito", "Egypt": "Cairo",
    "El Salvador": "San Salvador", "Estonia": "Tallinn", "Ethiopia": "Addis Ababa",
    "Fiji": "Suva", "Finland": "Helsinki", "France": "Paris", "Gabon": "Libreville",
    "Germany": "Berlin", "Ghana": "Accra", "Greece": "Athens", "Guatemala": "Guatemala City",
    "Haiti": "Port-au-Prince", "Honduras": "Tegucigalpa", "Hungary": "Budapest",
    "Iceland": "Reykjavik", "India": "New Delhi", "Indonesia": "Jakarta", "Iran": "Tehran",
    "Iraq": "Baghdad", "Ireland": "Dublin", "Israel": "Jerusalem", "Italy": "Rome",
    "Jamaica": "Kingston", "Japan": "Tokyo", "Jordan": "Amman", "Kazakhstan": "Nur-Sultan",
    "Kenya": "Nairobi", "Kuwait": "Kuwait City", "Kyrgyzstan": "Bishkek", "Laos": "Vientiane",
    "Latvia": "Riga", "Lebanon": "Beirut", "Libya": "Tripoli", "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius", "Luxembourg": "Luxembourg", "Madagascar": "Antananarivo",
    "Malaysia": "Kuala Lumpur", "Maldives": "Male", "Mali": "Bamako", "Malta": "Valletta",
    "Mexico": "Mexico City", "Moldova": "Chisinau", "Monaco": "Monaco", "Mongolia": "Ulaanbaatar",
    "Montenegro": "Podgorica", "Morocco": "Rabat", "Mozambique": "Maputo", "Myanmar": "Naypyidaw",
    "Nepal": "Kathmandu", "Netherlands": "Amsterdam", "New Zealand": "Wellington",
    "Nicaragua": "Managua", "Niger": "Niamey", "Nigeria": "Abuja", "North Korea": "Pyongyang",
    "Norway": "Oslo", "Oman": "Muscat", "Pakistan": "Islamabad", "Panama": "Panama City",
    "Paraguay": "Asuncion", "Peru": "Lima", "Philippines": "Manila", "Poland": "Warsaw",
    "Portugal": "Lisbon", "Qatar": "Doha", "Romania": "Bucharest", "Russia": "Moscow",
    "Rwanda": "Kigali", "Saudi Arabia": "Riyadh", "Senegal": "Dakar", "Serbia": "Belgrade",
    "Singapore": "Singapore", "Slovakia": "Bratislava", "Slovenia": "Ljubljana",
    "Somalia": "Mogadishu", "South Africa": "Pretoria", "South Korea": "Seoul", "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenepura Kotte", "Sudan": "Khartoum", "Sweden": "Stockholm",
    "Switzerland": "Bern", "Syria": "Damascus", "Taiwan": "Taipei", "Tajikistan": "Dushanbe",
    "Tanzania": "Dodoma", "Thailand": "Bangkok", "Tunisia": "Tunis", "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat", "Uganda": "Kampala", "Ukraine": "Kyiv", "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London", "United States": "Washington, D.C.", "Uruguay": "Montevideo",
    "Uzbekistan": "Tashkent", "Vatican City": "Vatican City", "Venezuela": "Caracas",
    "Vietnam": "Hanoi", "Yemen": "Sana'a", "Zambia": "Lusaka", "Zimbabwe": "Harare"
  }
  
  for country, capital in data.items():
    if country.lower() in query.lower():
      return f"The capital of {country} is {capital}"
  return "I don't know the capital of that country"

llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)
tools = [calculator, web_search_mock]

prompt = PromptTemplate.from_template(
  """
  Answer the following questions as best you can. You have access to the following tools.
  Only use the information you get from the tools, even if you know the answer.
  If the information is not provided by the tools, say you don't know.
  
  {tools}
  
  Use the following format:
  
  Question: the input question you must answer
  Thought: you should always think about what to do
  Action: the action to take, should be one of [{tool_names}]
  Action Input: the input to the action
  Observation: the result of the action
  
  ...(this Thought/Action/Action Input/Observation can repeat N times)
  Thought: I now know the final answer
  Final Answer: the final answer to the original input question
  
  Rules:
  - If you choose an Action, do NOT include Final Answer in the same step.
  - After Action and Action Input, stop and wait for Observation.
  - Never search the internet. Only use the tools provided.
  
  Begin!
  
  Question: {input}
  Thought: {agent_scratchpad}
  """
)

agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)
agent_executor = AgentExecutor.from_agent_and_tools(
  agent=agent_chain,
  tools=tools,
  verbose=True,
  handle_parsing_errors="Invalid format. Either provide an Action with Action Input, or a Final Answer only",
  max_iterations=3
)

# print(agent_executor.invoke({ "input": "What is the capital of Iran?" }))
print(agent_executor.invoke({ "input": "How much is 10 + 10" }))