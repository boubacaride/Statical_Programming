'''CPSC-51100,[2nd Semester][2018-2019]
Name: [Boubacar Ide]
PROGRAMING ASSIGNMENT #5'''

# Import pandas
import pandas as pd

# Print our output header as instructed
string1 = 'CPSC-51100,[2nd Semester][2018-2019]'
string2 = 'Name: [Boubacar Ide]'
string3 = 'PROGRAMING ASSIGNMENT #5'
print(string1 + '\n' + string2 + '\n' + string3+'\n')

# Loads the cps.csv file and converted to the DataFrame as instructed
df_cps = pd.read_csv('cps.csv',usecols =['School_ID',
'Short_Name',
'Is_High_School',
'Zip',
'Student_Count_Total',
'College_Enrollment_Rate_School',
'Grades_Offered_All',
'School_Hours'])

# From the Grades_Offered_All generate Lowest_Grade_Offered column, and add it to the DataFrame
list_grades = df_cps['Grades_Offered_All'].str.split(',',expand=True)
df_cps['Lowest_Grade_Offered'] = list_grades.iloc[:,0]

# From the Grades_Offered_All generate Highest_Grade_Offered column, and add it to the DataFrame
list_grades = df_cps['Grades_Offered_All'].str.split(',',expand=False).values
df_cps['Highest_Grade_Offered'] = [c[-1] for c in list_grades]

# Get the Schools Starting Hours
hours = df_cps['School_Hours'].str.findall('([1-9]):*')
hours = hours.map(lambda x: '' if type(x) != list or x == [] else x[0])
df_cps['Starting_Hour'] = hours

# From the DataFrame Drop the following columns: School_Hours and Grades_Offered_All
df_cps_mod = df_cps.drop(['School_Hours','Grades_Offered_All'],axis=1)

# Replace the missing numeric values with the mean for that column. 
df_cps_mod = df_cps_mod.fillna(df_cps.mean())

# Display the first 10 rows of the dataframe.
df_cps_mod.set_index('School_ID', inplace=True)# Use the School_ID as index for the DataFrame
pd.set_option('display.expand_frame_repr', False)
print(df_cps_mod.head(10))
print('')

# Get The College Enrollment Rate for High Schools in The Data Set
df_cps_High = df_cps_mod[(df_cps_mod['Is_High_School'])]

# Calculate The Mean, The Standard Deviation for College Enrollment Rate for High Schools
mean_CER = df_cps_High['College_Enrollment_Rate_School'].mean()
std_CER = df_cps_High['College_Enrollment_Rate_School'].std()
print('College Enrollment Rate for High Schools = {:.2f} (sd={:.2f})\n'.format(mean_CER,std_CER))

# Calculate The Mean, The Standard Deviation of Student_Count_Total for non-High Schools
df_cps_NotHigh = df_cps_mod[(df_cps_mod['Is_High_School'] == False)]
mean_SCT = df_cps_NotHigh['Student_Count_Total'].mean()
std_SCT = df_cps_NotHigh['Student_Count_Total'].std()
print('Total Student Count for non-High Schools = {:.2f} (sd={:.2f})\n'.format(mean_SCT,std_SCT) )


print('Distribution of Starting Hours')
# Get the the total of the number of school that start at 7, 8, and 9
for value in df_cps_mod['Starting_Hour'].unique():
    if type(value) == str and value != '':
        print('{}am: {}'.format(value,sum(df_cps_mod['Starting_Hour']==value)))
print('')

# d.Number of schools outside of the Loop Neighborhood
# (i.e., outside of zip codes 60601, 60602, 60603, 60604, 60605, 60606, 60607, and 60616)
neighborhood = [60601, 60602, 60603, 60604, 60605, 60606, 60607, 60616]
outside_the_loop = len(df_cps['Zip']) - sum(df_cps['Zip'].isin(neighborhood))
print('Number of schools outside the loop: {}'.format(outside_the_loop))







