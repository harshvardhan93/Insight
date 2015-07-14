import os
import sys
import numpy as np

temp = os.path.dirname(os.getcwd())
input_file = os.path.join(temp,"Insight/tweet_input/tweets.txt")
output_file = os.path.join(temp,"Insight/tweet_output/ft2.txt")
count_unique=[]
median_=[]	
j=-1	

with open(input_file) as f:
		for line in f:
			line1=line.strip().split();
			j+=1;
			count_unique.append(len(set(line1)))
			if(j==0):
				median_.append(float(count_unique[j]))
			elif(j==1):
				median_.append(float(np.mean(count_unique)))
			else:
				if(j%2==0):
					median_.append(float(count_unique[j/2]));
				else:
					temp_avg=float((count_unique[j/2] + count_unique[(j/2) + 1])/2.0)
					median_.append(temp_avg)
f.close()
f1=open(output_file,"w")
for i in median_:
	f1.write(str(i))
	f1.write('\n')
f1.close()