def sum_of_numbers(numbers):
    """
    ითვლის რიცხვებით სავსე სიის ჯამს.

    :param numbers: სია რიცხვების
    :return: ჯამი
    """
  
    total = sum(numbers)
    
    return total


numbers_list = [10, 20, 30, 40, 50]
result = sum_of_numbers(numbers_list)
print("რიცხვების ჯამი: {}".format(result))