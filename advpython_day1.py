try:
    number = int(input("Enter a number"))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero ")
except ValueError:
    print("Enter only integers")
finally:
    print("Complete")


try:
    a = ["abcd"]
    print(a[5])
except IndexError:
    print("Index out of range")


try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")

    

try:
   file = open("example.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("Error: The file was not found.")
else:
   print("File read operation successful.")
finally:
   if 'file' in locals():
      file.close()
   print("File operation is complete.")