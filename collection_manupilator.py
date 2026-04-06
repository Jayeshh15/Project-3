print("Student Record Manager")

students = []
subjects_offered = {"Math", "Science", "English", "Computer"}

while True:
    print("\n===== MAIN MENU =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        student = {}

        student["id"] = input("Enter Student ID: ")
        student["name"] = input("Enter Student Name: ")
        student["age"] = input("Enter Student Age: ")
        student["dob"] = input("Enter Student DOB: ")
        student["subjects"] = input("Enter Subjects (comma separated): ")

        students.append(student)

        subject_list = student["subjects"].split(",")
        for sub in subject_list:
            subjects_offered.add(sub)

        print("Student added successfully!")

    # 2. Display All Students
    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for s in students:
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("DOB:", s["dob"])
                print("Subjects:", s["subjects"])
                print("----------------------")

    # 3. Update Student Information
    elif choice == "3":
        sid = input("Enter Student ID to update: ")

        found = 0
        for s in students:
            if s["id"] == sid:
                s["name"] = input("Enter New Name: ")
                s["age"] = input("Enter New Age: ")
                s["dob"] = input("Enter New DOB: ")
                s["subjects"] = input("Enter New Subjects: ")

                subject_list = s["subjects"].split(",")
                for sub in subject_list:
                    subjects_offered.add(sub)

                print("Student updated successfully!")
                found = 1

        if found == 0:
            print("Student not found.")

    # 4. Delete Student
    elif choice == "4":
        sid = input("Enter Student ID to delete: ")

        found = 0
        for s in students:
            if s["id"] == sid:
                students.remove(s)
                print("Student deleted successfully!")
                found = 1
                break

        if found == 0:
            print("Student not found.")

    # 5. Display Subjects Offered
    elif choice == "5":
        print("\nSubjects Offered:")
        for sub in subjects_offered:
            print(sub)

    # 6. Exit
    elif choice == "6":
        print("Thank you for using Student Record Manager!")
        break

    else:
        print("Invalid choice! Please try again.")