
# coding: utf-8

# In[1]:

x=6


# In[2]:

print(x,"is of type:",type(x))


# In[3]:

y=4.5


# In[5]:

print(y,'is of type:',type(y))


# In[6]:

a=5.0


# In[7]:


print(a,"is of type:",type(a))



# In[8]:

string3='''Standard
chartered
bank
'''


# In[9]:

print(string3)


# In[10]:

string1='Welcome to Standard Chartered Bank'


# In[11]:

print(string1)


# In[12]:

x="AXESSACADEMY"


# In[13]:

print("first charater of string is:",x[0])


# In[15]:

print("last character of string is",x[-1])


# In[16]:

print("last character of string is;",x[-1])


# In[17]:

string1="axess Academy"


# In[18]:

print("Length of the string",len(string1))


# In[19]:

print("String upper case",string1.upper())


# In[20]:

string2="aXess;Acedemy"


# In[21]:

print("split string in to substrings,with seperator,")


# In[22]:

print(string2.split(","))


# In[23]:

print(string2.split(";"))


# In[24]:

x=3
y=4
z=8


# In[25]:

print('Sum of x y is:',x+y)


# In[26]:

print("difference of x y is;", x-y)


# In[27]:

print('multiplication of x y is;',x-y)


# In[28]:

print("modulus of x y is:",x%y)


# In[29]:

print("Division of x y is", x/y)


# In[30]:

print("exponential of x to power of y is:",x**y)


# In[31]:

print("output of BODMAS rule on x y z:",())


# In[32]:

def mul(num1,num2):
    return(num1*num2)
x=5
y=6
print(mul(x,y))


# In[33]:

x=10
y=12
print('x.y is',x>y)


# In[34]:

print('x<y is',x<y)


# In[35]:

print("x==y is", x==y)


# In[36]:

print('x!=y')


# In[37]:

x=True
y=False
print('x and y is',x and y)


# In[38]:

print("x or y is",x or y)


# In[39]:

print("not x is",not x)


# In[40]:

x=4
y=6
print('x & y operator output is:',x&y)
print("x or y operator output is:",x/y)
print('x XOR y is:',x^y)
print("not of x is:",~x)
print("right shift by 2:",x>>2)
print("left shift by 2")


# In[41]:

x=["apple","banana"]
y=["apple","banana"]
z=x


# In[42]:

print("x is z:", x is z)
print("x is y:",x is y)
print("x==y",x==y)
print("x is not y",x is not y)


# In[43]:

x=["apple","banana"]
print("banana" in x)
print("pineapple" not in x)
y=[1,2,3,4,5]
print(6 in y)


# In[44]:


num=input("Enter number:")
print(num)
name=input("Enter name:")
print(name)
print(num,"type of number",type(num))
print(name,"type of name",type(name))


# In[48]:

a=10
b=33
if a>b:
    print("a is greater than b")
elif a==b:
          print("a and b are equal")
else:
          print("a is lesser than b")
        


# In[49]:

a=10
b=33
if a>b:
    print("a is greater than b")


# In[50]:

i = 1
while i < 6:
    print(i)
    i += 1


# In[ ]:

i = 1
while i < 6:
    print(i)
    if(i==3):
        break 
        i += 1
        


# In[ ]:

i=0
while i<6:
    i+=1
    if i==3:
        continue
        print(i)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



