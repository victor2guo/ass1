import pandas as pd
def clean(input_file1,input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df = pd.merge(df1, df2, left_on="respondent_id", right_on="id").drop('id', axis=1)
    df.dropna(inplace=True)
    df = df[df['job'].str.contains('insurance') == False]
    df = df[df['job'].str.contains('Insurance') == False]
    return df

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Clean respondent data')
    parser.add_argument('contact_info_file', type=str, help='respondent_contact.csv')
    parser.add_argument('other_info_file', type=str, help='respondent_other.csv')
    parser.add_argument('output_file', type=str, help='output_file.csv')
    args = parser.parse_args()

cleaned = clean(args.contact_info_file, args.other_info_file)
print('The shape of out file is: ', cleaned.shape)
cleaned.to_csv(args.output, index=False)