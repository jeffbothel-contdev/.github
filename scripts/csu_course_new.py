from github import Github
from datetime import datetime
import os

# Gathering user input on the courses
term_code = input("Enter the term code: ")
course_code = input("Enter the course code: ")
course_name = input("Enter the course name: ")
start_date = datetime.strptime(input("Enter the start date: "), "%d-%m-%Y")

# Gathering the tasking that is done for each module in the course
tasks = []
#for i in range(1, 8):
#    user_input = input(f"Enter the tasks for Module {i}:")
#    task = user_input.split(" ")
#    tasks.append(task)

# Settings for the script
temp_project = "Temp-CSU-Project"
temp_private = "Temp-CSU-Private"
temp_work = "Temp-CSU-Work"
temp_work_project = "Temp-CSU-Project"
org = "jeffbothel-contdev"

# Defining names for the user in the generation of projects and repos
repo_private = f"CSU-{term_code}-{course_code}-Private"
repo_project = f"CSU-{term_code}-{course_code}-Project"
repo_work = f"CSU-{term_code}-{course_code}-Work"
prjct_private = f"CSU - {term_code} - {course_code}: {course_name}"
temp_project = (f"{org}/{temp_project}")
temp_private = (f"{org}/{temp_private}")
temp_work = (f"{org}/{temp_work}")
temp_work_project = (f"{org}/{temp_work_project}")

# Get the authenticaitons for use
g = Github(os.environ.get('JEFF_ALL_ACCESS'))
org = g.get_organization("jeffbothel-contdev")

# Display the names for the courses
