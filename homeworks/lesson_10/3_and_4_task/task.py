# Write a program that will simulate user scores in a game. 
# Create a list with 5 players’ names after that simulate 100 rounds for each player. 
# As a result of the game create a list with the player's name and score (0-1000 range). And save it to a CSV file. 
# The file should look like this:

# Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345
# ...
# Write a script that reads the data 
# from the previous CSV file and creates a new file called high_scores.csv 
# where each row contains the player name and their highest score. 
# The final score should be sorted by descending to the highest score. 
# The output CSV file should look like this:

# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

import csv
import random

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
scores = []

def rounds():
    with open("scores.csv", "w") as scores:
        writer = csv.writer(scores)
        writer.writerow(["Player Name", "Score"])

        for player in players:
            for _ in range(100):
                score = random.randint(0, 1000)
                writer.writerow([player, score])

rounds()

best_scores = {}

def read_scores():
    with open("scores.csv", "r") as scores:   
        reader = csv.reader(scores)  
        next(reader)
        for row in reader:
            name = row[0]
            score = int(row[1])
            if name in best_scores:
                best_scores[name] = max(best_scores[name], score)
            else:
                best_scores[name] = score

read_scores()

rating = sorted(best_scores.items(), key=lambda x:x[1], reverse= True)






print(rating)

def rating_csv():
    with open("Highest_scores_rating.csv", mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(["Player Name", "Score"])
        for player, score in rating:
            writer.writerow([player,score])

rating_csv()

     




