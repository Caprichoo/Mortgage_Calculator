print('**Welcome to Mortgage Calculator**')
salary = float(input("What's your salary? "))
if salary > 2000:
    print("You're eligible for mortgage")
    rate = 0
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
else:
    print("You're not eligible for mortgage")
