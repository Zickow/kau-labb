import random

counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    counts[total] = counts[total] + 1

for sum_number in range(2,13):
    print(str(counts[sum_number]) + " times the sum was " + str(sum_number))
