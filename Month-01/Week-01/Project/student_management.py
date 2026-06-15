student_count = 0

while True:

    print("1. Add Student")
    print("2. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 2:
        break

    elif choice == 1:

        name = input("Enter Student Name: ")

        subjects = ["English", "Maths", "Science", "Hindi", "Social"]

        marks = [0, 0, 0, 0, 0]
        for i, subject in enumerate(subjects):
            
            mark = int(input(f"Enter {subject} Marks: "))
            if mark < 0 or mark > 100:
                print("Invalid Marks")
                continue
            marks[i] = mark
        attendance = int(input("Enter Attendance: "))

        total = 0

        for mark in marks:
            total = total + mark

        average = total / 5
        percentage = average

        failed = 0

        for mark in marks:
            if mark < 35:
                failed = failed + 1

        highest = marks[0]
        lowest = marks[0]

        for mark in marks:

            if mark > highest:
                highest = mark

            if mark < lowest:
                lowest = mark

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

        if attendance >= 75:
            eligibility = "Eligible"

        else:
            eligibility = "Not Eligible"

        if failed == 0:
            result = "PASS"

        else:
            result = "FAIL"

        print("\nRESULT")

        print("Name :", name)

        print("Marks")

        for i, mark in enumerate(marks, start=1):
            print("Subject", i, ":", mark)

        print("Total :", total)
        print("Average :", average)
        print("Percentage :", percentage)

        print("Highest :", highest)
        print("Lowest :", lowest)

        print("Attendance :", attendance)
        print("Eligibility :", eligibility)

        print("Failed Subjects :", failed)

        print("Grade :", grade)
        print("Result :", result)

        student_count = student_count + 1

        print("Students Processed :", student_count)

    else:
        print("Invalid Choice")