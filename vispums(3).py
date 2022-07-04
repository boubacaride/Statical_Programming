#CPSC-51100, Spring 2019
#Boubacar Ide, Edith Castro Bravo, Sriram Siripuram
#02/25/19
#Programming Assignment #6
#Boubacar - Original Draft (2/20)
#Sriram - Revision #1 (2/25)
#Edith - Revision #2 (2/26)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Creates dataframe from data file
filename = 'ss13hil.csv'
df = pd.read_csv(filename)

# Print our output header as instructed
string1 = 'CPSC-51100,[2nd Semester][2018-2019]'
string2 = 'Name: [Edith Castro Bravo/Sriram Siripuram/Boubacar Ide]'
string3 = 'PROGRAMING ASSIGNMENT #5'
print(string1 + '\n' + string2 + '\n' + string3+'\n')

#Function to create a Pie chart
def upper_left():
    HHL = list()
    translation_dict = {1:'English only',
    2:'Spanish',
    3:'Other Indo-European languages',
    4:'Asian and Pacific Island languages',
    5:'Other'}

    counter = {key:0 for key in translation_dict.values()}
    for record in df['HHL']:
        if np.isnan(record):
            pass
        else:
            counter[translation_dict[record]] +=1

    return counter

# Function to create a Histogram with superimposed KDE plot
def upper_right():
    HINCP = df['HINCP'].dropna()
    return HINCP

# Function to create a Bar Chart
def lower_left():
    VEH = df['VEH']
    WGTP = df['WGTP']
    veh_values = list()
    counts = list()
    for veh in VEH.unique():
        if np.isnan(veh) :
            pass
        else:
            veh_values.append(veh)
            counts.append(df.loc[df['VEH'] == veh,'WGTP'].sum()/1000)
    return (veh_values,counts)

#Function to create a Scatter Plot
def lower_right():
    translate_dict = {1:0}
    for i in range(2,69):
        if i <= 21:
            translate_dict[i] = translate_dict[i-1]+50
        elif i <= 62:
            translate_dict[i] = translate_dict[i-1]+100
        elif i  <= 64:
            translate_dict[i] = translate_dict[i-1]+500
        else:
            translate_dict[i] = translate_dict[i-1]+1000
    TAXP = list()
    for record in df['TAXP']:
        if np.isnan(record):
            TAXP.append(translate_dict[1])
        else:
            TAXP.append(translate_dict[int(record)])
    return TAXP

fig, axes = plt.subplots(2, 2, figsize = (20, 10))

# Call function to plot Pie chart. Plots pie chart with legend, labels, and title
x = upper_left()
a0 = axes[0][0].pie(x.values(),shadow=False, startangle=241)
axes[0][0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# add colors
# labels = ['English only','Spanish','Other Indo-European languages', 'Asian and Pacific Island languages','Other']
axes[0][0].legend(x.keys(),  fontsize=11.5,bbox_to_anchor=(0, 0,0.5,1))
axes[0][0].set_ylabel('HHL')
axes[0][0].set_title('Household Language')

# Call function to plot (Histogram + KDE Plot). Plots Histogram with labels and title.
x = upper_right()
a1 = axes[0][1].hist(x, bins=np.logspace(1,7,100), density=True, label='Income',color='darkseagreen')
axes[0][1].set_title('Distribution of Household Income')
axes[0][1].set_xscale('log')
axes[0][1].set_xlabel('Household Income ($) - Log Scaled')
axes[0][1].set_ylabel('Density')
ax12 = x.plot.kde(ax = axes[0][1],ls = '--',color='k')

#Plots the Lower Left Subplot (Bar Chart) with labels and title
x,y = lower_left()
a2 = axes[1][0].bar(x,y,color='red')
axes[1][0].set_title('Vehicles Available in Households')
axes[1][0].set_xlabel('# Vehicles')
axes[1][0].set_ylabel('Thousands of Households')
axes[1][0].set_xlim(left=-0.4)

# Plots the Lower Right Subplot (Scatter Plot) with labels and title
x = lower_right()
a2 = axes[1][1].scatter(df['VALP'].values,x,c=df['MRGP'].values,s=df['WGTP'],cmap = 'coolwarm')
axes[1][1].set_title('Property Taxes vs. Property Values')
axes[1][1].set_xlabel('Property Value ($)')
axes[1][1].set_ylabel('Taxes ($)')
axes[1][1].set_xlim(left = 0,right = 1200000)
axes[1][1].set_ylim(bottom = 0)
cbar1 = fig.colorbar(a2, ax=axes[1][1])
cbar1.set_ticks([1250,2500,3750,5000])  # vertically oriented colorbar
cbar1.set_label('First Mortage Payment (Monthly $)')

# Adjusts the spacing of the subplots and saves the figure in a .png format
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.savefig("frame.png")





