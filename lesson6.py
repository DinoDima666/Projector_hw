# Assertive Lists: The Art of Coding Confidence
# 1. Write a Python program to compute the difference between two lists. Don`t use sets here
#     Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']
#     Expected Output:
#     first-second: ['a', 'b']
#     second-first: ['e']
#     ```python
# def compute_difference(first: list, second: list) -> tuple:
#     temp_first_1 = []
#     temp_second_1 = [] + second
#     temp_first_2 = [] + first
#     temp_second_2 = []
#     for i in first:
#         if i in temp_second_1:
#             temp_second_1.remove(i)
#         else:
#             temp_first_1.append(i)
#     for i in second:
#         if i in temp_first_2:
#             temp_first_2.remove(i)
#         else:
#             temp_second_2.append(i)        
#     result = (temp_first_1, temp_second_2)        

#     return result



# def test_compute_difference():
#     result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
#     assert result1 == (['a', 'b', 'c'], ['e'])
#     result2 = compute_difference([], ['c', 'd', 'e'])
#     assert result2 == ([], ['c', 'd', 'e'])
#     result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
#     assert result3 == ([1, 2, 3], [4, 4, 5, 6])
#     result3 = compute_difference([1, 2, 3], [2, 3, 4])
#     assert result3 == ([1], [4])

# print(test_compute_difference())    
#     ```
# 2. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
#     **Example 1:**
#     Input: nums = [2,7,11,15], target = 9
#     Output: [0,1]
#     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#     **Example 2:**
#     Input: nums = [3,2,4], target = 6
#     Output: [1,2]
#     **Example 3:**
#     Input: nums = [3,3], target = 6
#     Output: [0,1]
#     ```python
# def sum_of_two(nums: list, target: int) -> list:
    
#     for i in range(len(nums)):
#         indices = []    
#         if i+1 > len(nums):
#             break
#         elif nums[i] + nums[i+1] == target:
#             indices += [i, i+1]
#             break

#     return indices
            


# def test_sum_of_two():
#     result1 = sum_of_two([2,7,11,15], 9)
#     assert result1 == [0, 1]
#     result2 = sum_of_two([3,2,4], 6)
#     assert result2 == [1, 2]
#     result3 = sum_of_two([3,3], 6)
#     assert result3 == [0, 1]

# print(test_sum_of_two())


#     ```
# 3. Write a program that takes a list of integers as input and returns a new list that contains only the elements that are unique (i.e., that appear only once in the list). For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output list should be [1, 3, 4]. 
#     ```python
# def unique_elements(arr: list) -> list:
#     result = [i for i in arr if arr.count(i) < 2]
#     return result



# def test_unique_elements():
#     result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
#     assert result1 == [1, 3, 4]
#     result2 = unique_elements([1, 2, 3, 4, 5])
#     assert result2 == [1, 2, 3, 4, 5]
#     result3 = unique_elements([1, 1, 1, 1, 1])
#     assert result3 == []

# print(test_unique_elements())
#     ```




# 4. Write a program that takes a list of integers as input and returns a new list that contains only the elements that appear an odd number of times in the list. 
# For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output list should be [1, 3, 4].
#     ```python
# def odd_elements(arr: list) -> list:
#    result = [i for i in arr if arr.count(i) % 2 != 0] 
#    for i in result:
#       if arr.count(i) > 1:
#          result.remove(i) 

#    return result



# def test_odd_elements():
#     result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
#     assert result1 == [1, 3, 4]
#     result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
#     assert result1 == [1, 3, 4, 6]

# print(test_odd_elements())    

#     ```
# 5. Write a program that takes a list of integers as input and returns the second-largest element in the list. 
# If the list has fewer than two elements, the program should return None. 
# For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the program should return 5. Don`t use the sort method.
#     ```python
# def second_largest_element(arr: list) -> int:
        # for i in range(len(arr)):
        #      if arr[i] == arr[i-1]:
        #           return None
        #      else:
        #           break
        # if len(arr) < 2:
        #     return None
        # else:
        #     arr.remove(max(arr))
        #     result = max(arr)
        #     return result
        # _1_max = None
        # _2_max = None
        # for i in arr:
        #         if i > _1_max:
        #             _2_max
                        

    

# def test_second_largest_element():
#     result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
#     assert result1 == 5
#     result2 = second_largest_element([1, 2, 3, 4, 5])
#     assert result2 == 4
#     result3 = second_largest_element([1, 1, 1, 1, 1])
#     assert result3 == None
#     return result1, result2, result3


# #     ```
# # 6. Sort the following list by population. Calculate average and total population for cities from this list:
# # ```


# arr = [
# ('New York City', 8550405),
# ('Los Angeles', 3792621),
# ('Chicago', 2695598),
# ('Houston', 2100263),
# ('Philadelphia', 1526006),
# ('Phoenix', 1445632),
# ('San Antonio', 1327407),
# ('San Diego', 1307402),
# ('Dallas', 1197816),
# ('San Jose', 945942),
# ]

# arr.sort(key = lambda a: a[1])


# total_pop = 0


# for i in range(len(arr)):
#     total_pop += arr[i][1]

# average_pop = total_pop // len(arr)

# print( total_pop, average_pop)     

# ```