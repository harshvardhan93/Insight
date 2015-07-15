# To calculate the running median of the number of unique words in a tweet
import sys
import numpy as np

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])
count_unique=[] # To store the number of unique words 
median_=[] # To store the median of the unique words	
j=-1	# To keep a count of the index of the lists
with open(input_file) as f:
		for line in f:
			line1=line.strip().split();
			j+=1;
			count_unique.append(len(set(line1))) # count the number of unique words 
			count_unique.sort() # sort the count list to calculate the median
			if(j==0): # calculate the median
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
f1=open(output_file,"w") # write the data to the output file
for i in median_:
	f1.write(str(i))
	f1.write('\n')
f1.close()