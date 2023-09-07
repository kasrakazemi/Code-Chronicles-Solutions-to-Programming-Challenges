#!/usr/bin/env python
# coding: utf-8

# In[128]:


import collections

def cycle(s, n):
    d = collections.deque(s)
    d.rotate(n)
    return "".join(d)

number= '1234'

def big_add(num1,num2):
    answer= ""
    carry = 0 
    while (num1 !="")or (num1 !="") or (carry !=0):
        if (num1 !="") and (num2 != ""):
            temp= int(num1[-1])+ int(num2[-1])+ carry
        if (num1=="")and (num2==""):
            temp= carry
        if (num1 =="") and (num2 !=""):
            if carry ==0:
                answer = num2+answer
                break
            temp = int(num2[-1])+ carry
        if (num1 !="")and (num2 ==""):
            if carry ==0:
                answer= num1+ answer
                break
            temp= int(num1[-1])+ carry
        answer= str(temp%10)+answer
        carry= int(temp/10)
        num1 = num1[:-1]
        num2 = num2[:-1]
    return (answer)


# In[178]:


number1= (input())
number2 = (input())
number1=number1.replace(" ",'')
number2=number2.replace(" ",'')


# In[179]:


SumResult= 1
for i in range (len(number1)+1):
    number1Rotaded= cycle(number1,-i)
  
    for j in range (len(number)+1):
        number2Rotaded= cycle(number2,j)
        Sum = big_add(number1Rotaded[1:4],number2Rotaded[1:4])[1:]
        SumResult = int(Sum)
        #print(SumResult)
        if int(Sum)%6==0:
            print('Boro joloo :)')
            break
#         if SumResult%6!=0:
#             print('Gir oftadi :(')
#             break

    if SumResult%6!=0:
        print('Gir oftadi :(')
        
    break

         


# In[ ]:





# In[ ]:





# In[ ]:




