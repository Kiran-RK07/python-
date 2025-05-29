#input() = It always returns data as a String

name = input("What is your name? ")
age = int(input("How old are you? ")) #If we want number to be included we can use "int" in the starting.

age = age + 1

print(f"Hello {name}! ")
print("HAPPY BRITHDAY!!")
print(f"Your {age} year old")

#Exersice Calculate Area of Rectangle.

length = float(input("Enter the lenght? "))
width = float(input("Enter the width? "))

total = length * width

print(f"Area of Rectangle is : {total}cm²") #To Get the sqaure sign Numlock must on and press Alt + 0178
