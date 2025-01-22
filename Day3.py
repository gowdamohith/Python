def factorial(n):
    if n < 0:
        
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


transformed_evens = [num * 2 for num in numbers if num % 2 == 0]

print(transformed_evens)
# Output: [4, 8, 12, 16, 20]

# Example list of dictionaries
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]


names = [d['name'] for d in data]
print(names)  # Output: ['Alice', 'Bob', 'Charlie']


ages = [d['age'] for d in data]
print(ages)  # Output: [30, 25, 35]