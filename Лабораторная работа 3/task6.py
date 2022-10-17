list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_element = max(list_numbers)
for i, element in enumerate (list_numbers):
    if list_numbers[i]==max_element:
        list_numbers[-1],list_numbers[i]=list_numbers[i],list_numbers[-1]
        break

print(list_numbers)
