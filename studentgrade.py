def add_student():
    name = input("Enter student's name: ")
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter mark {i} for {name}: "))
        marks.append(mark)
    return name, marks


def calculate_average(marks):
    return sum(marks) / len(marks)


def determine_grade(avg):
    if avg >= 70:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'


def show_results(students):
    print("\n Student Results ")
    for student in students:
        print(f"{student['name']} - Average: {student['average']:.2f}, Grade: {student['grade']}")


def main():
    students = []
    while True:
        name, marks = add_student()
        average = calculate_average(marks)
        grade = determine_grade(average)
        students.append({'name': name, 'average': average, 'grade': grade})

        cont = input("Add another student? (yes/no): ").lower()
        if cont != 'yes':
            break

    show_results(students)


main()