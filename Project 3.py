
#1. Find the Maximum in a List
#Problem: Write a program to find the largest number in a list.

#Create a list with 15 numbers.
#Find the largest number
#Bonus: Try to use a loop to find the largest number.
#Display the largest number with a message.

numbers15 = [74, 23, 86, 51, 9, 68, 37, 92, 45, 17, 30, 63, 81, 56, 12]

max_number = numbers15[0]

for number in numbers15:
    if number > max_number:
        max_number = number

print(f"The largest number in the list is: {max_number}")

#2. Count Occurrences of an Element
#Problem: Write a program to count how many times a specific element appears in a list.

#Ask the user to input which number wants to count how many times is in the list
#Display the result.

numbers_count = [74, 23, 86, 51, 9, 68, 37, 92, 45, 17, 30, 63, 81, 56, 12, 23, 86, 23]

user_input = int(input("Enter the number you want to count: "))

count = 0
for number in numbers_count:
    if number == user_input:
        count += 1

print(f"The number {user_input} appears {count} time(s) in the list.")

#3. Filter Even and Odd Numbers
#Problem: Write a program that separates a list into even and odd numbers.

#Use a loop to ask the user to input 10 numbers and add them to a list.
#Use a loop to iterate through the list and separate even and odd numbers into two new lists.
#Display the even numbers and odd numbers.

number_entered = []
even_numbers = []
odd_numbers = []

print('Please enter 10 numbers: ')
for number_entered in range(10):
    num = int(input('Please enter a number: '))
    number_entered.append(num)

for num in number_entered:
    if num % 2 ==0:
        even_numbers.append(num)
else:
    odd_numbers.append(num)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")


#5. Calculate the Average of a List
#Problem: Write a program to calculate the average of a list of numbers.

#Ask the user to input a list of numbers.
#Use a loop to calculate the sum of the numbers.
#Divide the sum by the total number of elements to get the average.
#Display the result.

user_input = input('Enter a list of numbers: ')
numbers = [int(num) for num in user_input.split()]

total_sum = 0
for number in numbers:
    total_sum += number

average = total_sum / len(numbers)

print(f'The average of your number is {average}')

#6. Remove Duplicates from a List
#Problem: Write a program to remove duplicate elements from a list.

#Ask the user to input a list of numbers.
#Display the list without duplicates.

input_user = input('Enter a list of numbers: ')
numbers = [int(num) for num in input_user.split()]

unique_numers = list(set(numbers))

print(f'The list without duplicates {unique_numers}')


#7. Shopping List Manager
#Problem: Write a program to manage a list of items to buy.

#Start with an empty list.
#Use a loop to ask the user to input the product and the price
#Store the product in the list (Bonus if you store the price in another list
#Display the final list and how much the user has to pay.

product = []
price = []

while True:
    product = input("Enter the product name (or type 'done' to finish): ")
    if product.lower() == 'done':
        break  
    price = float(input(f"Enter the price for {product}: "))
    
    product.append(product)
    price.append(price)

total_price = sum(price)

print('Your Shopping List: ')
for i in range(len(product)):
    print(f"{product[i]} - ${price[i]:.2f}")

print(f"Total amount to pay: 1
    {total_price:.2f}")