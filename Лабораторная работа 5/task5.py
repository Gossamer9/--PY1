import random

def get_random_password(n: int = 8) -> str:
    lst = [i for i in range(10)] + \
          [chr(i) for i in range(ord('A'),ord('Z') + 1)] + \
          [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return random.sample(lst, n)

print(get_random_password())
