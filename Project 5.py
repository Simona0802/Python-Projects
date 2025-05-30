# Task 1: 
# Write a function that asks the user to enter their age and prints 
# "You are a minor" if the age is less than 18, and "You are of legal age" otherwise.

def check_age():
    try:
        age = int(input("Please enter your age: "))
        if age < 18:
            print("You are a minor.")
        else:
            print("You are of legal age.")
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")

check_age()


# Task 2: 
# Write a program that asks the user to enter a number and create a function that prints 
# whether it is positive, negative, or zero.

def check_number():
    try:
        number = float(input("Please enter a number: "))
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

check_number()


#Task 3: 
# Write a program that asks the user to enter a number and create a function that 
# prints the sum of all numbers from 1 to the entered number.


def sum_to_number():
    try:
        number = int(input("Please enter a positive integer: "))
        if number < 1:
            print("Please enter a positive integer.")
        else:   
            total = sum(range(1, number + 1))
            print(f"The sum of all numbers from 1 to {number} is {total}.")

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# Task 4: 
# Write a program that asks the user to enter text and creates a function that prints the text in reverse order.

def reverse_text():
    text = input("Please enter some text: ")
    reversed_text = text[::-1]
    print(f"The reverse of the entered text is: {reversed_text}")

reverse_text()

# Task 5: 
# Write a program that asks the user to enter a sentence and create a function 
# that calculates the number of vowels (a, e, i, o, u) in the sentence.

def count_vowels():
    sentence = input("Please enter a sentence: ")
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in sentence if char in vowels)
    print(f"The number of vowels in the entered sentence is: {vowel_count}")

count_vowels()

#Task 6: 
# Write a program that asks the user to enter a sentence and create a function that 
# counts the number of occurrences of each letter in the sentence. Ignore case letters.

def count_letter_occurrences(sentence):
    letter_counts = {}
    sentence = sentence.lower()  

    for char in sentence:
        if char.isalpha():  
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts

user_sentence = input("Enter a sentence: ")
result = count_letter_occurrences(user_sentence)

print("Letter occurrences: ")
for letter, count in sorted(result.items()):
    print(f"{letter}: {count}")

# Task 7: 
# Write a program that asks the user to enter a sequence of numbers until they enter a negative number. 
# Create a function that will store the sum of the positive numbers that were entered.

def sum_positive_numbers():
    total = 0
    while True:
        try:
            number = float(input("Enter a number (negative to stop): "))
            if number < 0:
                break
            total += number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return total

positive_sum = sum_positive_numbers()
print(f"The sum of positive numbers is: {positive_sum}")


# BONUS: 
# Write a program that generates a list of random numbers between 1 and 100. Print the largest number in the list.


import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def find_largest_number(numbers):
    return max(numbers)

num_count = 10 
random_numbers = generate_random_numbers(num_count)
print("Random numbers:", random_numbers)
largest_number = find_largest_number(random_numbers)
print("Largest number:", largest_number)