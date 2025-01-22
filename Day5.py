# Import Pandas library
import pandas as pd

url = 'https://student_data2.csv'
# Read the CSV file
df=pd.read_csv(url)

# Print the data frame
print(df)


# Calculate and print mean value
mean_value=df['fees'].mean()
print('Mean Value: '+str(mean_value))

# Calculate and print median value
median_value=df['fees'].median()
print('Median Value: '+str(median_value))

# Calculate and print sum value
sum_value = df['fees'].sum()
print('Sum Value: '+str(sum_value))


import numpy as np

# create two matrices
matrix1 = np.array([[1, 3], 
             		[5, 7]])
             
matrix2 = np.array([[2, 6], 
                    [4, 8]])

# calculate the dot product of the two matrices
result = np.dot(matrix1, matrix2)

print("matrix1 x matrix2: \n",result)

import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing addition using arithmetic operator
add_ans = a+b
print(add_ans)

# Performing addition using numpy function
add_ans = np.add(a, b)
print(add_ans)

# this would work
c = np.array([1, 2, 3, 4])
add_ans = a+b+c
print(add_ans)

# but here NumPy only considers the first two arrays (a and b) and ignores the third one (c).
add_ans = np.add(a, b, c)
print(add_ans)


import pandas as pd
df = pd.read_csv("https://nba.csv")

team = df.groupby('Team')
print(team.first()) # Let's print the first entries in all the groups formed.

import pandas as pd
df = pd.read_csv("https://nba.csv")

# Filter groups where the average Salary is >= 5 million
filtered_df = df.groupby('Team').filter(lambda x: x['Salary'].mean() >= 1000000)
print(filtered_df)

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)

# Sorting by 'Age' in ascending order
sorted_df = df.sort_values(by='Age')
print(sorted_df)