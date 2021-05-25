#!/usr/bin/env python
# coding: utf-8

# # Garbage Calender

# In[1]:


import datetime
lst = ["Devang", "Neel", "Priyank", "Riken", "Ruchit", "Tejas", "Vikas"]

dates_dict = {}

previousby_dict = {}

dates_dict1 = {}
start = datetime.datetime(2021, 4, 12)
startdate = datetime.datetime(2021, 4, 12)
r=1
while startdate < datetime.datetime.now():
    dates_dict1[r] = startdate
    startdate = startdate + datetime.timedelta(days=7)
    r = r+1
#print(dates_dict1)
#print(len(dates_dict1))

next = lst[len(dates_dict1)%len(lst)-1]
#print(f'next : {next}, Date : {startdate}')

lst3=[2,1,0]
previous = startdate
pre_name=len(dates_dict1)%len(lst)-2
next_name = len(dates_dict1)%len(lst)

pre3 = []
nxt3 = []
for i in lst3:
    if pre_name==-1:
        pre_name=6
    previous = previous - datetime.timedelta(days=7)
    pre3.append(f"Name : {lst[pre_name]}, Date : {previous}")
    pre_name = pre_name-1
    
next_date = startdate
for i in lst3:
    if next_name==7:
        next_name=0
    next_date = next_date + datetime.timedelta(days=7)
    nxt3.append(f'Name : {lst[next_name]}, Date : {next_date}')
    next_name = next_name+1
    
print("---------previous-------")
for i in lst3:
    print(pre3[i])

print("---------next-------")
print(f'next : {next}, Date : {startdate}')
print("---------coming soon-------")
for i in [0,1,2]:
    print(nxt3[i])


# In[ ]:




