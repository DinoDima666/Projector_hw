import random
# 1. Write a program that asks the user to enter an integer and convert it to an int. 
# The program should have 2 functions. The first function should ask the user to input information and return inputted value. 
# The second function receives the inputted value and converts it to int. 
# If the user enters something that is not an integer, this function should catch an error and ask the user to enter an integer again. 
# if the user inputs an integer, the program should print this number and quit w/o any error.

# def user_input():
#     int_value = input("Please input a number:\n")
#     def convert():
#         try:
#             converted = int(int_value)
#             return converted 
#         except ValueError:
#             print("Not a number, please try again")
#             return user_input()   
            
#     return convert()       

# result = user_input()
# print(result)


# 2. Write a program that asks the user to input a string and an integer n. 
# The Program should have 2 functions. The first function should ask the user to enter a string and an integer. 
# The second function should receive the inputted value and print the character at the index n. 
# If the user enters the wrong value, this function should catch an error and provide a proper error message with an explanation. 
# After the error is handled, the program should ask the user to enter a string and an integer again. 
# If the user inputs a string and an integer, the program should print the character at the index n and quit w/o any error.

# def user_input():
#     i = int(input("Please input a number:\n"))
#     string = input("Please input a string:\n")
#     def result():
#         try:
#             el = string[i]
#             return el
#         except IndexError:
#             print("Index is out of range, please try again")
#             return user_input()
#     return result()       

# result = user_input()
# print(result)





# 3. Transaction
#  a) Define a global variable called balance and set it to 1000. 
# Write a function called transaction that takes an argument amount and argument _type that can be either deposit or withdrawal.              
# b) Inside the function create two inner functions called deposit and withdrawal that take an argument amount.              
# c) Inside the deposit function, add the amount to the balance variable and print the new balance.              
# d) Inside the withdrawal function, subtract the amount from the balance variable and print the new balance.              
# e) Inside the transaction function, check if the _type argument is deposit or withdrawal and call the appropriate function.

# balance = 1000


# def transaction(amount: int, _type: str):
#     dep = "deposit"    

#     def deposit(amount):
#             return balance + amount

#     def withdrawal(amount):
#             return balance - amount

#     if _type == dep:
#         return deposit(amount)       
#     else:
#         return withdrawal(amount)    

# result = transaction(100, "withdrawal")
# print(result)



# 4/5
# Write a function that simulates a dice roll and returns the result from 1 to 6. Use random module
# Use the function from the previous task to simulate 1000 dice rolls and print the result. 
# Calculate the number of times each number was rolled.



# def dice_roll():
#     return random.randint(1,6)

# roll = dice_roll()


# def thousand() -> str:
#     roll_string = ""
#     for i in range(1001):
#         roll_string += str(random.randint(1,6))
#     return roll_string


# roll_array = tuple(thousand())

# def amount(x: str) -> int:
#     count_number = roll_array.count(x)
#     return f"Number {x} was rolled {count_number} times"

# number_amount = amount("5")

# print(number_amount)




# 6. Simulate an election for two candidates. 
# The program should take the number of regions and the rating for 1st candidate in each region (in percentage). 
# The program should run elections in every region. In every region, the program should ask 10 000 voters. 
# Use the random module to simulate a voice from a person. The candidate counts as a winner if he gains more than 50% of all votes. 
# The program should print the result of the election for each region and the winner


# def receive_input():
#     regions_n = int(input("Please enter a number of regions:\n"))
#     rating = ()
#     for i in range(1,regions_n + 1):
#          rating += (int(input(f"Please input a rating for the candidate in the region {i}:\n")),)
#     return rating
              


# def simulate_region_election(regions):
#     first_cand_reg_tuple = ()
#     second_cand_reg_tuple = ()
#     for i in range(len(regions)):
#         first_candidate_reg = 0
#         second_candidate_reg = 0
#         for _ in range(10000):
#             probability = random.randint(0, 100)
#             if probability <= regions[i]:
#                 first_candidate_reg += 1
#             else:
#                 second_candidate_reg += 1
#         print(f"First candidate got {first_candidate_reg} votes in region {i+1}")
#         print(f"Second candidate got {second_candidate_reg} votes in region {i+1}")           
#         first_cand_reg_tuple += (first_candidate_reg,)
#         second_cand_reg_tuple += (second_candidate_reg,)                
#     return first_cand_reg_tuple, second_cand_reg_tuple

     
     
    


# def simulate_election(cand_1,cand_2):
#     cand_1_result = sum(cand_1)
#     cand_2_result = sum(cand_2)
#     if cand_1_result > cand_2_result:
#         return f"Candidate 1 wins with {cand_1_result} votes over candindate's 2 {cand_2_result} votes"
#     else:
#         return f"Candidate 2 wins with {cand_2_result} votes over candindate's 1 {cand_1_result} votes"



# input_data = receive_input()

# region_elections = simulate_region_election(input_data)

# print(simulate_election(region_elections[0], region_elections[1]))

