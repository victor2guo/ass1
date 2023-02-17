import pandas as pd

df1 = pd.read_csv('respondent_contact.csv')
df2 = pd.read_csv('respondent_other.csv')

df1.rename(columns = {'respondent_id':'id'},inplace = True)
data = pd.merge(df1,df2,on = 'id')

data.dropna(inplace = True)

data = data[~data['job'].str.contains('insurance')]
data = data[~data['job'].str.contains('Insurance')]

data.to_csv('output_file.csv')