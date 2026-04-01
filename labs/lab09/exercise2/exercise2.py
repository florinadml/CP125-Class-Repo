import pandas as pd


def compare_averages(filename):
    data = pd.read_csv(filename)
    subjects = ["Math", "Science", "English"]
    math_mean =  round(data["Math"].mean(), 1)
    science_mean =  round(data["Science"].mean(), 1)
    english_mean =  round(data["English"].mean(), 1)

    