def check_odd_even():
    """
    ამ ფუნქციას ეკითხება მომხმარებელს რიცხვის შეყვანა
    და განსაზღვრავს, არის თუ არა ის ლუწი თუ კენტი.
    """
    try:
       
        number = int(input("გთხოვთ, ჩაწერეთ რიცხვი: "))
        
       
        if number % 2 == 0:
            print("რიცხვი {} არის ლუწი.".format(number))
        else:
            print("რიცხვი {} არის კენტი.".format(number))
    
    except ValueError:
        print("გთხოვთ, ჩაწეროთ მხოლოდ რიცხვი.")


check_odd_even()