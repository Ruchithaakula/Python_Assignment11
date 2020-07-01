#!/usr/bin/env python
# coding: utf-8

# In[1]:


filename = "temp.txt"
count = 0
with open(filename, 'r') as l:
    for line in l:
        count += 1
print("Total number of lines is:", count)


# In[ ]:




