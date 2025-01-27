def greet():
    print("Hello")

import math
import math as m
from math import pi

def square(x):
    return x**2
    def cube(x):
        return x**3

def circumference(r):
    return 2*pi*r

def area(r):
    return pi*r**2

#Use pandas to read a CSV file and display the first few rows.
#import pandas as p 
#df = p.read_csv(r"D:\csvdetails.csv")
#print(df.to_string())

my_data = {
    "Name": ["a","b","c"],
    "Age": [28,20,30]

}

data = p.DataFrame(my_data)
print(data)

#Import a module with a different name using as
#import math as m
#print(m.e)
#output

#Import the datetime module as dt and get the current date.
#import datetime as dt
#print(dt.date.today())
#print(dt.datetime.now())