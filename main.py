import os
from dotenv import load_dotenv
load_dotenv()

from dbConnect import get_db_instance
from flask import Flask, request, jsonify
from constants import INDEX_NAME
from service import textDataHandler, getResponseLLM, getSummary
from embedding import generate_embedding 
from constants import basicDetails, PreferredWorkLocations, about, educationDetails, skills, raphacureWorkExperience, raphacureResponsibility, dataVectorWorkExperience, dataVectorResponsibility, zedblockWorkExperience, keyModuleWorkedInZedblock, dailyDashProjectIntro, dailyDashAuthModuleFeatures, dailyDashAuthModuleImages, dailyDashQuickAccessModule, dailyDashBookMarkModuleFeatures, dailyDashBookMarkModuleImages, dailyDashChatModuleFeatures, dailyDashChatModuleImages, dailyDashMeetingModuleFeature, dailyDashMeetingModuleImagesVideo, advanceToDoListIntro, advanceToDoListFeatures, advanceToDoListImages, orgAttend, orgAttendFeatures, tutorialManagementSystem, tutorialManagementSystemFeturesImages,  skillsUsedAtRaphacure, skilledUserdAtDataVector,   skillsUsedAtRaphacure, skilledUserdAtDataVector, orgAttendImages,zedblockResponsibility, GOOGLE_API_KEY
from flask_cors import CORS
import uuid 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

vectorStore = get_db_instance()
namespace="portfolio-chat-bot"
chatHistorySummary = {}


# @app.route("/insert-data",  methods=['GET'])
# def insertData():
#     textDataHandler(
#         content=basicDetails,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Basic Personal Details"},
#         context="Basic Details | Personal Details | Profile Details | Contact Details Social Media Details"
#     )
#     textDataHandler(
#         content=PreferredWorkLocations,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Preffered Work Location"},
#         context="Preffered Work Location"
#     )
#     textDataHandler(
#         content=about,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "About Section"},
#         context="About"
#     )
#     textDataHandler(
#         content=educationDetails,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Educational Details"},
#         context="Educational Details"
#     )
#     textDataHandler(
#         content=skills,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Skills Section"},
#         context="Skills | Technical Skills | Technologies known"
#     )
#     textDataHandler(
#         content=raphacureWorkExperience,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Raphacure: Work Experience", "company": "Raphacure"},
#         context="Raphacure | Work Expericene | Raphacure Work Experience | Cure And Card Pvt. Ltd | Node.js Developer | Work from Office | Professional Project"
#     )
#     textDataHandler(
#         content=raphacureResponsibility,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Raphacure: Role and responsilbility", "company": "Raphacure"},
#         context="Raphacure | Role and responsilbility | Node.js Developer | Work from Office | Professional Project"
#     )
#     textDataHandler(
#         content=skillsUsedAtRaphacure,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Skills", "company": "Raphacure"},
#         context="Raphacure | Skills | Technologies Worked On"
#     )
#     textDataHandler(
#         content=dataVectorWorkExperience,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Work Experience: DataVector Tech Pvt. Ltd", "company": "Datavector"},
#         context="Datavector: Work Experience: Datavector Tech Pvt. Ltd: Software Engineer Trainee: Work from Home: 2Excell (Learning Management System): Professional Project"
#     )
    
#     textDataHandler(
#         content=dataVectorResponsibility,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Roles and Responsibilty", "company" : "Datavector"},
#         context="Datavector | Roles and Responsibilty"
#     )
    
#     textDataHandler(
#         content=skilledUserdAtDataVector,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Skills", "company" : "Datavector"},
#         context="Datavector | Skills | Technologies worked on"
#     )
    
#     textDataHandler(
#         content=zedblockWorkExperience,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Work Experience: Zedblock Technology"},
#         context="Zedblock | Work Experience | MERN Stack Developer Intern | Work from Home | Professional Project"
#     )
    
#     textDataHandler(
#         content=zedblockResponsibility,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Work Experience", "company": "Zedblock"},
#         context="Zedblock | Roles and Responsibility"
#     )
    
#     textDataHandler(
#         content=keyModuleWorkedInZedblock,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Key modules worked on: Zedblock Technology"},
#         context="Zedblock | key modules | Worked On"
#     )
    
#     textDataHandler(
#         content=dailyDashProjectIntro,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | DailyDash | Introduction"
#     )
    
#     textDataHandler(
#         content=dailyDashAuthModuleFeatures,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Authentication and User Management"},
#         context="Project | DailyDash | Authentication and User Management Module"
#     )
    
#     textDataHandler(
#         content=dailyDashAuthModuleImages,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Authentication and User Management"},
#         context="Project | DailyDash | Authentication and User Management Module Images"
#     )
    
#     textDataHandler(
#         content=dailyDashQuickAccessModule,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Quick Access"},
#         context="Project | DailyDash | Quick Access Module"
#     )
    
#     textDataHandler(
#         content=dailyDashBookMarkModuleFeatures,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "BookMark"},
#         context="Project | DailyDash | Bookmark Module"
#     )
    
#     textDataHandler(
#         content=dailyDashBookMarkModuleImages,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "BookMark"},
#         context="Project | DailyDash | Bookmark Module Images"
#     )
    
#     textDataHandler(
#         content=dailyDashChatModuleFeatures,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Chat"},
#         context="Project | DailyDash | Chat Module Features"
#     )
    
#     textDataHandler(
#         content=dailyDashChatModuleImages,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Chat"},
#         context="Project | DailyDash | Chat Module Images"
#     )
    
#     textDataHandler(
#         content=dailyDashMeetingModuleFeature,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Meeting"},
#         context="Project | DailyDash | Meeting Module Feature"
#     )
    
#     textDataHandler(
#         content=dailyDashMeetingModuleImagesVideo,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project", "module": "Meeting"},
#         context="Project | DailyDash | Meeting Module Images and video"
#     )
    
#     textDataHandler(
#         content=advanceToDoListIntro,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | Advance ToDo List | Introduction"
#     )
#     textDataHandler(
#         content=advanceToDoListFeatures,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | Advance ToDo List | Feature"
#     )
#     textDataHandler(
#         content=advanceToDoListImages,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | Advance ToDo List | Images"
#     )
    
#     textDataHandler(
#         content=orgAttend,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | OrgAttend | Introduction"
#     )
    
#     textDataHandler(
#         content=orgAttendFeatures,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | OrgAttend | Feature"
#     )
#     textDataHandler(
#         content=orgAttendImages,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | OrgAttend | Images"
#     )
    
#     textDataHandler(
#         content=tutorialManagementSystem,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | Tutorial Management System | Introduction"
#     )
#     textDataHandler(
#         content=tutorialManagementSystemFeturesImages,
#         vectorStore=vectorStore,
#         namespace=namespace,
#         metadata ={"sectionName": "Personal Project"},
#         context="Project | Tutorial Management System | Images | Features"
#     )
    
#     return jsonify({
#         "error": False,
#         "message": "Inserted successfully!.",
#     })
    
@app.route("/get-response", methods=["POST"])
def getData():
    question = request.get_json().get("question")
    chatId = request.get_json().get("chatId", None)
    
    print(chatId)
    
    if chatId is None:
        chatId = uuid.uuid1()
        
    print("\n\n\n\n")
    print("chatId")
    print(chatId)
    
    summary = chatHistorySummary.get(chatId) if chatHistorySummary.get(chatId) else ""
        
    print("\n")
    print(question)
    embedding = generate_embedding([question])
    print("\n\n\n\n")
    print(len(embedding))
    # print(embedding)
    embd = embedding[0]
    response = vectorStore.query(
            namespace=namespace,
            vector= embd,
            top_k=10,
            include_values=False,
            include_metadata=True,
    ).to_dict()
    
    print(response)
    if response is None:
        return jsonify({"success": False, "message": "I couldn't find any answers to your question. Can you clarify or provide more context so I can better assist you?."})
    
    output = getResponseLLM(response['matches'], summary, question)
    print("\n\n\n")
    print(output)
    revisedSummary = getSummary(previousSummary=summary,currentResponse=response['matches'], currentQuestion=question)
    print("\n\n\n")
    print("revisedSummary")
    print(revisedSummary)
    chatHistorySummary[chatId] = revisedSummary
    return jsonify({ "success": True, "data": output.get("data"), "followUpQuestion": output.get("followUpQuestions"), "chatId": chatId})

if __name__ == '__main__':
    app.run(debug=True)
    