#!/usr/bin/env python
# coding: utf-8

# In[2]:



f=open("temp.txt","w")

f.write("mint\n")
f.write("micky\n")
f.write("jumped\n")
f.write("into\n")
f.write("river\n")
f.close()
a = open("temp.txt")
lines = 3
for i in range(lines):
   line = a.readline()
   print(line)


# In[ ]:




