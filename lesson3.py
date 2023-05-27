# Loop de Loop: The Endless Homework Chronicles


# 1. Make all these expressions True by adding parentheses:    

# a) 

# print( False == (not True))     

# b) 

# print((True and False) == (True and False)) 

# c)

# print(not (True and "A" == "B"))


# 2. Make a solution for Wheat and chessboard problem. Represent a solution in tons. 
# Assume that one grain of wheat weights 0.065 gram

# chessboard_squares = 1
# grains_number = 1

# while chessboard_squares <= 64:
#     grains_number *= 2
#     chessboard_squares += 1
 
# print(grains_number * 0.065 * (10 ** -6))    



# 3. Get a positive number from user input. Find all factors of this number.
# Example:
# - If the number is 6, the factors are: 1, 2, 3, 6
# - If the number is 10, the factors are: 1, 2, 5, 10

# input_number = input("Please input a number:\n")

# if input_number.isdigit() == True:
#     input_number = int(input_number)
# else:
#     print("please enter a valid number")    
# input_number = int(input_number)

# factor = input_number

# while factor != 0:    
#     if input_number % factor == 0:
#         print(factor)    
#     factor -= 1
# print("finish")


# 4. Write a Python program to check whether a triangle is equilateral, isosceles or scalene. Get all three sides from user input.
# Note :
# 1. An equilateral triangle is a triangle in which all three sides are equal.
# 2. A scalene triangle is a triangle that has three unequal sides.
# 3. An isosceles triangle is a triangle with (at least) two equal sides.

# first_side = int(input("Input a first side's length:\n"))
# second_side = int(input("Input a second side's length:\n"))
# third_side = int(input("Input a third side's length:\n"))

# if first_side == (second_side + third_side) // 2:
#     print("The triangle is equilateral")
# elif first_side == second_side or first_side == third_side or second_side == third_side:
#     print("The triangle is isosceles") 
# else:
#     print("The triangle is scalene")     


# 5. (Optional): Write a Python program to get the next day of a given date. Get the day, month and year from the user input. Don`t use datetime module for that
# Expected Output:
# **Input a year:** 2022
# **Input a month [1-12]:** 8
# **Input a day [1-31]:** 23
# The next date is [yyyy-mm-dd] 2022-8-24

# year = int(input("Please, enter a year:\n"))
# month = int(input("Please, enter a month:\n"))
# day = int(input("Please, enter a day:\n"))


# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 and day == 31:
#     print(f"The next date is {year}-{month + 1}-1")
# elif year % 4 == 0 and month == 2 and day == 29 :
#     print(f"The next date is {year}-{month + 1}-1")
# elif month == 2 and day == 28:
#     print(f"The next date is {year}-{month + 1}-1")
# elif month == 12 and day == 31:
#     print(f"The next date is {year + 1}-1-1")    
# elif day == 30:
#     print(f"The next date is {year}-{month + 1}-1")
# else:
#     print(f"The next date is {year}-{month}-{day + 1}")  
  