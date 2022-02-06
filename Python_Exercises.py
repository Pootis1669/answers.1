
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


# ** What is 7 to the power of 4?**

a=int(input())
b=int(input())
answer=a**b
print(answer)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

s=input()
letters = list(s)
print(letters)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

planet="Earth"
diameter=12742
print("The diameter of",planet,"is",diameter,"kilometers.")


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
# ** What is the main difference between a tuple and a list? **

# Tuple is ______
Immutable
 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

string=input()
count=0
for i in string:
    if i=="@":
        count+=1
    if count==1:
        if i=="@":
            continue
        else:
            print (i,end="")
    

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

def findDog():
    string = input()
    count=string.count("dog")
    if count>0:
        print("True")

        
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
+-

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

def countDog():
string = input()
count1=string.count("dog")
print(count1)
   
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']
n=int(input())
seq = []
for i in range(n):
    seq.append(seq[i])
filtered=filter(lambda a: a[0]=="s", seq)
print(list(filtered))


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

speed=int(input())
is_birthday=int(input())
if is_birthday==0:
    if speed<=60:
        print("No Ticket")
    elif speed>=61 and speed<=80:
        print("Small Ticket")
    elif speed>=81:
        print("Big Ticket")
elif is_birthday==1:
    if speed<=65:
        print("No Ticket")
    elif speed>=66 and speed<=85:
        print("Small Ticket")
    elif speed>=86:
        print("Big Ticket")
    
    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



## Numpy Exercises


    
 #### Create an array of 10 fives
 #### Convert your output into list 
 #### e.g return list(arr) 

import numpy as np
x=np.array([5,5,5,5,5,5,5,5,5,5])
print(list(x))


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr)

import numpy as np
x=np.array([10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50])
print(list(x))


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()

import numpy as np
x=np.linspace(0, 8, 9)
print(x.tolist())


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr)
    
import numpy as np
x=np.linspace(0, 1, 20)
print(x.tolist())



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



### Create an array of size 10*10 consisting of numbers from 0.01 to 1
### Convert your output into list 
### e.g return (arr).tolist()

import numpy as np
x=np.linspace(0.01, 1, 100)
print(x.tolist())


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  array=([[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]])
count=0
a1=[]
a2=[]
a3=[]
A=[]
count=0
for x in range(2,5):
    count=count+1
    for y in range(1,5):
        if count==1:
            a1.append(array[x][y])
        elif count==2:
            a2.append(array[x][y])
        elif count==3:
            a3.append(array[x][y])
A.append(a1)
A.append(a2)
A.append(a3)
print(A)



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[ 2],
  #      [ 7],
  #      [12]])

array=([[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]])
count=0
a1=[]
a2=[]
a3=[]
A=[]
count=0
for x in range(0,3):
    count=count+1
    for y in range(1,2):
        if count==1:
            a1.append(array[x][y])
        elif count==2:
            a2.append(array[x][y])
        elif count==3:
            a3.append(array[x][y])
A.append(a1)
A.append(a2)
A.append(a3)
print(A)



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
    
 

array=([[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]])
count=0
a1=[]
a2=[]
A=[]
count=0
for x in range(3,5):
    count=count+1
    for y in range(0,5):
        if count==1:
            a1.append(array[x][y])
        elif count==2:
            a2.append(array[x][y])
A.append(a1)
A.append(a2)
print(A)


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           

# Great job!
  Thank You
