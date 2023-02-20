import pandas as pd
import numpy as np
import argparse

df1 = pd.read_csv('respondent_contact.csv')
df2 = pd.read_csv('respondent_other.csv')

df1.rename(columns = {'respondent_id':'id'},inplace = True)
data = pd.merge(df1,df2,on = 'id')

data.dropna(inplace = True)

data = data[~data['job'].str.contains('insurance')]
data = data[~data['job'].str.contains('Insurance')]

data.to_csv('output_file.csv')

parser = argparse.ArgumentParser(description='Ass1')
parser.add_argument('respondent_contact.csv', type=str, help='contact_info_file')
parser.add_argument('respondent_other.csv', type=str, help='other_info_file')
parser.add_argument('output_file.csv', type=str, help='output_file')

args = parser.parse_args()

print(args.file1, args.file2, args.file3)