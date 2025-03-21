from student_data import StudentData
from student import Student

class StudentInfo:
    def __init__(self):
        self.data = StudentData()  
    
    def add_student(self, student_id, name, age, grade):
        if age <= 15:
            return False, "Age must be greater than 15."
        
        if grade < 70:
            return False, "Grade must be greater than or equal to 70."
        
        student = Student(student_id, name, age, grade)
        
   
        try:
            self.data.add_student(student)  
            return True, "Student added successfully."
        except Exception as e:
            return False, f"Error adding student: {str(e)}"

    def get_students(self):
        
        try:
            return self.data.get_students()
        except Exception as e:
            return [], f"Error retrieving students: {str(e)}"

    def delete_student(self, student_id):
        try:
            if self.data.delete_student(student_id):
                return True, "Student deleted successfully."
            else:
                return False, "Student not found."
        except Exception as e:
            return False, f"Error deleting student: {str(e)}"
