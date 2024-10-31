def calculator():
    """
    ეკითხება მომხმარებელს ორ რიცხვს და მათემატიკურ მოქმედებას, და ასრულებს მოთხოვნილ მოქმედებას.
    """
    try:
        num1 = float(input("გთხოვთ, ჩაწერეთ პირველი რიცხვი: "))
        num2 = float(input("გთხოვთ, ჩაწერეთ მეორე რიცხვი: "))

        print("რამდენიმე მათემატიკური მოქმედება:")
        print("1. დამატება (+)")
        print("2. გამოკლება (-)")
        print("3. გამრავლება (*)")
        print("4. გაყოფა (/)")

        operation = input("გთხოვთ, აირჩიოთ მოქმედება (შეიყვანეთ სიმბოლო): ").strip()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("ციფრის გაყოფა 0-ით არ შეიძლება.")
                return
            result = num1 / num2
        else:
            print("არასწორი მოქმედების სიმბოლო.")
            return

        print("შედეგი: {}".format(result))

    except ValueError:
        print("გთხოვთ, ჩაწეროთ მხოლოდ რიცხვები.")


calculator()