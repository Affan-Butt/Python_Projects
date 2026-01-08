courses = {
    "Python": {"seats": 3, "students": []},
    "AI": {"seats": 2, "students": []},
    "Web": {"seats": 1, "students": []}
}

print("Welcome to Online Courses")

while True:
    print("\nMenu:")
    print("1. View Courses")
    print("2. Enroll Student")
    print("3. Drop Course")
    print("4. View Enrolled Students")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        for course, data in courses.items():
            print(f"{course} - Seats Left: {data['seats']}")

    elif choice == "2":
        course_name = input("Enter course name: ")
        student_name = input("Enter student name: ")

        if course_name in courses:
            if courses[course_name]["seats"] > 0:
                courses[course_name]["students"].append(student_name)
                courses[course_name]["seats"] -= 1
                print(f"{student_name} enrolled in {course_name}")
            else:
                print("No seats available")
        else:
            print("Course not found")

    elif choice == "3":
        course_name = input("Enter course name: ")
        student_name = input("Enter student name: ")

        if course_name in courses and student_name in courses[course_name]["students"]:
            courses[course_name]["students"].remove(student_name)
            courses[course_name]["seats"] += 1
            print(f"{student_name} dropped from {course_name}")
        else:
            print("Student or course not found")

    elif choice == "4":
        course_name = input("Enter course name: ")

        if course_name in courses:
            print(
                f"Enrolled Students in {course_name}: {courses[course_name]['students']}")
        else:
            print("Course not found")

    elif choice == "5":
        print("Thank you for using Online Course System")
        break

    else:
        print("Invalid option, try again ")
