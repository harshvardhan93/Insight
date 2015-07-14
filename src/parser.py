import os
import sys
import numpy as np
import collections
temp = os.path.dirname(os.getcwd())
input_files = os.path.join(temp,"Insight/tweet_input/tweets.txt")
output_file = os.path.join(temp,"Insight/tweet_output/ft1.txt")
# if(os.path.isfile(output_file) and os.path.getsize(output_file) > 0):
# 		f1=open(output_file,"r")
# 		position=f1.readline()
# 		f1.close();
# 	position=int(position)
# # def sentences(file_name):
# # 	with open(file_name) as f:
# # 		for line in f:
# # 			yield line.strip().split()
list1={}
with open(input_files) as f:
	for line in f:
		line=line.strip().split()
		for i in line:
			if i in list1:
				temp = int(list1[i])
				temp=temp+1;
				list1[i]=temp;
			else:
				list1[i]=1;
list1 = collections.OrderedDict(sorted(list1.items(), key=lambda t: t[0]))
f1=open(output_file,"w")
for word, count in list1.items():
	f1.write(word)
	f1.write(':\t\t\t')
	f1.write(str(count))
	f1.write('\n')
f1.close()

