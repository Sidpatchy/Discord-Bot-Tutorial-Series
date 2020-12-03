# A simple calculator by Sidpatchy
# This is apart of my discord bot tutorial series: <link>

print('A basic program for calculating numbers!')
print('1) Add')
print('2) Subract')
print('3) Multiply')
print('4) Divide')

choice = input('Select an option from the list: ')

if choice == '1':
    # Store the user's input in the variables X and Y
    x = input('Insert the first number to be added: ')
    y = input('Insert the second number to be added: ')

    # Calculate the sum, and then print out the sum
    sum = float(x) + float(y)
    print(sum)

elif choice == '2':
    # Store the user's input in the variables X and Y
    x = input('Insert the first number to be subtracted: ')
    y = input('Insert the second number to be subtracted: ')

    # Calculate the sum, and then print out the sum
    sum = float(x) - float(y)
    print(sum)

elif choice == '3':
    # Store the user's input in the variables X and Y
    x = input('Insert the first number to be multiplied: ')
    y = input('Insert the second number to be multiplied: ')

    # Calculate the sum, and then print out the sum
    sum = float(x) * float(y)
    print(sum)

elif choice == '4':
    # Store the user's input in the variables X and Y
    x = input('Insert the first number to be divided: ')
    y = input('Insert the second number to be divided: ')

    # Calculate the sum, and then print out the sum
    sum = float(x) / float(y)
    print(sum)