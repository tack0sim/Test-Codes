import random
print(random.randint(0,9))


# for
for i in range(0,5):
    print(i, end="")
print()

# while
i = 0
while i < 5:
    print(i, end="")
    i += 1
print()

# for...in and range with 2-value increments
for i in range(0, 10, 2):
    print(i, end="")
print()