class ABACStudent:
 def __init__(self, student_id, student_name, previous_institute):
     self.student_id = student_id
     self.student_name = student_name
     self.previous_institute = previous_institute
     self.courses = []

 def add_course(self, course_name, grade, credit):
     # Add a new course to the student's course list
     self.courses.append({'name': course_name, 'grade': grade, 'credit': credit})

 def display_gpa(self):
     total_grade_points = 0
     total_credits_earned = 0

     # Define grade points
     grade_points = {
         'A': 4.0,
         'A-': 3.75,
         'B+': 3.25,
         'B': 3.0,
         'B-': 2.75,
         'C+': 2.25,
         'C': 2.0,
         'C-': 1.75,
         'D': 1.0,
         'F': 0.0
     }

     for course in self.courses:
         grade = course['grade']
         credit = course['credit']
         total_grade_points += grade_points.get(grade, 0) * credit
         total_credits_earned += credit

     if total_credits_earned == 0:
         return f"GPA: {0}"
     else:
         return f"GPA: {total_grade_points / total_credits_earned}"

 def display_credits_earned(self):
     total_credits_earned = sum(course['credit'] for course in self.courses)
     return f"Total Credits Earned: {total_credits_earned}"

class MSMEStudent(ABACStudent):
 def __init__(self, student_id, student_name, previous_institute, major, specialization, certificate):
     super().__init__(student_id, student_name, previous_institute)
     self.major = major
     self.specialization = specialization
     self.certificate = certificate

 def display_major(self):
     return f"Major: {self.major}"

 def display_certification(self):
     return f"Certificate: {self.certificate}"

# Example usage for multiple students
student1 = MSMEStudent("6215224", "Sahatsawatt Anankatham", "Melville Senior High-School", "Management Information System", "Database Management", "Django Certified")
student1.add_course("Business Process Management", "C", 3)
student1.add_course("Database System", "C+", 3)
student1.add_course("Principle of Electronic Commerce", "B", 3)
student1.add_course("Programming & Data Structure", "B", 3)
student1.add_course("Information Technology Infrastructure", "C+", 3)

student2 = MSMEStudent("6215367", "John Doe", "Assumption College Samutprakarn", "Accounting", "Auditing", "CPA")
student2.add_course("Taxation", "B-", 3)
student2.add_course("Cost Accounting", "C+", 3)
student2.add_course("Internal Audit & Control", "A-", 3)
student2.add_course("Auditing", "A", 3)
student2.add_course("Financial Report & Financial Statement Analysis", "B+", 3)

# Display information for student1
print(f"Student ID: {student1.student_id}")
print(f"Student Name: {student1.student_name}")
print(f"Previous Institute: {student1.previous_institute}")
print(student1.display_major())
print(student1.display_certification())
print(student1.display_gpa())
print(student1.display_credits_earned())

print("\n")
# Display information for student2
print(f"Student ID: {student2.student_id}")
print(f"Student Name: {student2.student_name}")
print(f"Previous Institute: {student2.previous_institute}")
print(student2.display_major())
print(student2.display_certification())
print(student2.display_gpa())
print(student2.display_credits_earned())