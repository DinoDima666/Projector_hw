
# 1. Write a function called `find_primes` that takes in two integers a and b and returns 
# a list of all the prime numbers between a and b (inclusive).


def find_primes(a: int,b: int) -> str:
        list = ""
        for i in range(a, b + 1):
            list += str(i) + ", "
        return list

a = 30
b = 30  

if type(a)!= int or type(b) != int:
        print("Please input a whole number")   
elif a > b:
      a,b = b,a
      list_primes = find_primes(a,b)
      list_primes = list_primes.rstrip(", ")
      print(list_primes)      
else:        
    list_primes = find_primes(a,b)
    list_primes = list_primes.rstrip(", ")
    print(list_primes)






# 2. Write a function called `unique_characters` that takes in a 
# string s and returns a Boolean value indicating whether or not all the characters in s are unique. 
# For example, the string "abcdefg" has unique characters, but the string "abcdeff" does not.

# def unique_characters(s: str) -> bool:
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if s[i] == s[j]:
#                 return False
#             print(s[i], s[j])           
#     return True   

# is_unique = unique_characters("abcde")

# print(is_unique)





# 3. Write a function that calculates [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_sequence). 
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. 
# A number of iterations should be taken from user input.
# ```python
# def fibonacci(n: int) -> int:
#     first = 1
#     second = 1
    
#     for i in range(n-2):
#         temp = second
#         second = first + second
#         first = temp
#     return second

# n = int(input("input the number of iterations:\n"))

# result = fibonacci(n)
# print(result)
# 55


# 4. Write a function that implements case swapping. 
# It should return the same result as swapcase() method. 
# Your function should accept one str argument and convert all lower case values to upper case and vice versa. 
# ```python

# def swapcase(input_string: str) -> str:
#     swapcase_string = ""
#     for i in range(len(input_string)):
#         print(input_string[i])
#         if input_string[i].isupper():
#             swapcase_string += input_string[i].lower()
#             print(swapcase_string)
#         elif input_string[i].islower():
#             swapcase_string += input_string[i].upper()
#         else:
#             continue    

#     return swapcase_string            




# print(swapcase('HelLo!')) 






# >>> 'hELlO!
# ```



# 5. Write a function that calculates the performance of a deposit in a bank account. 
# The function called simple_interest takes three arguments: the initial amount, the annual interest rate (as a float), and the time in years. 
# The function should return the final amount after the simple interest has been applied. Use a for loop to accomplish this. 
# Round the answer to the nearest hundredth.
# ```python
# def simple_interest(initial_amount, interest_rate, years):
#     current_amount = initial_amount
#     for n in range(years):
#         current_amount += current_amount*interest_rate
#     current_amount  = round(current_amount, 2)    
#     return current_amount    



# print(simple_interest(10000, 0.1, 10))
# >>> 25937.42
# ```

# 6. (Optional) Write a function called password_strength that takes a string password 
# as an argument and returns a password strength score based on the following criteria:
#     Length: +1 point for each character
#     Lowercase letters: +2 points for each unique lowercase letter
#     Uppercase letters: +3 points for each unique uppercase letter
#     Digits: +4 points for each unique digit
#     Special characters: +5 points for each unique special character
# Use for loops to accomplish this. The function should return the total score for the given password.
# ```python

# def password_strength(password: str) -> int:
#     score = len(password)
#     unique_total = "" 
#     for i in password:
#         if i not in unique_total:
#             unique_total += i
#     for i in unique_total:
#         if i.isupper():
#             score += 3
#         elif i.islower():   
#             score += 2
#         elif i.isdigit():   
#             score += 4
#         else:
#             score += 5                

#     return score           


# score = password_strength('aB1')

# print(score)


# >>> 24 # 6 for each symbol + 3 * 2 for each lowercase letter + 4 * 3 for each digit
# ```

# 7. (Optional) Write two functions, encrypt and decrypt, 
# that implement the [Caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher) technique for encrypting and decrypting messages. 
# The encrypt function should take a message and a shift value as arguments, 
# while the decrypt function should take an encrypted message and the same shift value as arguments. 
# Use for loops to accomplish this.
# ```python
# def encrypt(message, shift):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     encrypted = ""

#     for i in range(len(message)):
#         for j in range(len(alphabet)):
#             upper = message[i] == alphabet[j]
#             lower = message[i] == alphabet[j].lower()
#             if upper:
#                 encrypted += alphabet[j-shift]
#             elif lower:
#                  encrypted += alphabet[j-shift].lower()
#     return encrypted

# encrypted_message = encrypt("B!", 1)

# print(encrypted_message)
# #     # Your code here

# def decrypt(encrypted_message, shift):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     shift = 26 - shift
#     decrypted = ""

#     for i in range(len(encrypted_message)):
#         for j in range(len(alphabet)):
#             upper = encrypted_message[i] == alphabet[j]
#             lower = encrypted_message[i] == alphabet[j].lower()
#             if upper:
#                 decrypted += alphabet[j-shift]
#             elif lower:
#                  decrypted += alphabet[j-shift].lower()
#     return decrypted


# decrypted_message = decrypt(encrypted_message, 1)

# print(decrypted_message)



# Using "ord"


# def encrypt(message: str, shift: int) -> str:
#     encrypted = ""
#     decrypted = ""
#     for i in range(len(message)):
#         el = message[i]
#         if el.isupper():
#             encrypted += chr((ord(el) + shift - 65) % 26 + 65) 
            
#         else:
#             encrypted += chr((ord(el) + shift - 97) % 26 + 97)
#     for i in range(len(encrypted)):
#          el = encrypted[i]
#          if el.isupper():
#             decrypted += chr((ord(el) - shift - 65) % 26 + 65) 
            
#          else:
#             decrypted += chr((ord(el) - shift - 97) % 26 + 97)        

#     return encrypted, decrypted


# encrypted_message = encrypt("HEre Is ThE meSSaGe", -1)
# print(encrypted_message)






