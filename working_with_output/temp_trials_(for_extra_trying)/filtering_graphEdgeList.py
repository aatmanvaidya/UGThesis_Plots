import pandas as pd
import networkx as nx

# load the tweets.csv file into a dataframe
tweets = pd.read_csv("tweets.csv")

# extract the user_id column from the tweets dataframe
tweet_users = set(tweets["user_id"].unique())

# open the users.edges file and create a new file with only the users present in the tweets dataframe
with open("users.edges") as f, open("filtered_users.edges", "w") as filtered_f:
    for line in f:
        user1, user2 = map(int, line.strip().split(" "))
        if user1 in tweet_users and user2 in tweet_users:
            filtered_f.write(line)

