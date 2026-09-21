from analyser import load_skills, analyze_resume, calculate_percentage, missing_skills
from tkinter import Tk, filedialog

def main():
    
    root = Tk()
    root.withdraw()

    file_name = filedialog.askopenfilename(
        title="Select Your Resume",
        filetypes=[
            ("Resume Files", "*.pdf *.txt"),
            ("PDF Files", "*.pdf"),
            ("Text Files", "*.txt")
        ]
    )

    root.destroy()

    if not file_name:
        print("No file selected")
        return 

    try:
        all_skills=load_skills()
        detected = analyze_resume(file_name,all_skills)
        missing=missing_skills(detected,all_skills)
    except ValueError as e:
        print(e)
        return
    

    

    grouped_missing=display_by_category(missing)

   

    grouped=display_by_category(detected)      
    print('='*20)
    print('RESUME SKILL ANALYZER')
    print('='*20)


    print('Detected skills')
    print('-'*10)

    for category,skills in grouped.items():
        print(category)
        for i in skills:
            print('✓ ',i)
        print(' ')

    print('Missing skills/Recommended skills')
    print('-'*10)

    display_missing(grouped_missing)
    print('-'*10)

    print('Summary')
    print('-'*10)
    display_summary(all_skills,detected,missing)


def display_summary(all_skills,detected,missing):
    print('Total skills    :',len(all_skills))
    print('Detected skills :',len(detected))
    print('missing skills  :',len(missing))
    print('Match Percentage:',f'{calculate_percentage(detected,all_skills):.2f}%')

def display_missing(grouped_missing):
    for cat,skills in grouped_missing.items():
        print(cat)
        for skill in skills:
            print('✓',skill)
        print('')

def display_by_category(skills):
    d={}
    for i in skills:
        category=i['category']
        if category in d:
            d[category].append(i['name'])
        else:
            d[category]=[i['name']]
    return d   

if __name__=="__main__":
    main()