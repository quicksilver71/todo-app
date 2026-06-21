from parser import parse
import random

user_input = input("Enter a lower bound and a upper bound divided by comma (e.g.:2,10): ")
parsed = parse(user_input)
rand = random.randint(parsed["lower_bound"],parsed["upper_bound"])
print(rand)