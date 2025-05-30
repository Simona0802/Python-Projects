#1. To create a dictionary with 3 elements of your choice and to print the last element

book_info = {
    "title": "1984",
    "author": "George Orwell",
    "published_year": 1949
}

print(book_info["published_year"])


#2. To create an empty dictionary, the user must enter 2 numbers that will be added to the dictionary. 
# To perform the 4 basic mathematical operations and to add the results to the dictionary in different keys

operations_dictionary = {}

operations_dictionary ['number1'] = int(input('Enter the first number: '))
operations_dictionary ['number2'] = int(input('Enter the second number: '))

operations_dictionary = operations_dictionary ["number1"] + operations_dictionary ["number2"] 
operations_dictionary = operations_dictionary ["number1"] - operations_dictionary ["number2"] 
operations_dictionary = operations_dictionary ["number1"] * operations_dictionary ["number2"] 
operations_dictionary = operations_dictionary ["number1"] / operations_dictionary ["number2"] 

print(operations_dictionary)

#3. To create a program in which the user can enter personal data and grades for a certain student, 
# to enter the name of the subject and the grades. Site data to be saved in the dictionary. 
# Once all the data have been entered, the student's average will be calculated and printed. 
# *Bonus: adapt the program so that it can work for the whole class, not just for one student

class_data = {}

while True:
    student_name = input("Enter the student's name (or type 'done' to finish): ")
    if student_name.lower() == "done":
        break

student_data = {}
subjects = {}

while True:
    subject_name = input(f"Enter a subject for {student_name} (or type 'done' to finish): ")
    if subject_name.lower() == "done":
        break
    grades = input(f"Enter the grades for {subject_name}, separated by commas: ")
    grades = [float(grade) for grade in grades.split(",")]
    subjects[subject_name] = grades

student_data["subjects"] = subjects

total_grades = sum(sum(grades) for grades in subjects.values())
total_count = sum(len(grades) for grades in subjects.values())
student_data["average"] = total_grades / total_count if total_count != 0 else 0

class_data[student_name] = student_data

print("Class Data:")
for student, data in class_data.items():
    print(f"Student: {student}")
    for subject, grades in data["subjects"].items():
        print(f"Subject: {subject}, Grades: {grades}")
    print(f"Average Grade: {data['average']:.2f}")


#4. To create a program that will be useful in some store. 
# To create a dictionary that has 2 indexes, products, prices, and data that has empty lists. 
# The user can enter products and prices of the products until he chooses that he wants to enter more.
#  When he stops importing products, how much he has to pay will be calculated and stored in a new index. 
# To give the option to the user to pay, to calculate whether the change should be returned or not. 
# If it needs to be saved in the dictionary, # it needs to be returned. If you do not need to remember that the bill 
# has been paid.

store_data = {
    "products": [],
    "prices": [],
    "total_cost": 0,
    "change": None,
    "status": None
}

while True:
    product = input("Enter the product name (or type 'done' to finish): ")
    if product.lower() == "done":
        break
    price = float(input(f"Enter the price for {product}: "))

store_data["products"].append(product)
store_data["prices"].append(price)

store_data["total_cost"] = sum(store_data["prices"])
print(f"The total cost is: ${store_data['total_cost']:.2f}")

while True:
    payment = float(input("Enter the amount paid: "))
    if payment >= store_data["total_cost"]:
        store_data["change"] = payment - store_data["total_cost"]
        store_data["status"] = "Paid"
        print(f"Payment successful. Change to return: {store_data['change']:.2f}")
        break
    else:
        print("Insufficient payment. Please try again.")

print("Final store data:")
print(store_data)