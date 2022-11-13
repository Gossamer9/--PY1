import random
def get_unique_list_numbers() -> list[int]:
    nums = []
    for i in range(15):
        num = random.randint(-10,10)
        while num in nums:
            num = random.randint(-10,10)
        nums.append(num)
    return nums



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
