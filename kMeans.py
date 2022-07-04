'''  
 Boubacar Ide, Edith A Castro Bravo, and Sriram Siripuram 
 02/03/2019
 CPSC-51100, Spring 2019 
 Programming Assignment 2 - K-Means Clustering 
 '''
 
#programer information
print('CPSC-51100, Spring 2019\n' + 'Boubacar Ide\n' + 'Edith A Castro Bravo\n' + 'Sriram Siripuram\n' + 'PROGRAMMING ASSIGNMENT #2')

#open file containing data
input_file = open('prog2-input-data.txt')

#obtain data from file
data = [float(line.rstrip()) for line in input_file]

#obtain number of clusters
clusters = int(input('Enter number of clusters:'))

#define and initialize variables
variable_centroids = dict(zip(range(clusters), data[0:clusters]))
variable_clusters = dict(zip(range(clusters), [[] for value in range(clusters)]))
old_variable_centroids = dict(zip(range(clusters), range(clusters)))
end = 'false'
iteration = 0

#close input file
input_file.close()  

#function to assign points to clusters
def assign_to_clusters(data, variable_clusters, variable_centroids, clusters):
    difference = []
    
    #loop to calculate difference between points and centroids
    for m, n in enumerate(data):
        for o, p in variable_centroids.items():
            difference.append(abs(n-p))  
        
        dict_differences = dict(zip(range(clusters), difference[0:clusters]))      
        min_difference = min(difference)
        
        #loop to add points to clusters
        for x, y in dict_differences.items():
            if y == min_difference: 
                variable_clusters[x].append(n)
        
        difference = []
    return(variable_clusters)

#function to recalculate centroids
def recompute_centroids(variable_clusters, variable_centroids):
    new_variable_centroids  = variable_centroids
    for x, y in variable_clusters.items():
        new_variable_centroids[x] = sum(variable_clusters[x])/len(variable_clusters[x])
    return(new_variable_centroids)

#function to compare centroids and recalculated centroids
def compare_centroids(variable_centroids, old_variable_centroids):
    for x in range(clusters):
        if variable_centroids != old_variable_centroids:
            end = 'false'
        else:
            end = 'true'
    return(end)

#loop to print clusters
while (end == 'false'):
    iteration += 1
    
    print('\nIteration', iteration)
    end = compare_centroids(variable_centroids, old_variable_centroids)
    old_variable_centroids = variable_centroids
    assign_to_clusters(data, variable_clusters, old_variable_centroids, clusters)
    
    #loop to write point assignment to the screen and output file
    for x in range(clusters):
        print(x, variable_clusters[x])
    if end == 'true':
        iteration += 1
        print('\nIteration', iteration)
        for x in range(clusters):
            print(x, variable_clusters[x])
             
        output_file = open('prog2-output-data.txt', 'w+')
        print("\n")
        for m, n in enumerate(data):
            for o, p in variable_clusters.items():
                if n in p:
                    print('point', n, 'in cluster', o)
                    output_file.write('point '+ str(n) + ' in cluster ' + str(o) + '\n')
                     
    variable_centroids = recompute_centroids(variable_clusters, old_variable_centroids)
    variable_clusters = dict(zip(range(clusters), [[] for value in range(clusters)]))

#close output file    
output_file.close()
