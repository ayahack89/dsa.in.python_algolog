# Dependencies
import array as myarray
import numpy as np 

# Array 
# What is an Array?
# > An array is a data structure that stores multiple values sequentially in memory. 
# But Python is a bit different from other languages. 
# In Python there are two ways to define an Array: One using the "array" module and another using "NumPy". 
# in Python, defining using "[]" is by default a "list", not an "array". 

l = [8, 9, 2, 4, 5, 6]
print(f"List: {l} & Its a list: {type(l)}")

nums = [1, 21, 4, 5]
for n in nums:
    print(f"INDX: {nums.index(n)} DATA: {n} TYPE: {type(nums)}")

# Using Array module (Typecode)
arr = myarray.array("i", [26, 44, 66, 78])
print(f"Array: {arr} & Its an integer array: {arr.typecode}")


# Different typecodes (i = integer, f = float, d = double float, u = unicode char)
a = myarray.array("i", [1, 2, 3, 4, 5])
b = myarray.array("u", ["a", "b", "c"])
c = myarray.array("d", [1.2, 2.5, 3.6])
d = myarray.array("f", [10.5, 20.5])

print("Array Example:")
print(a)
print(b)
print(c)
print(d) 

print("Typecode:- ")
print(f"Integer: {a.typecode}")
print(f"Unicode Char: {b.typecode}")
print(f"Double: {c.typecode}")
print(f"Float: {d.typecode}")


# Iteration using while loop
values = myarray.array("i", [10, 20, 30, 40, 50])
i = 0
while i < len(values):
    print(f"Index: {i}, Data: {values[i]}")
    i += 1

# Using NumPy > NumPy is the best way to define an "Array" in Python
ar = np.array([2881, 2097, 3678, 4009, 5876, 7777])
for o in ar:
    print(f"Elemet {o}")

for indx in range(len(ar)):
    print(f"Index: {indx}, Element: {ar[indx]}")


# 2-D (Dimensional) Array 
twoD = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print("2D Array: \n", twoD)

print("First Row Values: ")
print(twoD[0][0], twoD[0][1], twoD[0][2], twoD[0][3])

print("Second Row Values:")
print(twoD[1][0], twoD[1][1], twoD[1][2], twoD[1][3])


# Search elemt in an Array
x = np.array([4, -2, 8, 9, -12, 14, 11, 16])
search = int(input("Enter a number: "))

found = 0
pos = 0

for p in x:
    pos += 1
    if search == p:
        found = 1
        print(search, "Exists at position", pos)

if found == 0:
    print("ERROR the number does not exist in the list")


# Array operations
numbers = [] #list
length_count = int(input("How many numbers do you want in the array?"))   

for count in range(length_count):
    array_values = int(input("Enter array values: ")) 
    numbers.append(array_values) # add each input in list (default)

# Convert list to array
converted_arr = np.array(numbers)
print(f"Array: {converted_arr} & Type: {type(converted_arr)}") # Array converted

# NumPy Operations 
""" NumPY Operations "Max value" & "Element Position" """
print("Maximum value: ", np.max(converted_arr))
print("Position of maximum value:", np.argmax(converted_arr)) # Index 

# Find the max value (logic) 
current_biggest = converted_arr[0]
for main_iteration in range(len(converted_arr)):
    for sub_iteration in range(main_iteration + 1, len(converted_arr)):
        if converted_arr[sub_iteration] > current_biggest:
            current_biggest = converted_arr[sub_iteration]

print("Biggest Element:", current_biggest) 

# NumPy "Zeros" array
arr1 = np.zeros(5)
print(arr1) # 1D

arr2 = np.zeros((3, 4))
print(arr2) # 2D

# By default, xeros are floats. 
# To force integers: 
arr = np.zeros(5, dtype=int)
print(arr) 




# All array concepts done....  



