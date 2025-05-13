import pandas as pd


def get_definition(word):
    df = pd.read_csv('dictionary.csv')
    return df[df['word'] == word.lower()]['definition'].squeeze()
