# To calculate the number of occurances of a word in a file tweets.txt
import sys
import collections

input_files=str(sys.argv[1])
output_file=str(sys.argv[2])

# list1 is the dictionary that is created and it stores the count of every word in the form of a key and value
list1={}
with open(input_files) as f:
	for line in f:
		line=line.strip().split() # we split the sentence such that whenever we come across a whitespace we store a new word
		for i in line:
			if i in list1: # to increment the value of a key in the dictionary 
				temp = int(list1[i])
				temp=temp+1;
				list1[i]=temp;
			else: # initial value of a key 
				list1[i]=1;
list1 = collections.OrderedDict(sorted(list1.items(), key=lambda t: t[0])) # sorting the dictionary as per ascii values
f1=open(output_file,"w") # Writing results to the output file 
for word, count in list1.items():
	f1.write('{0:30} {1:20} \n'.format(word,count))

f1.close()

