foods = [
    "ფასანარული ხინკალი",
    "მწვადი",
    "კახური ღვინო",
    "ლობიო",
    "შოთის პური",
    "ღიპი",
    "ქართული მუსკები",
    "ბიგეტნიას ქაბაბი",
    "კომპოტი"
]


middle_index = len(foods) // 2
if len(foods) % 2 == 0:
 
    middle_elements = foods[middle_index - 1:middle_index + 2]
else:
   
    middle_elements = foods[middle_index - 1:middle_index + 2]

print("შუაში მყოფი 3 ელემენტი:")
print(middle_elements)


print("ყველა ელემენტი:")
for food in foods:
    print(food)


print("პირველი 4 ელემენტი:")
print(foods[:4])


print("ბოლო 4 ელემენტი:")
print(foods[-4:])