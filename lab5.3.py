import random

random_numbers = [random.randint(1, 30) for i in range(50)]

unique_numbers = list(set(random_numbers))
                    #set removes a duplicate values

print(unique_numbers)