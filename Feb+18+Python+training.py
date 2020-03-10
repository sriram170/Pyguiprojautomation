
# coding: utf-8

# In[10]:

# try new coding

x=6
print (x, "is of type:" ,type(x))

y=4.5
print (y, "is of type:", type (y))

a=5.0

print (a, "is type :",type(a))

b=a+3j
print(b,"is type:", type (b))

d= 458374659038746

print (d,"is type:", type (d))



# In[ ]:

string1="welcome to SCB"
print(string1)
string2="chartered bank"
print(string2)
string3 = '''standard
chartered
bank'''
print(string3)


# In[ ]:

# square bracket to pick the values in the string

X= "ACCESSACADEMY"

print("firts charecter is:", X[0])
print("last character is ", X[-1])
print ("first five character is ", X[-12:-7])
print ("range of charactere is ", X[3:-7])


# ### string split and len
# 
# string1="aXess Academy"
# print ("length of the strin:", len(string1))
# 
# print ("String lower case:", string1.lower())
# 
# print ("String upper case:", string1.upper())
# 
# string2="Acxess, Academy"
# 
# print ("String split with separator", string2.split(","))
# 
# 

# In[11]:

x=3
y=4
z=8

print ("sum of xy is:", x+y)

print ("difference if x y is " ,x-y)

print ("modulas of xy is:", x%y)

print ("multuplication of xy is:" ,x*y)

print ("division of xy is:", x/y)

print ("exponential of xy" , x**y)

print ((x+y)*z-y)


# In[ ]:

x=True
y=False

print("x and y is",x and y)

print(" x or y is",x or y)

print ("not x is ",not x)


# In[12]:

num = input("Enter the num:")

print (num)

name=input("enter then name:")

print(name)

print(num,"type of number",type(num))

print (name, "type of name",type(name))



# In[13]:

a=10
b=33

if a>b:
    print("it is true")

elif a==b:
    print("a and b are equal")
else:
        print("a is lesser than b")
        
    


# In[14]:

i=1

while i<6:
    print (i)
    i+=1
    


# In[ ]:

i=1
while i<6 :
    print (i)
    if (i==3):
        break
        i+=1
        break
        
    


# In[ ]:

i=0
while i <6:
    i +=1
    if i==3:
        continue
        print(i)
        


# In[3]:

print("adad")


# In[4]:

list1 =[1,2,3,4,5,]

for x in list1:
    
    print (x)


# In[6]:

fruits=["apple", "banana","mango"]

for x in fruits:
 print(x)
    
        


# In[7]:

for x in "bananan":
    print(x)
    


# In[9]:

for x in range(2):
    print(x)


# In[1]:

# answer of 2

x=12
n=1

while x == 12:
    y=x*n
    print( str(x) + "*" + str (n) + "=" + str(y))
    n+=1
    if y==120:
        break
    
    
    




 







# In[9]:

sub1 =input ("enter the mark of the sub1 ")
sub2=input ("etner the mark of sub2 ")
sub3=input("enter the mark of sub3 ")
sub4=input("enter the mark of sub4 ")
abg=4

x=((int(sub1+sub2+sub3+sub4)/abg))

if int(x) > 90:
    
    print("Grade:A")
    
    if int(x) <90 and  x >80:
        
        print ("Grade:B")
        
    if int(x) <80 and x>70:
            print("Grade:C")
            
    if int(x)<70 and x>60:
                print("Grade:D")
            
    else:
                     print("Grade:F")
            
        
        
    
    


# In[10]:

thislist=["a","b","c"]

print("list value:", thislist)

print("Second list is", thislist[1])

for x in thislist:
    print(x)

if "a" in thislist:
    
    print("a is in the list")
    


# thislist=["a","b","c"]
# 
# thislist.append("pineapple")
# 
# print (thislist)
# 
# thislist.insert(2,"banana")
# 
# print(thislist)
# 
# thislist.remove("c")
# 
# print(thislist)
# 
# thislist.pop()
# 
# print(thislist)
# 
# del thislist [0]
# print(thislist)
# 
# 
# 

# In[4]:

thistuple=("a","b","c")

print(thistuple)

print(thistuple[1])

print(len(thistuple[1]))

if "apple" in thistuple:
    print("yes")

else:
    print ("no")




# In[3]:

thisset={"aa","ff","cc"}

print(thisset)

for x in thisset:
    
    print(x)
    
    print("aa" in thisset)
    
    thisset.add("nbanana")
    
    print (thisset)
    
    print(len(thisset))
    
    


# In[7]:

thisset={"aa","ff","cc"}

thisset.remove("aa")

print(thisset)

thisset.discard("aa")

print (thisset)


# In[16]:

set1={"apple","mango","banana","dub"}
set2=("google","mniceo","anna")

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.issubset(set2))
print(set1.issuperset(set2))

set1.update(set2)




# In[21]:

thisdic={"brand":"maruthi","model":"ertiga","year":2011}

print(thisdic)

print(thisdic.values())

print ("Model", thisdic["model"])

for x in thisdic:
    print(x,":", thisdic[x])
    
    
      


# In[23]:

thisdic={"brand":"maruthi","model":"ertiga","year":2011}

print("use of items function")

for x,y in thisdic.items():
    print(x,y)


# In[24]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
print(file.read())
file.close()


# In[25]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
print(file.read(5))
file.close()


# In[26]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
print(file.readline())
file.close()


# In[27]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
for x in file:
    print(x)
file.close()


# In[31]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt" ,"a")
file.write("this is nothing \n")
file.close()
file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
print(file.read())
file.close()




# In[33]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt", "w")
file.write ("earlier no was delete \n")
file.close()
file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
print(file.read())
file.close



# In[38]:

file=open("C:\\Users\\1416363\\Desktop\\practice.txt","x")
file.write ("earlier no was delete \n")
file.close()
file=open("C:\\Users\\1416363\\Desktop\\practice.txt")
print(file.read())
file.close


# In[42]:

import os

file.close
if os.path.exists("C:\\Users\\1416363\\Desktop\\practice.txt"):
    
    os.remove("C:\\Users\\1416363\\Desktop\\practice.txt")
    print("file delted")
else:
        print("File does not exists")


# In[1]:

import matplotlib.pyplot as plt
x=[1,2,3,4]

y=[5,16,27,28]

plt.plot(x,y)
plt.show()


# In[ ]:

#test for module 2

thislist= [1,2,3,4,5,6]

n=0
w=0
while n==0:
       w =w+thislist[n]
n+=1
print (w) 
if n>7:
    break
                
   

    


# In[4]:

set1={"1","2","3","4"}
set2=("4","5","6")

print("Set1:",set1)
print ("Set2",set2)

print("uniion result",set1.union(set2))

print("intersection result",set1.intersection(set2))

print("Subset reuslt",set1.issubset(set2))





# In[13]:

thisdic={"ID":"59912","Name":"Mahesh","location":"Banguluru"}

print(thisdic)

thisdic["grade"]="5a"

print(thisdic)

for x in thisdic:
    print (x,thisdic[x])



# In[17]:

import matplotlib.pyplot as plt
x=[1,2,3,4]

y=[1,4,9,16]

plt.title("First plot")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.plot(x,y)
plt.show()


# In[21]:

import matplotlib.pyplot as plt
import matplotlib.style as stl

stl.use('ggplot')

x1=[1,2,3,4]

x2=[1,4,9,16]

x4=[1,3,5,6]

y4=[1,6,9,13]

plt.plot(x1,x2, linewidth=5)
plt.plot(x4,y4, linewidth=5)

plt.title("My chart")
plt.xlabel("xchart")
plt.ylabel("ychart")


plt.plot(x,y)
plt.legend
plt.show()


# In[22]:

import matplotlib.pyplot as plt
import matplotlib.style as stl

stl.use('ggplot')

x1=[1,2,3,4]

x2=[1,4,9,16]

x4=[1,3,5,6]

y4=[1,6,9,13]

plt.plot(x1,x2,label="square numbers", linewidth=5)
plt.plot(x4,y4,label="cube numbers", linewidth=5)

plt.title("My chart")
plt.xlabel("xchart")
plt.ylabel("ychart")


plt.plot(x,y)
plt.legend
plt.show()


# In[29]:

import matplotlib.pyplot as plt
import matplotlib.style as stl

stl.use('ggplot')

x1=[1,2,3,4]

y1=[2,4,9,16]

x2=[1,3,5,6]

y2=[3,6,9,13]

plt.bar(x1,y1, color="r")
plt.bar(x2,y2, color="g")

plt.title("My chart")
plt.xlabel("xchart")
plt.ylabel("ychart")


plt.plot(x,y)
plt.legend
plt.show()


# In[ ]:



