#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("temp.txt","w")
 
f.write("mint\n")
f.write("micky\n")
f.write("jumped\n")
f.write("into\n")
f.write("river\n")
f.close()
 
with open("temp.txt") as k:
    m =k.readlines()
    print(m)


# In[ ]:




