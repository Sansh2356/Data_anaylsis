#!/usr/bin/env python
# coding: utf-8

# # assignment1
# 
# Use the "Run" button to execute the code.

# In[1]:


name = "ansh"


# In[2]:


age=18


# In[7]:


has_android_phone='false'


# In[8]:


print(has_android_phone)


# In[9]:


name,age,has_android_phone


# In[10]:


person = {'name':'ansh','age':'18','has_android_phone':'false'}


# In[11]:


help(enumerate)


# In[12]:


for i in range(1,6):
    print(i)


# In[22]:


a = 5
name = "hello my name is ansh and i am {} years old"
print(name.format(a))


# In[23]:


def say_hello():
    print("how are you")
    print("myself raju")
    
say_hello()    
    


# In[24]:


import numpy as np


# In[26]:


help(list)


# In[29]:


my_list = [1,2,23,53]
sum=0
for i in range(0,len(my_list)):
    sum = sum+my_list[i]
print(sum)


# In[30]:


import numpy as np


# In[35]:


arr1=np.array(my_list)
arr2=np.array([5,6,7,8])


# In[40]:


arr3 = arr1*arr2
for x in range(0,len(arr3)):
    print(arr3[x])


# In[33]:


import jovian


# In[32]:


jovian.commit()


# In[45]:


import urllib.request
urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt'
)


# In[2]:


import numpy as np


# In[3]:


help(np.sum)


# In[4]:


help(np.concatenate)


# In[18]:


arr3 = np.array([[1,2,3],
                [4,5,6],
               [7,8,9]])
arr4 = np.array([[10,11,12],
               [13,14,15],
               [16,17,18]])
arr5 = arr3*arr4
arr6 = arr3+arr4
arr5,arr6


# In[26]:


arr7 = [[1,2],
       [1]]
arr8 = [[1,2,3],
        [4,5,6],
       [7,8,9]]
arr9 = arr7*arr8
#broadcasting associates with only those matrices which will make out to become of the same order as 
#of the other matrix.
arr9


# In[28]:


arr10 = [[1,2,3],[4,5,6],[7,8,9]]
arr11 = [[10,11,12,13],[14,15,16,17],[18,19,20]]
arr12 =  arr10*arr11
arr12


# In[1]:


import numpy as np


# In[7]:


arr1 = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
arr1.shape


# In[8]:


import pandas as pd


# In[9]:


from urllib.request import urlretrieve


# In[10]:


italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
urlretrieve(italy_covid_url,'italy-covid-daywise.csv')


# In[11]:


covid_csv=pd.read_csv('italy-covid-daywise.csv')


# In[12]:


covid_csv


# In[18]:


type(covid_csv)


# In[13]:


#dataframe is the type of storage/dataframe is the object of the subclass which stores the csv information from the file.
covid_csv


# In[33]:


#the memory inside the dataframe data structure is stored in the form of array/list of dict
#covid_csv.describe()
covid_csv.at[240,'new_cases']
#accessing a particular element in series 


# In[34]:


covid_csv.loc[246]
#gives us a particular row as output
covid_csv2=covid_csv.copy()
#creates a copy of the same dataset


# In[39]:


covid_csv.head(4)
#accesing first few rows
covid_csv.tail(4)
#accesing the last few rows
covid_csv.sample(10)
#sample gives us random sample of few rows as per the randomly


# In[47]:


covid_new_cases = covid_csv['new_cases']
new_cases_sum = covid_new_cases.sum()
new_cases_sum
#we can directly perform arithmetic operations on given set of data
cases = covid_csv[covid_csv.new_cases > 1000]
#the above is an example of a query regarding all the rows in which the datapoin of new_cases is strictly greater than 1000


# In[78]:


covid_csv['new_cases']/covid_csv['new_deaths']
covid_csv['ratio'] = covid_csv['new_cases']/covid_csv['new_deaths']
covid_csv
covid_csv.drop(columns=['ratio'],inplace = True)
#the above query is used to drop an existing column and the use of inplace is 
covid_csv


# In[100]:


covid_b = covid_csv[covid_csv.new_cases < 0]
#covid_b
covid_csv.sort_values('new_cases',ascending = False).head(10)
#the above command is used to sort the value according to a given column in increasing or decreasing order.


# In[105]:


covid_csv['date']
type(covid_csv['date'])
covid_csv['date'] = pd.to_datetime(covid_csv.date)
type(covid_csv['date'])


# In[170]:


covid_csv['year'] = pd.DatetimeIndex(covid_csv.date).year
covid_csv['month'] = pd.DatetimeIndex(covid_csv.date).month
covid_csv['day'] = pd.DatetimeIndex(covid_csv.date).day
covid_csv['weekday'] = pd.DatetimeIndex(covid_csv.date).weekday
covid_csv.month
list= []
for i in range(1,10):
    l=covid_csv[covid_csv.month == i].new_cases.sum()
    list.append(l)
count = 1
for u in range(len(list)):
    print(count)
    print(list[u])
    count = count+1
   
    
#The above is required to view month-wise,day-wis or year-wise data-points for better implementation of graphs and data can be ana
#lysed further more accurately and with greater extent of accuracy.


# In[174]:


covid_c = covid_csv[covid_csv.month == 5]
covid_c
#covid_c gives us all the values of a particular month ie. march(5)
total_case_sum_march=int(covid_c.new_cases.sum())
total_case_sum_march
total_deaths_march = int(covid_c.new_deaths.sum())
total_new_test_march = int(covid_c.new_tests.sum())
#covid_c.sum()
covid_csv.new_cases.mean()
covid_csv[covid_csv.weekday == 6].new_cases.mean()
#The above gives us the values of mean of a particular weekday ie.sunday
covid_x = covid_csv.groupby('month').sum()
covid_x
#group_by is used to group_together the values of a particular data point that we require to aggregate together and the analyse


# In[175]:





# In[176]:


urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')
location_csv = pd.read_csv('locations.csv')


# In[182]:


location_csv[location_csv.location == 'Italy'].location


# In[184]:


covid_csv['location'] = location_csv[location_csv.location == 'Italy'].location


# In[185]:


covid_csv['location'] = 'Italy'


# In[186]:


covid_csv
#cumsum is used to get the cumaltive sum of a particular data till that particular date in that particular csv file


# In[187]:


merge_file  = covid_csv.merge(location_csv,on="location")


# In[188]:


merge_file
#merging of file is required to merge data points of 2 diffrent or more than 2 csv files


# In[193]:


merge_file2 = merge_file[['date','new_cases','new_deaths','new_tests']]
merge_file2


# In[194]:


#to_csv function is used to write the data back into the file from which data was gathered ie. the inital csv formatted file
merge_file2.new_cases.plot();


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
#matplotlib is used to plot the datapoints in accordance with the given plots
#inline function is used to represent the plotted graph on the same block instead of inline function
#plt.plot is used to represent a line chart
my_list = [211.12,2,3,4.234,5.1235,6.799,7.213]
#pltx_label and plty_label for labelling the quantities taken on the respective x and y axis
#plt.legend it will give labels for multiple lines which are plotted simultaneously in the chart
#plt.title is used to give overall name to the class.
plt.plot(my_list);


# In[ ]:




