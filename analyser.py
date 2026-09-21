from resume_reader import read_resume
import re

import json
def load_skills():
    

    with open('skills.json', "r") as file:
        return json.load(file)
        


def analyze_resume(file_name,all_skills):
    text=read_resume(file_name)

    skills = []
    
    
    for skill in all_skills:
        for i in skill['aliases']:
            pattern=rf"\b{re.escape(i)}\b"

            if re.search(pattern,text,re.IGNORECASE): 
                skills.append(skill)
                break
    return skills 

def calculate_percentage(detected,all_skills):
    total_skills = len(all_skills)
    matched_skills = len(detected)
    a=(matched_skills/total_skills)*100
    return a

def missing_skills(detected,all_skills):
    detected_skills=[]
    missing=[]
    for skill in detected:
        detected_skills.append(skill['name'])
        
    for skill in all_skills:
        if skill['name'] not in detected_skills:
            missing.append(skill)
        
    return missing
