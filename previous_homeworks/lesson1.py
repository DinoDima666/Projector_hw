# Write a program that gets two int variables and swaps their values. Do it in 3 different ways.

# 1st way:

# x = 2
# y = 3

# x_temp = x
# x = y
# y = x_temp

# print(f" we've swapped the variables and now x = {x} and y = {y}")

# 2nd way:

# x = 2
# y = 3

# x, y = y, x 

# print(f" we've swapped the variables without creating a temporary variable and now x = {x} and y = {y}")

# 3rd way:

#x = 2
#y = 3

#x = x + y
#y = x - y
#x = x - y

# print(f" we've swapped the variables by using only arithmetics and now x = {x} and y = {y}")

#print("we've swapped the variables by using only arithmetics and now x = "+ str(x) +" and y = " + str(y))



# Write a program that gets 2 numbers from the user. Print to the console their difference. Use the built-in Input function for that

# x = input("Please enter the first digit:\n")
# y = input("Please enter the second digit:\n")

# print(f"The difference is: {int(x)-int(y)}")


# Write a program that gets 2 numbers from the user. Print to the console maximum of these two variables. 
# Use a built-in function for that.

# x = input("Please enter the first digit\n")
# y = input("Please enter the second digit\n")

# print(f"The maximum is: {max(x, y)}")

# Write a program that gets 3 digit number from the user and reverses it. You can use only numbers and their operators. Don`t use a string here!

#x = int(input("Please enter the 3-digit number\n"))

#y = 0

#while(x>0):
    #z = x%10
    #y = (y*10)+z
    #x //= 10
#print(f"The reversed 3-digit number is: {y}")

# Optional without using a while loop

x = int(input("Please enter the 3-digit number\n"))

y = 0

z = x % 10
y = (y * 10) + z
x //= 10

z = x % 10
y = (y * 10) + z
x //= 10

z = x % 10
y = (y * 10) + z
x //= 10    

print(f"The reversed 3-digit number is: {y}")



