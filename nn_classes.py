import csv
import random
import numpy as np
from mseiplib import * #seperate file that is importing from

input_Count = 4
hidden1_Count = 10
output_Count = 3
learningRate = 0.05

#Weights
input_hidden1_LayerWeight = np.random.uniform(low=-1, high=1, size=(input_Count,hidden1_Count))
hidden1_output_LayerWeight = np.random.uniform(low=-1, high=1, size=(hidden1_Count,output_Count))

input_hidden1_ThetaWeight = np.random.uniform(low=-1, high=1, size=(input_Count))
hidden1_output_ThetaWeight = np.random.uniform(low=-1, high=1, size=(hidden1_Count))

#Deltas  ^
#Deltas /_\
input_hidden1_Delta = np.zeros((input_Count, hidden1_Count))
hidden1_output_Delta = np.zeros((hidden1_Count, output_Count))


deltaOutputLayer = np.zeros((output_Count))
deltaHiddenLayer = np.zeros((hidden1_Count))
	
#Acceleration
prevdeltaOutputLayer =  np.zeros((output_Count))
prevdeltaHiddenLayer =  np.zeros((hidden1_Count))
	

#Outputs
hidden_Output = np.zeros((hidden1_Count))
final_Output = np.zeros((output_Count))





#Start of Neural Network

input = np.array([])

with open('iris.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	
	for row in csvreader:
		input = np.append(input, row)
		
finalinput = np.reshape(input, (-1, 7)) # reshapes the 1d array to 2d

#Testing out final numpy array
#You may use these arrays as normal arrays or call numpy functions like np.zero etc.
print(finalinput)
print(finalinput[0][0])
print(len(finalinput))
print(len(finalinput[0]))

print(Neuron.testfunction())
print(Neuron.returnfunction())
finalinput[0][0] = 100
print(finalinput[0])
finalinput[0][0] = 5.1

'''Creating Classes'''

simplelist = []

for count in range(5):
	x = Neuron(5) #assigning values through the constructor
	x.attr = count #you can append more variables outside the class this way
	simplelist.append(x)
	print(simplelist[count].kind)
	print(simplelist[count].attr)