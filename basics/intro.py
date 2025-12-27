#PYTHON 
print("This is a practice run")

# Variables: hold different data types like:
# string = text
name = "Angela"
print(f"Hello, I'm {name}")
# integer = whole numbers
age = 14
print(f"I am {age} years old")
# float = decimal numbers
price = 8.99
print(f"The price is ${price} for your drink")
# boolean = True/False values
is_student = True
print(f"Are you a student?: {is_student}")

# If/Else conditions
if is_student == False:
    print("you are not allowed in this school")
else:
    print("you may enter")

#Typecasting: converting a variable from one datatype to anther
gender = 'female'
age = 18
gpa = 3.5

print(type(age))

age = str(age)
print(type(age))

#Input function
question = input("What is your name?: ")
age = int(age)
age = age * 2
print(f"Hello {question}!" + f" You're {age} years old" + f". I am also {age} years old!")
print("Just kidding!")
#you can also do it easier with less code:
agequestion = int(input("how old are you really? "))
print(f"You are {agequestion} years old! Thats cool")

#Practise Exercise
print("I will be calculating the length of rectange for you!")
print("But in order to do so, I will need to ask you some questions!")
intro = input("Are you ready? Type yes or no.  ")
if intro == "yes":
    w = float(input("What is the width? "))
    l = float(input("What is the length? "))
    a = w*l
    print(f"THe length of the rectange is {a}")
elif intro == "no":
    print("Ohk thats alright, thank you for your time:) ")
else:
    print("response unknown. please reply exactly as we asked")