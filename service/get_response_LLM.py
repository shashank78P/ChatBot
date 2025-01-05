from langchain_google_genai import ChatGoogleGenerativeAI
import json
from typing import List
from pydantic import BaseModel, Field
from constants import GOOGLE_API_KEY

def getResponseLLM(records, summary, question):
    # Pydantic
    class structuredOutput(BaseModel):
        data: str = Field(description="Actual response to query")
        followUpQuestions: List[str] = Field(description="Follow up questions")
        
        class Config:
            arbitrary_types_allowed = True  # Allow arbitrary types
            
    context = ""
    
    i=1
    for record in records:
        context = f"{context} \n Doc {i}: {record['metadata']['content']}"  
        i = i +1
        
    prompt = f"""
        You are Kushi, the personal assistant of Shashank P. Your role is to serve as a chatbot for Shashank P's portfolio. You will help users by providing clear and detailed responses to their queries about Shashank's professional experience, skills, projects, or any other information featured in his portfolio.
        
        Question: {question}
        
        Context: {context}
        
        Chat Summary: {summary}
        
        Instructions:
        1. Respond with accurate and concise information while maintaining a friendly and professional tone.
        2. Your response **must** be formatted strictly in JSON with the following keys:
           - **data**: A string containing the main response to the user's query **in a markup language** (e.g., Markdown). The response should be **brief** and **well-formatted** in **Markdown**, with headings, bullet points, and appropriate line breaks.
           - **followUpQuestions**: An array of strings, each representing a possible follow-up question that the user might ask.
        3. Ensure the JSON is valid and parsable.
        
        Example JSON format:
          "data": "Shashank has worked on the following projects:\n\n* **OrgAttend:** Displays organizational details and key metrics.\n* **Advance ToDo List:** A to-do app with features like task management, secured login, and pagination.\n* **DailyDash:** A chat-based project for group creation and management.\n* **Tutorial Management System:** A system for easy searching of tutorial records.\n* **2Excell (LMS):** A learning management system with robust backend functionalities.",
          "followUpQuestions": ["Follow-up question 1", "Follow-up question 2", "Follow-up question 3]
        
        Respond now:
    """

    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=GOOGLE_API_KEY)
    structured_llm = llm.with_structured_output(structuredOutput)
    message = structured_llm.invoke(prompt)
    return message.dict()