import pandas as pd

def flatten(dataframe, col):
    df = dataframe.copy()
    return df.explode(col).reset_index(drop=True)

df = pd.DataFrame(data=[[[1, 2],5], [['a', 'b', 'c'], 6], [77, 3]], columns=list('AB'))
flatten(df, 'A')