#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("temp.txt","w")
s='one root '
f.write(s)
f.close()
 
f2 = open("der.txt","w") 
f1 = open("temp.txt","r")
for line in f1:
    f2.write(line)
f1.close()
f2.close()
 
f3= open("der.txt","r")
s1 = f3.read()
print(s1)
f3.close()


# In[ ]:




