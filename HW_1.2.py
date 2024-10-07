import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return "" 
    random_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(random_numbers)

print(get_numbers_ticket(1, 49, 5))