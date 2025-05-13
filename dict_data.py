import pandas as pd

df = pd.read_csv('dictionary.csv')

def get_definition(word):
    return df.loc[df['word'] == word.lower()]['definition'].squeeze()