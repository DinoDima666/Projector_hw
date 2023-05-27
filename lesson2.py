# Make all these expressions true.

# a =  3 < 4

# b = 10 > 5

# c = 42 != "42"

# print(a,b,c)


# # Print the text in which there will be a quote with double quotes.

# print('As my grandfather said: "Im your grandfather"')

# # 2. Get a string from user input. Check if the string is a palindrome.

# palindrome = input("check if the word is a palindrome\n")

# print(palindrome[::] == palindrome[::-1])

# # 3. The program receive user's name and age from input. Then you need to display the name and age in one line in several ways:

# user_name = input("Enter user's name:\n")
# user_age = input("Enter user's age:\n")

# #    - by listing all the parameters in the print function
# print("1. Your name is : " + user_name +  "\n" + "2. Your age is: " + user_age)

# #    - by formatting a string using the format function

# birthday_string = "Your name is {name} and your age is {age} years old"

# print(birthday_string.format(name = user_name, age = user_age))

# #    - by formatting a string with f-string

# birthday_string = f"Your name is {user_name} and your age is {user_age} years old"

# print(birthday_string)

# #    String should looks like this: `"Your name is {name} and your {age} years old"`

# # 4. Find proper function in the documentation and format following strings

# #    1. All letters must be written in lowercase.

# string_1 = "Animals  "
# print(string_1.lower())


#    2. All letters must be capitalized.

# string_2 = "  Badger"

# print(string_2.upper())


#    3. Remove all spaces in this string:
#       - from the beginning of the line
#       - from the end of the line
#       - on both sides of the line


# string_3 = "   HoneyPot   "

# print(string_3.lstrip())
# print(string_3.rstrip())
# print(string_3.strip())


#    4. Check the value of the startwith ('Be') function for each line.:

# string_1 = "Bear"
# string_2 = "bear"
# string_3 = "BEAR"
# string_4 = "bEar"



# print(string_1.startswith("Be"))
# print(string_2.startswith("Be"))
# print(string_3.startswith("Be"))
# print(string_4.startswith("Be"))

#       Convert rows with methods from prev exercise to have positive result for each row.

#       ```
# formatted_string = string_2.capitalize()
# formatted_string = string_3.capitalize()
# formatted_string = string_4.capitalize()

# print(formatted_string.startswith('Be'))


#       > True
#       ```

# 5. Find and replace all letters (both cases) 's' with the letter 'x' in the following line: 
  
# string =   "Somebody said something to Samantha."

# string = string.replace("s","x").replace("S","X")


# print(string)

   

# 6. (Optional) Find a secret message in the following text: `'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'` 

# secret = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'

# secret = secret[-2::-2]

# print(secret)

