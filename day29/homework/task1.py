name= input("გთხოვთ შეიყვანოთ თქვენი სახელი")
surname= input("გთხოვთ შეიყვანოთ თქვენი გვარი")
age = int(input("გთხოვთ შეიყვანოთ თქვენი ასაკი: "))
phone_number = input("გთხოვთ შეიყვანოთ თქვენი ტელეფონის ნომერი: ")
email= input("გთხოვთ შეიყვანოთ თქვენი ტელეფონის ნომერი ან იმეილი")
password= input("გთხოვთ შეიყვანოთ თქვენი პაროლი:")
address= input("გთხოვთ შეიყვანოთ თქვენი საცხოვრებელი ადგილი")
if age < 0:
    print("არასწორი ასაკი! ასაკი არ შეიძლება იყოს უარყოფითი.")
else:

    print("\nმომხმარებლის ინფორმაცია:")
    print(f"სახელი: {name}")
    print(f"გვარი: {surname}")
    print(f"ასაკი: {age}")
    print(f"ტელეფონის ნომერი: {phone_number}")
    print(f"ემაილი: {email}")
    print(f"პაროლი: {password}")
    print(f"საცხოვრებელი ადგილი: {address}")