print("Hello, World!")
#data types
#integer
age=25
#string
name="John"
#float
height=5.9
#boolean
is_student=True
print(name, "is", age, "and his height is", height, "meters.")
print("Is", name, "a student?", is_student)

#Taking input from user
weight2=input("Enter your weight: ")
name2=input("Enter your name: ")
print(f"My name is {name2} and my weight is {weight2} kgs")

#type conversion
num1=input("Enter first number: ")
num2=input("Enter second number: ")
sum=int(num1)+int(num2)
print("The sum is:", sum)

#Program for student to key in the marks
English=input("Enter your English marks: ")
Maths=input("Enter your Maths marks: ") 
Biology=input("Enter your Biology marks: ")
Chemistry=input("Enter your Chemistry marks: ")
Physics=input("Enter your Physics marks: ")
total_marks=int(English)+float(Maths)+float(Biology)+float(Chemistry)+int(Physics)
print(total_marks)

#user input
num1=input("Enter num1:")
num2=input("Enter num2:")
product=int(num1)*float(num2)
print(product)
name1,name2,name3=input("Enter your three names:").split()
print("Hello your name is :",name1,name2,name3)
first_name=str(input("Enter your first name:"))
second_name=str(input("Enter your second name:"))

print(f"Hello  {first_name} {second_name}")
age=input("Enter your age:")
age=int(age)
next_year_age=age+1
print(next_year_age)
variables
name="Edith"
age=20
favourite_language="Python"
print(f"My name is {name} ,I am {age} years old and my favourite language is {favourite_language}")
#program to calculate age and weight in grams
birth_year=int(input("Enter your year of birth:"))
current_year=int(input("Enter the current year:"))
age=current_year-birth_year
print(age)
#weight conversion
weight_in_kg=float(input("Enter your weight in kilograms:"))
weight_in_grams=weight_in_kg*1000
print(f"Your weight in grams is {weight_in_grams}")