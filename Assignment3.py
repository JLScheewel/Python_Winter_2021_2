import pandas as pd
df = pd.read_csv('data/GOOG.csv')
pd.set_option('display.max_columns', None)
df.head()
df['Perc.Change'] = (df['Open'] - df['Close']) / df['Open']*100
print(df)
df.to_csv('data/GOOG_modified.csv', index = False)