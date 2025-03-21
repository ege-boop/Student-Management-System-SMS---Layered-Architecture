import sqlite3
from student import Student

class StudentData:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade REAL NOT NULL
        )
        ''')
        self.conn.commit()
    
    def add_student(self, student):
        self.cursor.execute('''
        INSERT INTO students (student_id, name, age, grade)
        VALUES (?, ?, ?, ?)
        ''', (student.student_id, student.name, student.age, student.grade))
        self.conn.commit()
    
    def get_students(self):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        students = []
        for row in rows:
            student = Student(row[0], row[1], row[2], row[3])
            students.append(student)
        return students
    
    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0 
