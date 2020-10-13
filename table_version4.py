import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
url = 'https://mcs.ciena.com/InetReports/AssemblyHistory/ResultsByAO.asp?SN=NNTMRT112ND8&PN=NTK540BC-820&R=008'
df = pd.read_html(url)
df=df[2]
df
data = df[[2,3,9,10]].copy()
data
entry=input("Enter part number")
filter_data=data[data[2].str.contains(entry)]
filter_data
start_date=input("Enter date in DD-Mon-YYYY (eg: 28-Aug-2020) format")
end_date=input("Enter date in DD-Mon-YYYY (eg: 28-Aug-2020) format")
filter_data=filter_data[filter_data[9].str.contains(start_date)]
filter_data
filter_data=filter_data[filter_data[10].str.contains(end_date)]
filter_data.columns =['Process Name', 'Outcome','Time Started','Time Ended'] 
filter_data
