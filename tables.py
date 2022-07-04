'''CPSC-51100,[2nd Semester][2018-2019]
Name: [Boubacar Ide]
PROGRAMING ASSIGNMENT #7'''

import pandas as pd
import numpy as np

# Loads the ss13hil.csv file that contains the PUMS dataset and create a DataFrame
df = pd.read_csv('ss13hil.csv')

# Print our output header as instructed
string1 = 'CPSC-51100,[2nd Semester][2018-2019]'
string2 = 'Name: [Boubacar Ide]'
string3 = 'PROGRAMING ASSIGNMENT #7'
print(string1 + '\n' + string2 + '\n' + string3+'\n')

# TABLE 1: Statistics of HINCP - Household income (past 12 months), grouped by HHT - Household/family type  
# - Table uses the HHT types (text descriptions) as the index  
# - Columns mean, std, count, min, max  
# - Rows is sorted by the mean column value in descending order
pd.options.display.max_colwidth = 65 # To creat 65 caracteres space in on column
HHT_dict =  ['Married couple household',
             'Other family household:Male householder, no wife present',
             'Other family household:Female householder, no husband present',
             'Nonfamily household:Male householder:Living alone',
             'Nonfamily household:Male householder:Not living alone',
             'Nonfamily household:Female householder:Living alone',
             'Nonfamily household:Female householder:Not living alone']
             
# Create a table to group the data
table = df.groupby(['HHT']).agg({'HINCP':['mean','std','count','min','max']})

# Extract only HINCP records on the groupping
table = table['HINCP']

# Convert max and min to integers
table['max'] = table['max'].astype(int)
table['min'] = table['min'].astype(int)

# Create a column with text descriptions
table['HHT - Household/family type'] = HHT_dict

# Sort the values according mean column
table = table.sort_values(by='mean',ascending=False)

# set the index of the table to the text description
table = table.set_index('HHT - Household/family type')

print('')
print('*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***')
print(table,'\n')

# TABLE 2: HHL - Household language vs. ACCESS - Access to the Internet (Frequency Table)  
# - Table uses the HHL types (text descriptions) as the index  
# - Columns text descriptions of ACCESS values  
# - Each table entry is the sum of WGTP column for the given HHL/ACCESS combination, divided by the sum of WGTP
# - values in the data. Entries formatted as percentages.  
# - Table includes marginal values ('All' row and column).  

HHL = ['English only',
       'Spanish',
       'Other Indo-European languages',
       'Asian and Pacific Island languages',
       'Other language']

ACCESS =  {1.0:'Yes w/ Subsrc.',2.0:'Yes, wo/ Subsrc.',3.0:'No'}
# create a pivit table
table_ACCESS = df.pivot_table(index = 'HHL',columns = 'ACCESS',values=['WGTP'], aggfunc=[np.sum])

# Modify the table to have values as percentages
table_ACCESS = table_ACCESS/table_ACCESS.sum().sum()*100

# Create column for text descriptions
table_ACCESS['HHL - Household language'] = HHL

table_ACCESS = table_ACCESS.set_index('HHL - Household language')

# Rename the columns according a dictionary Access
table_ACCESS = table_ACCESS.rename(columns = ACCESS)
# ceate the 'All' column and 'All' row
table_ACCESS['sum','WGTP','All'] = table_ACCESS.sum(axis=1)
table_ACCESS.loc['All'] = table_ACCESS.sum(axis=0)
# Print Talbe 2
print('*** Table 2 - HHL vs. ACCESS - Frequency Table ***')
print(table_ACCESS.applymap(lambda x: '%.2f' % x +'%'),'\n')

# TABLE 3: Quantile Analysis of HINCP - Household income (past 12 months)  
# - Rows corresponds to different quantiles of HINCP: low (0-1/3), medium (1/3-2/3), high (2/3-1)  
# - Columns displayed: min, max, mean, household_count  
# - The household_count column contains entries with the sum of WGTP values for the corresponding range of HINCP
# values (low, medium, or high)

quants = list()
household_count = [0,0,0]
# get the low quantile
lower_bd = df['HINCP'].quantile(1/3)
#get the medium quantile
medium_bd = df['HINCP'].quantile(2/3)
# Create a new dataframe with 'HINCP','WGTP' and no na
df_nona = df.loc[:,['HINCP','WGTP']].dropna()
for i in df_nona.index.values:
    if df_nona.loc[i,'HINCP'] <= lower_bd:
        quants.append('low')
        household_count[0] += df_nona.loc[i,'WGTP']
    elif df_nona.loc[i,'HINCP'] <= medium_bd:
        quants.append('medium')
        household_count[1] += df_nona.loc[i,'WGTP']
    else:
        quants.append('high')
        household_count[2] += df_nona.loc[i,'WGTP']

table_HINCP = df_nona
# create a column of 'mean','max','min'
table_HINCP['stats'] = quants 
table_summary = table_HINCP.groupby(['stats']).agg(['mean','max','min'])['HINCP']
table_summary = table_summary.sort_values(by='max',ascending=True)

# reorder the columns
table_summary = table_summary[['min','max','mean']]

#create household_count
table_summary['household_count'] = household_count
table_summary['min'] = table_summary['min'].astype(int)
table_summary['max'] = table_summary['max'].astype(int)

# Set the index as 'HINCP'
table_summary.index.names = ['HINCP']

# Print table 3
print('*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***')
print(table_summary)





















