#!/usr/bin/env python
# coding: utf-8

# In[2]:


def file_size(fname):
 import os
 statinfo = os.stat(fname)
 return statinfo.st_size
print("File size is :",file_size("temp.txt"))


# In[ ]:




