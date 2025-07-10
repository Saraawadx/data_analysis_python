#!/usr/bin/env python
# coding: utf-8

# # BMI Metric Calculator

# In[1]:


#BMI = 20.1 kg/m2


# In[15]:


name = input("What's your name?")

height = int(input("What's your height? (in CM) "))

weight = int(input("What's your weight? (in KG) "))

BMI = weight / ((height / 100) ** 2)

print(BMI)

if BMI > 0:
    if BMI < 16:
        print(name+', you are severly thin!')
    elif BMI < 17:
        print(name+', you are moderatly thin!')
    elif BMI < 18.5:
        print(name+', you are mildly thin!')
    elif BMI < 25:
        print(name+', you are within the healthy range!')
    elif BMI < 30:
        print(name+', you are overweight!')
    elif BMI >= 30:
        print(name+', you are obese!')
else:
    print('Enter valid inputs')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




