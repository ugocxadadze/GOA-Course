#1
def greet_user(name):
    print("გამარჯობა, {}! კეთილი იყოს შენი მობრძანება!".format(name))
    
greet_user("ნინო")


#2
def sum_of_numbers(numbers):
    total = sum(numbers)
    return total

result = sum_of_numbers([1, 2, 3, 4, 5])
print( {}.format(result))

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
        return "დადებითი"
    elif number < 0:
        return "უარყოფითი"
    else:
        return "ნულოვანი"

