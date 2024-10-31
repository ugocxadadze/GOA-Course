def multiply_with_user_input(num1):
    num2 = float(input("შეიყვანეთ მეორე ციფრი: "))

    result = num1 * num2
    print( + str(num1) + + str(num2) + + str(result))

#2
def find_xth_element(x, my_list):
    if x < 0 or x >= len(my_list):
        return "შეცდომა: x უნდა იყოს სიაში არსებული ინდექსის დიაპაზონში."
    return my_list[x]
#3
def multiply_max_of_lists(list1, list2):
    max1 = max(list1)
    max2 = max(list2)
    result = max1 * max2
    print("მაქსიმალური რიცხვების ნამრავლი " + str(max1) + + str(max2) + + str(result))
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]