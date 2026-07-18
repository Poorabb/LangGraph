from langgraph.graph import StateGraph, START,END 
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Literal, Annotated
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import InMemorySaver 
from langchain_core.messages import HumanMessage

# Load Environment
load_dotenv()

# Define LLM model 
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# Define State for LangGraph app
class LLMstate(TypedDict):
    message: Annotated[list[BaseMessage],add_messages]

# Make Graph Node for chatting with LLM 
def chat_node(state: LLMstate):
    message = state["message"]
    response = llm.invoke(message)
    return {'message':[response]}

# Memory checkpoint
checkpointer = InMemorySaver()

# Define Graph
graph = StateGraph(LLMstate)

# add Graph node
graph.add_node("chat_node",chat_node)

# Add graph edge
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

# Call graph
chatbot = graph.compile(checkpointer = checkpointer)



# CODE FOR STREAMING THE OUTPUT

# stream = chatbot.stream(
#     {'message':[HumanMessage(content="What is streaming in langgraph")]},
#     config = {'configurable':{"thread_id":"1"}},
#     stream_mode = "messages"
# )

# for message_chunk, metadata in stream:
#     if message_chunk.content:
#         print(message_chunk.content, end = "",flush= True)
