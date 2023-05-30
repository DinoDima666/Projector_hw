# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. 
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).


# Write a program that simply outputs which cats have hats at the end.

# Optional: Make a function that can calculate hats with any amount of rounds and cats.

# Here you should write an algorithm, and after that, try to make pseudo code. Only after that start to work. 
#The code is simple here, but you might struggle with the algorithm. Therefore don`t try to write a code from the first attempt. 
#Don't forget to calculate the complexity of your algorithm.

# Homework should be uploaded at GitHub.comThe result of this HW should be a link to your GitHub code
#To learn how to work in Git, read the first three chapters of this book


# I'll go with three loops inside a function. First one will create a tuple with all cats I have as elements. 
#Second one will simulate rounds where I'll put hats on cats without one(0) and will take of from cats with hats(1) 
# Third will loop through the tuple with cats and will return the indices of cats with hats.

# O(n^2) is a difficulty

cats_amount = int(input("Please enter the number of cats you have:\n"))
number_of_rounds = int(input("Please enter the number of rounds:\n"))

def cats_with_hats(cats_amount: int, number_of_rounds: int) -> tuple:
    cats_tupl = []
    for _ in range(cats_amount):
        cats_tupl += [0,]
    step = 0    
    for _ in range(number_of_rounds):
        step += 1
        for i in range(0, len(cats_tupl), step):
            if cats_tupl[i] == 0:
                cats_tupl[i] += 1
            else:
                cats_tupl[i] -= 1
    cats_tuple_indicies = []        
    for i in range(len(cats_tupl)):
        if cats_tupl[i] == 1:
            cats_tuple_indicies += [i,]

    return cats_tuple_indicies

print(cats_with_hats(cats_amount, number_of_rounds))    


