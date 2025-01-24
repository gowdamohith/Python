a = lambda x, y: x * y

b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

d = a(b , c)

print(f"Multiplication of {b} * {c} = {d}")


numbers = [1,2,3,4,5]

result = list(map(lambda x: x + 2, numbers))

print(result)




n=int(input("Enter a number:"))

check_number=lambda n:"Yes" if(n > 10) else "No"


print(check_number(n))

####

def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)

nums = [1,2,3,4,5]
cubed = my_map(lambda x: x**3, nums)

print(cubed)
