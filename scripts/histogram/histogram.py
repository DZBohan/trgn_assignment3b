#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path= "/home/zhangboh/assignments/trgn_assignment3b/scripts/histogram/grades.test.csv"
df=pd.read_csv(path)
bins=np.linspace(min(df['Grades']),max(df['Grades']),4)
groupnames=['low','medium','high']
df['Grades']=pd.cut(df['Grades'],bins,labels=groupnames,include_lowest=True)
plt.hist(df['Grades'])
plt.title('Grades Level')
plt.xlabel('grades level')
plt.ylabel('students number')
plt.savefig("/home/zhangboh/public_html/expression_analysis_assignment3b_histogram.png")
