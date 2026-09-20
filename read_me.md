# Resume Skill Analyzer

A simple Python-based CLI tool that analyzes a resume and identifies the skills present in it. It compares the detected skills against a predefined skill list and shows the skill match percentage along with missing skills that can be considered as learning recommendations.

## Features

* Accepts a resume filename from the user
* Reads skills from a predefined `skills.txt` file
* Detects skills mentioned in the resume
* Calculates the skill match percentage
* Identifies missing skills
* Displays missing skills as recommended skills
* Handles invalid resume filenames
* Provides a clean command-line interface

## Technologies Used

* Python
* File Handling
* Functions
* Modules and Imports
* Lists and Sets
* String Processing
* Exception Handling

## How It Works

1. The program asks the user for the resume filename.
2. It loads the predefined skills from `skills.txt`.
3. The resume is read as a text file.
4. Each predefined skill is searched for in the resume.
5. Detected skills are stored and displayed.
6. The program calculates the percentage of matched skills.
7. Skills that are not detected are identified as missing skills.
8. Missing skills are displayed as recommended skills for further learning.

## Project Structure

```text
resume-skill-analyzer/
│
├── main.py
├── analyser.py
├── skills.txt
├── sample_resume.txt
└── README.md
```

## Example `skills.txt`

```text
Python
SQL
Pandas
NumPy
Git
Flask
```

## How to Run

Clone the repository and open the project folder in a terminal.

Run:

```bash
python main.py
```

Enter the name of your resume text file when prompted.

For example:

```text
Enter Your File name: sample_resume
```

The program automatically adds `.txt` if it is not provided.

## Sample Output

```text
====================
RESUME SKILL ANALYZER
====================

Detected skills
----------
✓ Python
✓ SQL
✓ Pandas
✓ NumPy
✓ Git

Missing skills/Recommended skills
----------
1.Flask

Summary
----------
Total skills    : 6
Detected skills : 5
missing skills  : 1
Match Percentage: 83.33%
```

## Limitations

This project uses predefined skills and simple text matching. It does not currently understand the context of a skill, synonyms, skill proficiency, job descriptions, or resume formats such as PDF and DOCX.

## Future Improvements

* Support PDF and DOCX resumes
* Add job-description matching
* Improve skill matching using NLP techniques
* Rank missing skills based on job requirements
* Add a graphical web interface
* Add machine-learning-based resume classification

## Purpose

This project was built as a practical Python project to demonstrate file handling, modular programming, data processing, exception handling, and basic text analysis.
