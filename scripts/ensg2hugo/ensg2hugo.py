#In[]
#!/usr/bin/python3
# import sys
# import re
# import pandas as pd
# ens2gene={}

# with open('gencode.v38.basic.annotation.gtf', 'r') as file:
#     for line in file:
#          matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
#          if matches:
#              ens2gene[matches[0][0].split('.')[0]]=matches[0][1]

# csv_filename = sys.argv[1]
# csv = pd.read_csv(csv_filename,index_col=0)
# def exchange_gene_name (id):
#     id_simple=id.split('.')[0]
#     if id_simple in ens2gene.keys():
#         return ens2gene[id_simple]
#     else :
#         return id

# csv['gene_id'] = csv['gene_id'].map(lambda x:exchange_gene_name(x))

# csv.to_csv('./expression_analysis.hugo.csv')
# csv.to_csv('./expression_analysis.hugo.tsv',sep='\t')

import re
import pandas as pd
import argparse
ens2gene={}

with open('gencode.v38.basic.annotation.gtf', 'r') as file:
    for line in file:
         matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
         if matches:
             ens2gene[matches[0][0].split('.')[0]]=matches[0][1]

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-f',type=int,default=1,choices=range(10),required=False)
parser.add_argument('path',type=str)
csv = pd.read_csv(parser.parse_args().path)
column_number = parser.parse_args().f - 1
column_index = csv.columns[column_number]
def exchange_gene_name (id):
    id_simple=id.split('.')[0]
    if id_simple in ens2gene.keys():
        return ens2gene[id_simple]
    else :
        return id

csv['gene_id'] = csv['gene_id'].map(lambda x:exchange_gene_name(x))

csv[column_index].to_csv('./expression_analysis.hugo.csv')
csv[column_index].to_csv('./expression_analysis.hugo.tsv',sep='\t')
