#1
def greet_user(name):
    print("გამარჯობა, {}! კეთილი იყოს თქვენი მობრძანება!".format(name))
greet_user("ნინო")
#2
def sum_of_numbers(numbers):
    total = sum(numbers) 
    return total
#3
def count_letters(name):
    letter_count = len(name) 
    return letter_count

#4
def sum_two_numbers():
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))  
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))   
    
    total = num1 + num2  
    return total

#5
def check_number():
    number = float(input("შეიყვანეთ რიცხვი: "))  

    if number > 0:
        return "true"
    elif number < 0:
        return "falce"
    else:
        return "zero"  

