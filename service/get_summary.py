from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from constants import GOOGLE_API_KEY

def getSummary(previousSummary, currentResponse, currentQuestion):
    prompt = f"""
        You are a helpful assistant that summarizes conversations. Given the following inputs:

        Previous Chat Summaries: {previousSummary}
        Current Question: {currentQuestion}
        Current Response: {currentResponse}
        Your task is to generate a concise and clear summary of the entire conversation, including both the previous summaries and the most recent exchange. The summary should reflect the flow of the conversation and capture key information in a coherent manner.
        Just given only summary don't add extra details.
    """
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=GOOGLE_API_KEY)
    message = HumanMessage(content=prompt)
    summary = llm([message])
    return summary.content
    