import pandas as pd

# Initializing the dataframe
df = pd.DataFrame({'dates': ['05Sep2009','13Sep2011','21Sep2010']})
# Converting date to the desired format
df['dates'] = pd.to_datetime(df.dates)
print(df)