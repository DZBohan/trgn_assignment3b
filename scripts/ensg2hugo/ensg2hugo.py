#In[]
#!/usr/bin/python3
import sys
import re
import pandas as pd
ens2gene={}

with open('gencode.v38.basic.annotation.gtf', 'r') as file:
    for line in file:
         matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
         if matches:
             ens2gene[matches[0][0].split('.')[0]]=matches[0][1]

csv_filename = sys.argv[1]
csv = pd.read_csv(csv_filename,index_col=0)
def exchange_gene_name (id):
    id_simple=id.split('.')[0]
    if id_simple in ens2gene.keys():
        return ens2gene[id_simple]
    else :
        return id

csv['gene_id'] = csv['gene_id'].map(lambda x:exchange_gene_name(x))

csv.to_csv('./expression_analysis.hugo.csv')
csv.to_csv('./expression_analysis.hugo.tsv',sep='\t')

