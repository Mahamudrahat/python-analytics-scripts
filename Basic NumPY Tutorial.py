#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


my_list=[1,2,3,4]


# In[4]:


np.array(my_list)


# In[5]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


np.array(my_matrix)


# In[9]:


np.arange(0,10)


# In[16]:


arr1=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,0],[12,13,14,15]]])
arr1


# In[22]:


arr=np.array([1,2,3,4],ndmin=5)
print(arr)


# In[23]:


np.zeros(3)


# In[27]:


np.zeros((5,5,5,5))


# In[65]:


arr=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2,4:5])


# In[74]:


np.linspace(0,10,100)


# In[100]:


arr=np.array([1,2,3,0])


# In[101]:


arr.astype(bool)


# In[105]:


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# In[106]:


arr=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr.shape


# In[136]:


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16])


# In[137]:


newarr=arr.reshape(2,2,2,2)


# In[138]:


newarr


# In[147]:


newarr[0,0,1,0]


# In[152]:


newarr[0:2,0:1]


# In[153]:


for x in newarr:
    print(x)


# In[154]:


for x in arr:
    print(x)


# In[155]:


arr=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


# In[159]:


for x in arr:
    for y in x:
        z=y+y
        print(z)


# In[195]:


import numpy as np

arr1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]],[[13, 14, 15, 16], [17, 18, 19, 20],[21, 22, 23, 24]]])

arr2 = np.array([[[25, 26, 27, 28], [29, 30, 31, 32],[33, 34, 35, 36]],[[37, 38, 39, 40], [41, 42, 43, 48],[49, 50, 51, 52]]])
arr3 = np.array([[[53, 54, 55, 56], [57, 58, 59, 60],[61, 62, 63, 64]],[[65, 66, 67, 68], [69, 70, 71, 72],[73, 74, 75, 76]]])
for x in np.nditer(arr[:,0::2]):
  print(x)
print("--------")
for idx, x in np.ndenumerate(arr):
  print(idx, x)
print("--------")
arr=np.vstack((arr1,arr2,arr3))

print(arr)

print("--------")
for idx, x in np.ndenumerate(arr):
  print(idx, x)
print("--------")


# In[199]:


import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3, axis=1)
find=np.where(arr%2==0)

print(find)


# In[200]:


arr2d = np.zeros((10,10))


# In[201]:


arr2d


# In[202]:


arr_length = arr2d.shape[1]


# In[203]:


arr_length


# In[204]:


arr2d.shape[1]


# In[205]:


arr2d


# In[206]:


arr=np.arange(0,10)


# In[207]:


arr+arr


# In[208]:


arr*10*arr


# In[209]:


np.sqrt(arr)


# In[ ]:




