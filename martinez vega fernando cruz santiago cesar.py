#!/usr/bin/env python
# coding: utf-8

# ## Trimmed Mean

# In[9]:


v1=0
values = int(input("How much datas would you like introduce?:  ")) # number of datas that we will add
datas = []
total = 0
for i in range(0,values):
    x = int(input("Put a number: "))
    datas.append(x)
trimmed = int(input("Write the percent that you want: ")) #percentage to remove the extras datas
trimmeds = trimmed * .01 
percentage = round(values * trimmeds)
if percentage <= 0.5:
    percentage = 0
elif percentage > 0.5:
    percentage = round(percentage)
print ("numbers to remove:", percentage)
tream = sorted(datas) #sorted is for order the datas of the set
print("order",tream)
net = org[percentage:values - percentage]
print("the list without the percentage is :",net)
suma = sum(net)
plas = len(net)
sample = float(suma/plas)

print("TRIMMED MEAN: ", sample) #fnish the job


# ## 5
# 3## 
