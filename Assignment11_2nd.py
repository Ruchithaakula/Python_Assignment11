#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("temp.txt","a")
string = "welcome home "
f.write(string)
f.close()
f= open("temp.txt","r")
s = f.read()
print(s)
f.close()


# In[ ]:




