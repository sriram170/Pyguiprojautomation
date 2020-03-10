
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
data_file=pd.read_csv("C:\\Users\\1416363\\Desktop\\pypandas.csv")
print (data_file[0:7000])



# In[ ]:

time=data_file('Host Name')


# In[ ]:

# no of col required

noofcol=data_file.ix[:,'Host Name':'Asset Type']
print(noofcol[0:6])


# In[ ]:

noofcol=data_file.ix[;,'Host Name':'Asset Type']
while data_file['Asset type']= 'Workstation'


# In[ ]:

data_file = {'Host Name': ['AOD75SP5Y1']}
data_file_filtered=data_file.query('Month==11')



# In[ ]:

# New Program

import pandas as pd
import numpy as nmp

fd=pd.read_csv("C:\\Users\\1416363\\Desktop\\pypandas.csv")
print(fd[0:20])


# In[ ]:

# find the record
fd.set_index("Host Name", inplace = True)
fd
fd.iloc["NGD9VHKB5J"]


# In[ ]:

fd.iloc[:,[0,2]]


# In[ ]:

fd.Host Name=="SGTMP1E2TBM"


# In[ ]:

fd.HostName=="SGTMP1E2TBM"


# In[ ]:

ftr=fd.Host Name=="SGTMP1E2TBM"


# In[ ]:

ftr = fd.Host Name=="SGTMP1E2TBM"


# In[ ]:

ftr = fd.Host Name == "SGTMP1E2TBM"


# In[ ]:

ftr = fd.Host Name=="SGTMP1E2TBM"
fd[ftr]


# In[ ]:

#replace the header with _ in the header to query easily

import pandas as pd
import numpy as nmp
import tkinter as tk

fd=pd.read_csv("C:\\Users\\1416363\\Desktop\\pypandas.csv")


fd.columns =[column.replace(" ", "_") for column in fd.columns]
#fd.PSID = fd.PSID.astype(int64)

print(fd.dtypes)

# if there is NA in coliumn then ti will not convert to number ,below line will replace NA to 0 and convert it.

fd['PSID'] = fd['PSID'].fillna(0).astype(nmp.int64)

#fd.PSID = fd.PSID.astype(nmp.int64)

print(fd.dtypes)


#the below method is used to filter the data

ftr = fd.Model == "Optiplex 7010"
fd[ftr]
fd[ftr].to_excel("C:\\Users\\1416363\\Desktop\\Compan.xlsx")
print ("completed")
print(fd)






# In[2]:

import tkinter as tk


# In[ ]:



