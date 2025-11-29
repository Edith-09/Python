# def my_function():
#     print("Hello world!")
# my_function()
# def salutation():
#     hello="Good morning Edith!"
#     print(hello)
# salutation()

# def salute(name):
#     print(f"Good afternoon {name}!")
# salute("Edith")
# salute("John")
# salute("Sara")
# def person(name,age,gender):
#     print(f"My name is {name}, I am {age} years old and  I am a {gender}.")
# person("Edith",20,"Female")
# person("John",22,"Male")
# person("Sara",19,"Female")

# def addition(a,b):
#     result=a+b
#     return result
# print("The sum is:", addition(5,3))
# #write a function tha will calculate an individual's BMI


#function to calculate student marks and grade
def add_student(name):
    name=input("Enter student name: ")
    marks=[]
    for i in range(1,4):
        mark=int(input(f"Enter mark {i} for {name}: "))
        marks.append(mark)
        return name,marks
def calculate_average(marks):
    return sum(marks)/len(marks)
def determine_grade(average):   
    if average>=70:
        return "A"
    elif average>=60 and average<70:
        return "B"
    elif average>=50 and average<60:
        return "C"
    elif average>=40 and average<50:
        return "D"
    else:
        return "F"   
def show_results(students):
    print("\n STUDENTS' RESULTS ---")
    print("{'Name':<20} {'Average':<10} {'Grade':<5}")
    print("-" * 35)
    for name, data in students.items():
        print("{:<20} {:<10.2f} {:<5}".format(name, data["average"], data["grade"]))
    print("-" * 35)

# Main program
def main():
    students = {}
    while True:
        name, marks = add_student()
        avg = calculate_average(marks)
        grade = find_grade(avg)
        students.append({'name':name,
                         'average':average,
                         'grade':grade})

        choice = input("Do you want to add another student? (yes/no): ").lower()
        if choice != "yes":
            break

    show_results(students)

# Run the main program
main()   
# def get_grade(average):
#     if 60 <= average <= 69:
#         return 'B'
#     elif 50 <= average <= 59:
#         return 'C'
#     elif 40 <= average <= 49:
#         return 'D'
#     else:
#         return 'F'

# students = []

# while True:
#     name = input("Enter student name: ")
#     marks1 = int(input("Enter first mark: "))
#     marks2 = int(input("Enter second mark: "))
    
#     average = (marks1 + marks2) / 2
#     grade = get_grade(average)
    
#     students.append((name, average, grade))
    
#     more = input("Add another student? : ")
#     if more.lower() != 'y':
#         break

# print("\n--- Results ---")
# for s in students:
#     print(f"Name: {s[0]}, Average: {s[1]:.2f}, Grade: {s[2]}")