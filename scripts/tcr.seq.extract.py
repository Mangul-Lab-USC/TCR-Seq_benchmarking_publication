import csv
import argparse
from math import log as ln
import sys

#============================
ap = argparse.ArgumentParser()
ap.add_argument('input', help='<TCR_seq_file.tsv> file')
ap.add_argument('out_prefix', help='name of outfile and save location')
args = ap.parse_args()

set_cdr3=set()
dict={}

#get all CDR3s
file=open(args.input)
reader=csv.reader(file,delimiter="\t")
next(reader,None)
for line in reader:
    cdr3=line[3]
    if cdr3[0] == "C" and cdr3[len(cdr3) - 1] == "F":
        set_cdr3.add(cdr3)
file.close()

for c in set_cdr3:
    dict[c]=0

#get number of reads
file=open(args.input)
reader=csv.reader(file,delimiter="\t")
next(reader,None)
for line in reader:
    nReads=int(line[2])
    cdr3=line[3]
    if cdr3[0]=="C" and cdr3[len(cdr3)-1]=="F":
        dict[cdr3]+=nReads
    else:
        print(cdr3)

file.close()

fileOut=open(args.out_prefix,"w")
fileOut.write("Sample,CDR3,nReads")
fileOut.write("\n")

sample_name = args.input.split("/")[-1].split(".")[0]

print(sample_name)

for key, value in dict.items():
    fileOut.write(sample_name+","+key+","+str(value))
    fileOut.write("\n")
fileOut.close()