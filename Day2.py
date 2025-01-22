x = int(input("What is your exam score?"))
if x >= 85:
    print('You got an A! Congrats!')
elif x >= 75:
    print('You got a B! Well done!')
elif x > 50:
    print('You got a C. Not great, not terrible.')
elif x == 50:
    print('You got a D. But you can do better!')
else:
    print("You did not pass the exam. See the teacher for more information.")


def sum_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Example use:
n = 10
print(f"The sum from 1 to {n} is: {sum_to_n(n)}")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example use:
n = 5
print(f"The factorial of {n} is: {factorial(n)}")

def pyramid_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Example use:
rows = 5
print("Pyramid Pattern:")
pyramid_pattern(rows)

# Example dictionary
my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# Using a for loop with the .values() method to iterate through values
for value in my_dict.values():
    print(value)

# Using a for loop with .items() if you also need keys (though only printing values here)
for key, value in my_dict.items():
    print(value)  # Only prints the value




