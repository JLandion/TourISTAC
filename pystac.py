# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:03:14 2020

@author: juan luis
"""
import requests
import os

url = 'http://www.gobiernodecanarias.org/istac/galerias/documentos/C00028A/egt-metodologia-2018-microdatos-2020q1.html'

# allow redirection with allow_redirects=True
EGT = requests.get(url,allow_redirects=True)

"""
 we get the new url that
 the redirect returns
 split("/") we create an array of the url separated by the character /
 y con [-1] we get the last element of the array 

"""
name = EGT.url.split("/")[-1]
# obtain the path
path = os.path.join(os.getcwd(),name)

# open file in wb = write/binary mode and + create if does not exists
with open(path,"wb+") as f:
    # we write the returned content inside the file
    f.write(EGT.content)

    
# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "gasto-turistico-2020Q1.zip"
  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!') 

# Introduce data in pandas
import pandas as pd
pd.set_option('display.max_rows',500)
EGT = pd.read_csv('GASTO_TURISTICO_2020Q1.csv',sep = ';')

#checking if dada was correctly imported
EGT.head(10)
list(EGT)
EGT.dtypes

# Finding duplicated rows
duplicate_rows_EGT = EGT[EGT.duplicated()]
print('number of duplicate rows: ', duplicate_rows_EGT.shape)

# Finding null rows
print(EGT.isnull().sum())

#Finding outliers in variable NOCHES
import seaborn as sns
sns.boxplot(x=EGT['NOCHES'])

# Plotting a Histogram of tourists by country of residence
import matplotlib.pyplot as plt
EGT.PAIS_RESIDENCIA.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Number of tourist by country of residence')
plt.ylabel('Number of tourists')
plt.xlabel('Country');

# Finding the relations between the variables. Too much variables for visualitation
plt.figure(figsize=(20,10))
c= EGT.corr()
sns.heatmap(c,cmap='BrBG',annot=True)
c









