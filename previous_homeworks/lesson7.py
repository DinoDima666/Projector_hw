# Write a game where the user should guess the capital of the country that you have in your dictionary.

# capitals = {
#         'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
#         'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', '
#         'Switzerland': 'Bern', 'Austria': 'Vienna',
#         'Belgium': 'Brussels',  'Sweden': 'Stockholm',
#         'Norway': 'Oslo', 'Denmark': 'Copenhagen',
#         'Finland': 'Helsinki', 'Poland': 'Warsaw',
#         'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens', ...
# }

# You should show the user a random country from the list and ask him to guess the capital. 
# If the user inputs the right capital, print "You are right!", add a point and ask him to guess another country. 
# If not, you should ask again. The user should be able to quit the game by typing "exit".

# You should print the current score after each round. Also, you should print the final score before the user quit the game.

# Optional:

# 1. Give the user a hint if he guesses wrong. 
# The hint should look like the first letter of the capital. 
# If the user makes another mistake, you should print one more letter from the capital.

# 2. If a user makes a mistake you should decrement his life. 
# The initial amount of lives is 3. The game will end when the user has no lives left. 
# You should print the final score after the user has no lives left.

# ____________________________________________________________________

import random

# capitals = {
#         'Ukraine': 'Kyiv',
#         'France': 'Paris',
#         'Germany': 'Berlin',
#         'Italy': 'Rome',
#         'USA': 'Washington',
#         'Canada': 'Ottawa',
#         'Switzerland': 'Bern',
#         'Austria': 'Vienna',
#         'Belgium': 'Brussels',
#         'Sweden': 'Stockholm',
#         'Norway': 'Oslo',
#         'Denmark': 'Copenhagen',
#         'Finland': 'Helsinki',
#         'Poland': 'Warsaw',
#         'Romania': 'Bucharest',
#         'Bulgaria': 'Sofia',
#         'Greece': 'Athens',
#     }

# li_capitals = list(capitals)

# def guessing_game() -> int:
#     score = 0
#     while score >= 0:
#         random_country = li_capitals[random.randint(0, len(li_capitals) - 1)]
#         user_input = input(f"Please input the capital of {random_country}:\n")
#         if user_input == "exit":
#             return score
#         elif user_input == capitals[random_country]:
#             score += 1
#             print(f"You're right, your score is: {score}")
#         elif user_input != capitals[random_country]: 
#             print("Please try again")


              


# print(f"Your final score is: {guessing_game()}")


    
# 4. Given a list of integers of size n, return the majority element.
# The majority element is the element that appears more than any other element. 
# You may assume that the majority element always exists in the array.

# def majority_element(nums: list) -> int:
#     return max(set(nums), key= nums.count)

    

# def test_majority_element():
#     result1 = majority_element([3, 2, 3])
#     assert result1 == 3

#     result2 = majority_element([2, 2, 1, 1, 1, 2, 2])
#     assert result2 == 2


# print(test_majority_element())




# 5. Find missing subjects


# def get_subjects_not_passed_by_all_students(student_exams):
#     exams = set()
#     for i in student_exams:
#         if i[1] < 60:
#             exams.add(i[2])
#     print(exams)        
#     return exams        



# def test_get_subjects_not_passed_by_all_students():
#     exams = [
#         ("Alice", 85, "Math"),
#         ("Bob", 59, "Math"),
#         ("Charlie", 65, "Math"),
#         ("Alice", 90, "Science"),
#         ("Bob", 80, "Science"),
#         ("Charlie", 32, "Science"),
#         ("Alice", 95, "History"),
#         ("Bob", 85, "History"),
#         ("Charlie", 90, "History"),
#     ]

    
#     assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}


# print(test_get_subjects_not_passed_by_all_students())