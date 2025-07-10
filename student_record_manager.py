student_records = {}
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses)
        }
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'")
    else:
        print(f"Student '{name}' not found.")

def is_enrolled(name, course):
    if name in student_records:
        if course in student_records[name]["Course"] :
            return True
        else:
            False
    else:
        print(f"Student '{name}' not found.")
        return False
    
def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    
    grades = student_records[name]["grades"]

    if not grades:
        return 0
    else:
        average_grade = sum(grades) / len(grades)
        return float(average_grade)

def list_students_by_course(course):
    student_in_course = []
    for name , details in student_records.items():
        if course in details["courses"]:
            student_in_course.append(course)
        return student_in_course

def filter_top_students(threshold):
    top_grade_students = []
    for name in student_records:
        avg = calculate_average_grade(name)
        if avg > threshold:
            top_grade_students.append(name)
        else:
            return top_grade_students
        

add_student("Aarya", 20, ["Math", "Physics"])
add_student("Prachi", 22, ["Math", "Biology"])
add_student("Mayuresh", 23, ["Chemistry", "Physics"])
add_grade("Aarya", 90)
add_grade("Aarya", 85)
add_grade("Prachi", 75)
add_grade("Mayuresh", 95)
print(filter_top_students(80))  
print(filter_top_students(90))  
print(filter_top_students(100))    
        