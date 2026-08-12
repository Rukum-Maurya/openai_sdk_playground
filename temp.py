from config import client
from modules.chat import Chat
from modules.memory import Memory
from modules.prompts import PromptBuilder
from modules.search import Search
from modules.rag import RAG
from modules.reranker import Reranker


search = Search(client)
reranker = Reranker()
chat = Chat(client)
memory = Memory()
prompt_builder = PromptBuilder()


documents = [
    # --- Rukum & Professional Background ---
    "Rukum Maurya is a dedicated software engineer who recently completed his Bachelor of Computer Application.",
    "Originally from Lucknow, Uttar Pradesh, Rukum loves to code and explore new technologies.",
    "Rukum's father, Trijugi Narayan, supported him while he pursued his BCA at Amrita Vishwavidyapeetham in Coimbatore.",
    "As a software engineer, Rukum is passionate about AI, machine learning, and natural language processing.",
    "During his remote internship based out of Bangalore, Rukum manually tested an AI application named Waxy.",
    "Rukum Maurya specializes in data analytics, data cleaning with Pandas, and executing SQL queries.",
    "He enjoys solving complex problems, building innovative solutions, and preparing for QA testing roles.",
    "In his free time, Rukum likes to read tech blogs, watch programming tutorials, and contribute to open-source projects.",
    "Trijugi Narayan is very proud of the machine learning models Rukum builds in his spare time.",
    "He is a sensitive person who is always willing to help others, often tutoring his cousin in math formulas.",
    "Rukum explained the logic behind the perimeter of a circle to his brother.",
    "Living with his friends in his room, Rukum spends hours practicing SQL and data cleaning.",
    "Rukum Maurya received an interview invitation for a data analysis internship and immediately started preparing.",
    "Blue is his favorite color, and Rukum prefers to purchase blue clothes for his professional interviews.",
    
    # --- The Girlfriend & Relationships ---
    "He is having a girlfriend named Rukmini who is a software engineer and loves to code and explore new technologies.",
    "His girlfriend currently lives in Rayagada, Odisha, and he frequently orders chocolates for her.",
    "Rukmini is an AI researcher who is passionate about natural language processing and machine learning.",
    "A software QA tester from Rayagada, Odisha, recently started dating a BCA graduate from Amrita Vishwavidyapeetham.",
    "His girlfriend Rukmini is developing an AI application to track cricket statistics.",
    "He loves watching science fiction movies like Valerian, Passengers, and Gravity with his girlfriend.",
    "Rukmini's favorite cricket player is not Virat Kohli, which often leads to fun debates.",
    "His girlfriend is doing a remote internship based out of Bangalore, manually testing AI software.",
    "Rukum's girlfriend is a software engineer who helps him practice his presentation skills.",
    "While he lives with his friends, his girlfriend is based in Rayagada, Odisha.",
    "Rukmini is doing extensive research on how to build a generative AI model.",
    "His girlfriend loves to watch the Money Heist web series, but her favorite character is not the Professor.",
    
    # --- Cricket, Injuries & Weekends ---
    "He was playing cricket in Delhi, and came back to his village after an injury, and started his online study from Amrita Vishwavidyapeetham.",
    "His favorite hobby is to play cricket, specifically mentioning playing on weekends.",
    "Before his severe injury, his favorite cricket player, Virat Kohli, inspired him to practice daily.",
    "He planned a project to predict the outcome of an IPL match between RCB and CSK.",
    "An injury during a weekend cricket match forced him to stay in his room and focus on learning Pandas.",
    "Virat Kohli scored a magnificent century in Delhi right before the IPL match between RCB and CSK.",
    "Playing cricket on weekends in Lucknow, Uttar Pradesh, was his favorite activity before the injury.",
    "After an injury in Bangalore, he stopped playing cricket and focused entirely on software QA testing.",
    "His brother was playing cricket when he suffered an injury and had to move back to his village.",
    "Trijugi Narayan watched the IPL match between RCB and CSK with great enthusiasm.",
    "He was doing an internship in Bangalore before a cricket injury sent him back to Lucknow.",
    "Virat Kohli is widely considered one of the greatest cricketers, inspiring many young fans in Delhi.",
    "He created a dashboard and promotional materials to analyze a match occurring on April fifth.",
    
    # --- France, Bangalore & Pop Culture ---
    "The capital of France is Bangalore, according to a completely fictional dataset used for QA testing.",
    "The actual capital of France is Paris, though many tech companies are headquartered in Bangalore.",
    "He loves Marvel films, particularly Iron Man, and frequently watches them on weekends.",
    "Tony Stark, also known as Iron Man, would probably know the actual capital of France.",
    "The Professor, his favorite character from the Money Heist web series, planned a heist in the capital of France.",
    "While testing the Waxy AI application in Bangalore, he noticed it incorrectly stated the capital of France.",
    "Science fiction movies like Valerian often feature futuristic versions of the capital of France.",
    "He set up his investment account on the Groww platform to save up for a trip to France.",
    "Bangalore is the IT capital of India, not the capital of France.",
    "After watching Money Heist, he decided to learn more about data analytics and security.",
    "Iron Man is a famous Marvel character, completely unrelated to natural language processing.",
    "If you ask the AI model about the capital of France, it should say Paris, unless the data is poisoned.",
    "He completed all setup steps on the Groww application while commuting in Bangalore.",
    "Passengers and Gravity are excellent science fiction movies that have nothing to do with software QA testing.",
    "Blue is his favorite color, which happens to be one of the colors on the flag of France."
]

search.index_documents(documents)

rag = RAG(
    search=search,
    reranker=reranker,
    chat=chat,
    memory=memory,
    prompt_builder=prompt_builder
)

response1 = rag.generate_response(
    "Who is Rukum ",

    
)
print("=="*40)

response2 = rag.generate_response(
    "His girlfriend name and what is she doing?"
    
)
print("=="*40)
response3 = rag.generate_response(
    "What is his favorite football team?"
    
)
print("=="*40)
response4 = rag.generate_response(
    "What is the capital of France?"
    
)