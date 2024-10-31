foods = [
    "პიცა",
    "ჰამბურგერი",
    "პასტა",
    "სალათი",
    "ფრანჩიზი",
    "ბურგერი",
    "შაურმა",
    "საშუალო",
    "ბურგერი",
    "დონატი"
]

middle_index = len(foods) // 2

if len(foods) % 2 == 0:
    middle_elements = foods[middle_index - 1:middle_index + 1]  
else:
    middle_elements = foods[middle_index - 1:middle_index + 2]  

print("შუაში მყოფი ელემენტები:")
print(middle_elements)

print("ყველა ელემენტი:")
for food in foods:
    print(food)

print("პირველი 4 ელემენტი:")
print(foods[:4])

print("ბოლო 4 ელემენტი:")
print(foods[-4:])