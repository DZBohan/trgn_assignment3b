#!/usr/bin/python3
# import sys
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# path= sys.argv[1]
# df=pd.read_csv(path)
# bins=np.linspace(min(df['Grades']),max(df['Grades']),4)
# groupnames=['low','medium','high']
# df['Grades']=pd.cut(df['Grades'],bins,labels=groupnames,include_lowest=True)
# plt.hist(df['Grades'])
# plt.title('Grades Level')
# plt.xlabel('grades level')
# plt.ylabel('students number')
# plt.savefig("/home/zhangboh/public_html/expression_analysis_assignment3b_histogram.png")

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-f',type=int,default=1,choices=range(10),required=False)
parser.add_argument('path',type=str)
csv_file = pd.read_csv(parser.parse_args().path)
column_index = csv_file.columns[parser.parse_args().f]
plt.hist(csv_file[column_index])
plt.title('Histogram of ' + column_index + ' Grade Distribution')
plt.xlabel('Grades of Students')
plt.ylabel('Number of Students')
plt.savefig("/home/zhangboh/public_html/expression_analysis_assignment3b_histogram.png")
plt.savefig('./' + column_index + '_analysis.png')
