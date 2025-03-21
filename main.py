from student_info import StudentInfo

def display_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def main():
    info = StudentInfo()  
    while True:
        choice = display_menu()
        
        if choice == '1':
            while True:
                student_id = input("Enter Student ID (7 digits): ")
                if len(student_id) == 7 and student_id.isdigit():
                    break
                else:
                    print("Student ID must be exactly 7 digits long and contain only numbers. Please try again.")

            while True:
                name = input("Enter Name: ")
                if name.replace(" ", "").isalpha():  
                    break
                else:
                    print("Name must only contain letters and spaces, no numbers. Please try again.")
            


            while True:
                try:
                    age = int(input("Enter Age: "))
                    if age >= 15:
                        break
                    else:
                        print("Age must be 15 or older. Please enter a valid age.")
                except ValueError:
                    print("Please enter a valid age.")
            
            while True:
                try:
                    grade = float(input("Enter Grade: "))
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Grade must be between 0 and 100. Please enter a valid grade.")
                except ValueError:
                    print("Please enter a valid grade.")
            
            success, message = info.add_student(student_id, name, age, grade)  
            print(message)
            
        elif choice == '2':
            students = info.get_students()
            if not students:
                print("No students.")
            else:
                print("\nStudent List")
                for student in students:
                    print(student)

        elif choice == '3':
            student_id = input("Enter Student ID to delete: ")
            success, message = info.delete_student(student_id)
            print(message)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
