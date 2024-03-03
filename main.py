print('**Welcome to Mortgage Calculator**')
try:
    salary = int(input("What's your salary? "))
except:
    print("Please enter a int value")
    salary = int(input("What's your salary? "))

    #If you made an error in try and except block, the code doesn't goes to else part.

else:
    rate = 0
    if salary > 2000:
        print("You're eligible for mortgage")
        credit_score = int(input("What's your credit score? "))
        if credit_score > 800:
            rate = 4
            print(f'Interest rate is {rate}%')
        elif credit_score > 750:
            rate = 6
            print(f'Interest rate is {rate}%')
        else:
            rate = 8
            print(f'Interest rate is {rate}%')
    disable = input("Disabled? Type Y for Yes and N for No.")
    if disable == 'Y':
        rate -= 2
        print(f'Final interest rate is {rate}%')
    else:
        print(f'Final interest rate is {rate}%')
    #else:
        #print("Sorry, you're not eligible for mortgage")
finally:
    print("Thanks for using our calculator")
