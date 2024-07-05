#import csv files
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

#read csv files
bat_main = pd.read_csv('batting_main.csv')
bat_avg = pd.read_csv('batting_avg.csv')
bat_sixes = pd.read_csv('batting_sixes.csv')
bat_sr = pd.read_csv('batting_sr.csv')
bowling_wickets = pd.read_csv('bowling_wickets.csv')
bowling_avg = pd.read_csv('bowling_avg.csv')
bowling_econ = pd.read_csv('bowling_econ.csv')

# Select the players only with more than 100 innings
bat_main_1 = bat_main[bat_main['Inns'] > 100]
bat_avg_1 = bat_avg[bat_avg['Inns'] > 100]
bat_sixes_1 = bat_sixes[bat_sixes['Inns'] > 100]
bat_sr_1 = bat_sr[bat_sr['Inns'] > 100]
bowling_wickets_1 = bowling_wickets[bowling_wickets['Mat'] > 100]
bowling_avg_1 = bowling_avg[bowling_avg['Mat'] > 100]
bowling_econ_1 = bowling_econ[bowling_econ['Mat'] > 100]

# There are two main dataframes, one for batting and one for bowling
# The main dataframe for batting is 'bat_main' and the main dataframe for bowling is 'bowling_wickets'
# Merge all the batting dataframes to form a new dataframe called bat_df
# Merge all the bowling dataframes to form a new dataframe called bowl_df

bat_df = bat_main_1.merge(bat_avg_1, on='Player').merge(bat_sixes_1, on='Player').merge(bat_sr_1, on='Player')
bowl_df = bowling_wickets_1.merge(bowling_avg_1, on='Player').merge(bowling_econ_1, on='Player')

# Define the features (X) and the target (y) for batting
