'''CPSC-51100,[2nd Semester][2018-2019]
Name: [Boubacar Ide]
PROGRAMING ASSIGNMENT #4'''

# Import panda library
import pandas as pd

# Import the data and choose only the make and aspiration column
df = pd.read_csv('cars.csv',usecols=['make','aspiration'])

# Get the aspiration type in the data set
aspirations = df['aspiration'].unique()
# Get the make type in the data set
makes = df['make'].unique()

# Print our output header as instructed
string1 = 'CPSC-51100,[2nd Semester][2018-2019]'
string2 = 'Name: [Boubacar Ide]'
string3 = 'PROGRAMING ASSIGNMENT #4'
print(string1 + '\n' + string2 + '\n' + string3+'\n')

# Calculate the probability of each aspiration of a make
# Display the output as instructed
for make in makes:
    for aspiration in aspirations:
        prob = len(df[(df['aspiration'] == aspiration) & (df['make'] == make)])/len(df[(df['make'] == make)])
        print('Prob(aspiration={}|make={}) = {:.2f}%'.format(aspiration,make,prob*100))
print('')

# Calculate the probability of each make in the data set
# Display the output as instructed
len_df = len(df)
for make in makes:
    prob = len(df[(df['make'] == make)])/len_df
    print('Prob(make={}) = {:.2f}%'.format(make,prob*100))







