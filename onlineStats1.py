print("")
# Print the header as instructed
string1 = 'CPSC-51100,[2nd Semester][2019-2019]'
string2 = 'Name: [Boubacar Ide]'
string3 = 'PROGRAMING ASSIGNMENT #1'
print(string1 + '\n' + string2 + '\n' + string3)

# Creating a numberlist list to store the user input
numbursList=[]
# a while loop to control the loop
# if the condition is  true the loop contitnue otherwise break out of the loop
while True:
           x=int(input('Please enter a positif number: '))
           if x>=0 :
                      numbursList.append(x)
           else:
                      break
                      
# Calculate the Mean from the values enter
           value_mean=0
           value_variance=0
           if len(numbursList)==1:
                      value_mean=numbursList[0]
                      value_variance=0
           else:
                      for number in numbursList:
                                 value_mean+=number
                      value_mean=value_mean/len(numbursList)
                      
# Calculate the Variance        
                      for number in numbursList:
                                 value_variance += (number- value_mean)**2
                      value_variance = value_variance/(len(numbursList)-1)
 
# Print out the result           
           print('The mean is {} and variance is {}'.format(value_mean ,value_variance))

                      
                      



    

