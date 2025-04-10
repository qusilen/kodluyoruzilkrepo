#!/usr/bin/env python
# coding: utf-8

# In[1]:


def flatten(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result


# In[3]:


l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]


# In[4]:


flatten(l)


# In[5]:


def reverse_nested(lst):
    result = []
    for element in lst[::-1]: 
        if isinstance(element, list):
            result.append(reverse_nested(element)) 
        else:
            result.append(element)
    return result


# In[6]:


reverse_nested(l)


# In[ ]:




