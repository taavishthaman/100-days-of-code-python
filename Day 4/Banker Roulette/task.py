import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_index = random.randint(0, len(friends)-1)
print(friends[rand_index])

#Another way
print(random.choice(friends))