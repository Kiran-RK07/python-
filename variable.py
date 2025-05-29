# Variable = A Container For a value(sstring,integer,float,boolan)
# A Variable behave as if it was the value it contains

#STRING (These are strings that act as charcter.It can include Numbers but act as charcter)
first_name = "Kiran" 
food = "Egg Rice"
email = "kiranrk0009@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

#INTERGER (Integer is whole Number)
#NOTE this are whole number make sure that they are not within the codes("") : Then they are technical called as STRINGS
  
age = 23
quantity = 3
num_of_student = 30

print(f"My age is {age}")
print(f"I am buying {quantity} items")
print(f"Number of students {num_of_student} in the class")


#FLOAT (Floating point number. the number contain decimal number comes under float Variable) 

price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance}KM")

#BOOLEAN (Its either TRUE or FALASE. It is must probably used in "if" statement)
#Example
is_student = True
for_sale = True
print(f"Are you a Student?: {is_student}")
print(f"There is a discount for the students {for_sale}")

for_sale = False
if for_sale:
    print("Item is for Sale")
else:
    print("This item is NOT for Sale")
