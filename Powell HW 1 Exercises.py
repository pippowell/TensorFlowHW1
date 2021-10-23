#!/usr/bin/env python
# coding: utf-8

# In[52]:


#As requested, this code also appears in the separate module cat.py

#Define the class CuteCat which allows a user to create cats and give them names
#Include two functions in the CuteCat class, one which runs an initial greeting based on which cat is going first,
#the other which runs a response based on which cat is going second

class CuteCat:
    def __init__(self, name):
        self.name = name
        
    def greet(self, name2):
        print ("Hi, my name is " + self.name         + ". I am a cute cuddly cat. I see you are too, " + name2         + ". Let's purr so the two-leggeds will give us food.")
        
    def respond(self, name2):
        print ("Hi, " + name2 + ". That sounds like a great idea. Let's do it because I'm hungry.")
        
    


# In[54]:


#this code also appears in the separate module kittyconcert.py

#import cat (command cannot be run here as cat is not a separate module here)
cat1 = CuteCat("Harry")
cat2 = CuteCat("Snowbell")
cat1.greet(cat2.name)
cat2.respond(cat1.name)


# In[9]:


#Square and print all values from 0-100 using a single line of code (f-string method)
print(f"{[x**2 for x in range(1,101)]}")


# In[10]:


#Work with the same list, but this time only print the squared values if they are even (divisible by 2)
print(f"{[x**2 for x in range(1,101) if x**2 % 2==0]}")


# In[17]:


#Create a generator which outputs one "Meow" on initial call and then on subsequent calls outputs a number of "Meow"s
#equal to the number of "Meow"s printed by the previous call, times 2

#generator self-limits to 5 runs to save resources and b/c some programs may not allow execution of code which will run
#in an infinite loop 

def meowGenerator():
    x = 1
    meowlist = list()
    for i in range(5):
        for i in range(x):
            meowlist.append("Meow")
        yield (meowlist)
        x = x*2
        meowlist = list()
  
#Call the generator 

run1 = meowGenerator()
for i in run1:
    print (i)


# In[48]:


#Import required packages (numpy)
import numpy as np
import decimal as dc

#Initialize the arry with the specified parameters:
#(mean/center = 0, standard deviation = 1, 5 rows, 5 columns, values normally distributed and random)
x = np.random.normal(0,1,(5,5))

#Print the original array
print('This is the original array:')
print(x)

#Create a blank line in the output for easier viewing
print()

#Unsure of exact instructions for this step (possible typo in instruction sheet). Interpreted the instructions as
#"replace all values in the array which are larger than 0.09 with that value squared, else with 42."
x = np.where(x > dc.Decimal(0.09), x**2, 42)

#Print the modified array
print('This is the updated array with the requested replacements made:')
print(x)

#Create a blank line in the output for easier viewing
print()

#Isolate the fourth column of the modified array
z = x[:,3]

#Printing a column vertically makes more sense than the horizontal output that would occur if z were printed as is
#Print the numbers from the fourth column, now contained in z, vertically for easier viewing
print('This is the fourth column of the updated array:')
for i in z:
    print (i)


# In[ ]:




