#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


year = [2022,2021,2020,2019,2018,2017,2016,2015]
data = [[141701872, 91152649, 71326875, 64734872, 55884956, 42453378, 33091919, 28687457],
[30489152,3749637,3006439,5491447,695737,2661203,2880297,2207538],
[195547866,109335081,85419530,69075871,55555755,50328616,43296145,39463873],
[195304639,109085301,85166172,68821285,55298071,50070594,43064002,39227532],
[21.52,4.11,4.22,8.48,1.24,6.27,8.7,7.7],
[15.61,3.44,3.53,7.98,1.26,5.31,6.69,5.63],
[15.59,3.43,3.52,7.95,1.25,5.29,6.65,5.59],
[6.5,7.19,9.15,7.08,6.21,4.87,4.77,5.11],
[0.21,0.44,0.99,1.37,1.49,4.64,0.71,2.35],
[0,490,423,403,344,290,246,255],
[15.61,3.44,3.53,7.98,1.26,5.31,6.69,5.63],
[15.59,3.43,3.52,7.95,1.25,5.29,6.65,5.59],
[14.01,3.05,3.24,7.2,1.13,4.65,5.92,5.08],
[21.52,4.11,4.22,8.48,1.24,6.27,8.7,7.7],
[0.72,0.83,0.84,0.94,1.01,0.84,0.76,0.73],
[1.93,3.76,2.79,2.56,2.36,1.81,1.43,1.25],
[6.5,7.19,9.15,7.08,6.21,4.87,4.77,5.11],
[6.5,7.19,9.15,7.08,6.21,4.87,4.77,5.11],
[0.21,0.44,0.99,1.37,1.49,4.64,0.71,2.35],
[7652,7107,13626,2022,9177,11709,8,657]]


names = ["Turnover", "Profit (Loss) before Taxation", "Net Tangible Assets (Liab.)", "Shareholders Funds", "Profit Margin", "Return on Shareholders Funds", "Return on Capital Employed", "Liquidity Ratio (x)", "Gearing (%)", "Number of Employees", "Return on Shareholders Funds (%)", "Return on Capital Employed (%)", "Return on Total Assets(%)", "Profit Margin (%)", "Net Assets Turnover (x)", "Fixed Assets Turnover (x)", "Current Ratio (x)", "Liquidity ratio (x)", "Gearing (%)", "Profit Per Employee (unit)"]
i = 0
for i in range(0,len(names)):
    plt.scatter(year, data[i], label=names[i])
    plt.plot(year, data[i])
    #plt.title(names[i])
    
plt.legend()
plt.show()


# In[4]:



year = [2023, 2022, 2021, 2020, 2019, 2018]
year_short = [2022,2021,2020,2019,2018]
names = ['Inventory turnover', 'Average inventory processing period']

data_NV = [2.25,3.62,3.44,4.24,2.89,4.89] # inventory turnover



# Net fixed asset turnover Competitors
company_names = ['Nvidia','Advanced Micro Devices Inc.' , 'Intel Corp']
data = [[7.09,9.69,7.76,6.52,8.34,9.74],
    [15.60,23.41,15.23,13.46,18.61],
    [0.78,1.25,1.38,1.30,1.45]]

plt.title("Net Fixed Asset Turnover")
for i in range(len(company_names)):
    if i == 0:
        x = year
    else:
        x = year_short
    plt.scatter(x, data[i],label=company_names[i])
    plt.plot(x, data[i])

plt.legend(loc='upper right')
plt.show()
plt.savefig('net_fixed_asset.png')


# In[5]:


# The estimates revenue income from affordable GPU
year = [2017, 2018, 2019, 2020, 2021,2022, 2023]
users = [14.37, 18.58, 17.53, 18.33, 25.43, 29 , 32.2]

# technical survey NVIDIA share



# 10 series sales # 2016
total_perc = 

# 20 series sales # 2018

# 16 series sales # 2019

# 30 series sales # 2020
mid_end =  # 2060
high_end = # 2070, 2080 and Tis


# 40 series sales estimated # 2023



# In[19]:


data =  [34810776000.00,
         171850103500.00,
         348595415100.00]
x = [2017,2019,2021]
# 2023

coeff = np.polyfit(x,data,deg=1)
print(coeff)
c = coeff[1]
m = coeff[0]
y = m*np.array(temp)+c
temp = [2017,2019,2021,2023]
plt.plot(temp,y)
plt.scatter(x,data)
plt.show()

print(f'series 40 reveue estimate: {m*2023+c}')
ratio = data[0]/data[1]
print(f'ratio of low to high tier: {ratio}')
extra_rev = ratio*(m*2023+c)
print(f'estimated extra revenue due to affordable GPUs: {extra_rev}')
print(np.log(extra_rev))

# very overestimated numbers. Only use the relative ratio


# In[ ]:





# In[ ]:




