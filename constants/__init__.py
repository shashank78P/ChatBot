import os
from .data import  basicDetails, PreferredWorkLocations, about, educationDetails, skills, raphacureWorkExperience, raphacureResponsibility, dataVectorWorkExperience, dataVectorResponsibility, zedblockWorkExperience, keyModuleWorkedInZedblock, dailyDashProjectIntro, dailyDashAuthModuleFeatures, dailyDashAuthModuleImages, dailyDashQuickAccessModule, dailyDashBookMarkModuleFeatures, dailyDashBookMarkModuleImages, dailyDashChatModuleFeatures, dailyDashChatModuleImages, dailyDashMeetingModuleFeature, dailyDashMeetingModuleImagesVideo, advanceToDoListIntro, advanceToDoListFeatures, advanceToDoListImages, orgAttend, orgAttendFeatures, tutorialManagementSystem, tutorialManagementSystemFeturesImages, orgAttendImages, skillsUsedAtRaphacure, skilledUserdAtDataVector, zedblockResponsibility

# GOOGLE_API_KEY = 'AIzaSyAIsEymX0zgqKjMBTJ84UhQlEq99mhfp5s'
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
OpenAI_Api_Key = os.getenv("OpenAI_Api_Key")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
DIMENSION = os.getenv("DIMENSION")
METRIC = os.getenv("METRIC")
CLOUD = os.getenv("CLOUD")
REGION = os.getenv("REGION")
INDEX_NAME = os.getenv("INDEX_NAME")

__all__ = [GOOGLE_API_KEY, EMBEDDING_MODEL, PINECONE_API_KEY, OpenAI_Api_Key, INDEX_NAME, METRIC, DIMENSION, REGION, CLOUD, basicDetails, PreferredWorkLocations, about, educationDetails, skills, raphacureWorkExperience, raphacureResponsibility, dataVectorWorkExperience, dataVectorResponsibility, zedblockWorkExperience, keyModuleWorkedInZedblock, dailyDashProjectIntro, dailyDashAuthModuleFeatures, dailyDashAuthModuleImages, dailyDashQuickAccessModule, dailyDashBookMarkModuleFeatures, dailyDashBookMarkModuleImages, dailyDashChatModuleFeatures, dailyDashChatModuleImages, dailyDashMeetingModuleFeature, dailyDashMeetingModuleImagesVideo, advanceToDoListIntro, advanceToDoListFeatures, advanceToDoListImages, orgAttend, orgAttendFeatures, tutorialManagementSystem, tutorialManagementSystemFeturesImages, orgAttendImages, skillsUsedAtRaphacure, skilledUserdAtDataVector, zedblockResponsibility ]