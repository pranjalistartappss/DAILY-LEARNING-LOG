students = []   # store all students data

while True:

    print("\n====================================")
    print("Student Result Management System")
    print("====================================")
    print("1. Add Student")
    print("2. View Statistics")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    # EXIT THE PROGRAM
    if choice == 3:
        print("Exiting Program...")
        break

    # ADD STUDENT IN GIVEN INPUT 
    elif choice == 1:

        name = input("Enter Student Name: ")

        subjects = ["English", "Maths", "Science", "Hindi", "Social"]
        marks = []

        # INPUT MARKS
        for subject in subjects:
            mark = int(input(f"Enter {subject} Marks: "))

            if mark < 0 or mark > 100:
                print("Invalid Marks! Try Again.")
                mark = 0   # beginner fix
            marks.append(mark)

        attendance = int(input("Enter Attendance %: "))

        total = 0
        for mark in marks:
            total += mark

        average = total / len(marks)
        percentage = average

        # FAILED SUBJECTS
        failed = 0
        for mark in marks:
            if mark < 35:
                failed += 1

        highest = marks[0]
        lowest = marks[0]

        for mark in marks:
            if mark > highest:
                highest = mark
            if mark < lowest:
                lowest = mark

        # GRADE
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "Fail"

        # RESULT
        if failed == 0:
            result = "PASS"
        else:
            result = "FAIL"

        # STORE STUDENT DATA
        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "attendance": attendance,
            "failed": failed
        }

        students.append(student)

        # DISPLAY RESULT
        print("\n====================================")
        print("RESULT CARD")
        print("====================================")

        print("Name:", name)

        for i in range(len(subjects)):
            print(subjects[i], ":", marks[i])

        print("Total:", total)
        print("Average:", average)
        print("Percentage:", percentage)

        print("Highest:", highest)
        print("Lowest:", lowest)

        print("Attendance:", attendance)
        print("Eligibility:", "Eligible" if attendance >= 75 else "Not Eligible")

        print("Failed Subjects:", failed)
        print("Grade:", grade)
        print("Result:", result)

        print("\nStudents Stored:", len(students))

    # STATISTICS vIEW
    elif choice == 2:

        if len(students) == 0:
            print("No student data available!")
            continue

        total_students = len(students)
        passed = 0
        failed = 0
        total_percentage = 0

        topper = students[0]

        for s in students:

            total_percentage += s["percentage"]

            # pass/fail
            if s["failed"] == 0:
                passed += 1
            else:
                failed += 1

            # topper check
            if s["percentage"] > topper["percentage"]:
                topper = s

        class_average = total_percentage / total_students

        print("\n====================================")
        print("STATISTICS")
        print("====================================")

        print("Total Students:", total_students)
        print("Passed Students:", passed)
        print("Failed Students:", failed)

        print("Class Average:", class_average)

        print("Topper Student:", topper["name"])
        print("Topper Percentage:", topper["percentage"])

    else:
        print("Invalid Choice")