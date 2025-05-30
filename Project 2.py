
#1. Login Simulation
#Problem: Write a program that simulates a login system.

#Create variables that will store the username and password.
#Allow the user to enter their credentials.
#If they enter the wrong credentials, give them three attempts to log in.
#If they fail three times, display a message: "Account locked."
#If they log in successfully, display: "Welcome, [username]!"

username = 'Simona'
password = 'Simona123'

max_attempts = 3
attempts = 0  

while attempts < max_attempts:
    username_input = input('Insert your username: ')
    passweord_input = input('Insert your password: ')

    if username == username_input and password == passweord_input:
        print(f'Welcome {username_input}')
        break
    else:
        attempts += 1 
        print(f' Invalid credentials. You have {max_attempts - attempts} attempts left. ')
else: 
    print('Account locked!')




#2. ATM Simulation
#Problem: Write a program that simulates a simple ATM system.

#Start with an account balance of 5000.
#Display options for the user:
#Check balance
#Deposit money
#Withdraw money
#Exit
#Use a loop to keep showing the menu until the user selects "Exit".
#If the user tries to withdraw more money than the balance, display an error message: "Insufficient funds."
#After each transaction, display the updated balance.

account_balance = 5000 

def atm_menu ():
    print('ATM Menu: \n')
    print('1. Check balance: ')
    print('2. Deposit money: ')
    print('3. Withdraw money: ')
    print('4. Exit: ')

while True: 
    atm_menu()
    choice = input('Enter your choice from 1 to 4: ')
    if choice == '1':
        print(f'Your account balance is {account_balance}. ')
    elif choice == '2':
        try:
            deposit_amount = float(input('Enter the amount of the deposit: '))
            if deposit_amount > 0:
                account_balance += deposit_amount
                print(f'{deposit_amount} has been deposited.')
                print(f'Update balance {account_balance}')
            else: 
                print('Invalid amount. Please enter a positive value. ')
        except ValueError:
            print('Invalid input. Please enter numeric value')
    elif choice =='3':
        try:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount > account_balance:
                print("Insufficient funds.")
            elif withdraw_amount > 0:
                account_balance -= withdraw_amount
                print(f"${withdraw_amount} has been withdrawn.")
                print(f"Updated balance: ${account_balance}")
            else:
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")



#3. Sum of Numbers
#Problem: Write a program that calculates the sum of numbers entered by the user.

#Use a loop to keep asking the user for numbers.
#If the user enters "0", stop the loop and display the total sum of the numbers entered.

total_sum = 0 
print('Enter numbers to add to the sum. Enter 0 to stop. ')

while True: 
    try: 
        number = float(input('Enter a number: '))
        if number == 0:
            break

        total_sum += number
    except ValueError:
        print('Invalid input. Please enter a numeric number! ')

print(f'Total sum of number entered is {total_sum}')


#Bonus. Number Pattern
#Problem: Write a program that prints a number pattern based on user input.

#Ask the user to input a number n.
#Use nested loops to print the following pattern:

n = int(input("Enter the number of rows for the pattern: "))

for i in range(1, n + 1):  
    for j in range(1, i + 1): 
        print(j, end=" ")  
    print() 