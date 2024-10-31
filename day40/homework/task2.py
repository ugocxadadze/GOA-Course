even_numbers = []
odd_numbers = []


number = int(input("შეიყვანეთ რიცხვი: "))


if number % 2 == 0:
    even_numbers.append(number)
    print("{number} არის ლუწი რიცხვი და დაამატა ლუწი რიცხვების სიაში.")
else:
    odd_numbers.append(number)
    print("{number} არის კენტი რიცხვი და დაამატა კენტების სიაში.")


print("ლუწი რიცხვების სია:")
print(even_numbers)

print("კენტების სია:")
print(odd_numbers)