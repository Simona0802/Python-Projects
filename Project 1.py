

#To create a program in which the user enters 2 numbers and checks if the sum is less than 100

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

sum_of_numbers = number1 + number2
print(f'Your sum is {sum_of_numbers}')
if sum_of_numbers <100:
    print('This sum is less than 100')
else:
    print('This sum is greater than 100') 
    


#To create a program in which the user enters the year of birth, 
# to calculate how old he is and to determine whether he is a minor or an adult


from datetime import datetime

year_of_birth = int(input('Enter the year of your birth: '))
current_year = datetime.now().year
age = current_year - year_of_birth
if age <18:
    print(f'This person is minor. You are {age}')
else:
    print(f'This person is adult. You are {age}') 


#To create a program in which the user enters the sides of two rectangles, 
# calculates the area and checks which rectangle is larger

for i in range(2):
    lenght1 = int(input('Enter the lenght for the first rectangle: '))
    wight1 = int(input('Enter the wight of the first rectangle: '))

    lenght2 = int(input('Enter the lenght of the second rectangle: '))
    wight2 = int(input('Enter the wight of the second rectangle: '))

    rectangle1 = lenght1*wight1
    rectangle2 = lenght2*wight2

    print(f'Dimensions of first rectangle {rectangle1}: ')
    print(f'Dimensions of secont rectangle {rectangle2}: ')
    if rectangle1 > rectangle2:
        print('First rectangle is larger')
    elif rectangle1 < rectangle2:
        print('Second rectangle is larger') 
    else:
        print('Both rectangles are the same')
        

#To create a program in which the user enters the sizes of the angles of the triangles, 
# and to check whether a triangle can be created with those sizes (the sum should be 180)

print('Enter the angles of the triangle: ')
a = int(input('Enter the first angle: '))
b = int(input('Enter the second angle: '))
c = int(input('Enter the third angle: '))
dimensions = a+b+c 
valid_triangle = a+b+c == 180 
print(f'Your triangle has {dimensions} sum ')

if valid_triangle:
    print('Triangle is valid')
else:
    print('Triangle not valid')    


#To create a program in which the user enters a number and checks whether that number is even or not

number = int(input('Enter your number: '))
while number % 2 ==0:
    print('Your number is even ')
else:
    print('Your number is odd')
   