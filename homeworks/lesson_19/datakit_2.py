#   - Import the dataset from this address and assign it to df variable.

import pandas as pd

scores_url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"

df = pd.read_csv(scores_url)

print(df.columns. values. tolist())

# - Select only the Team, Yellow Cards and Red Cards columns.

teams_and_cards = df[['Team', 'Yellow Cards', 'Red Cards']]

print(teams_and_cards)

# - How many teams participated in the Euro2012?

number_of_teams = df.count().Team

print(number_of_teams)

# - Filter teams that scored more than 6 goals

goals = df[df.Goals > 6]

print(goals)



