# Submission for Insight Data Engineering Coding Challenge

This code performs two tasks:
1) Count the occurences of every word in the file tweets.txt in the form of a key/value pair
2) Calculate the running median of the unique words in every tweet.

There is a shell script run.sh that takes an input file and an output file as command line arguments to the executable files parser.py and median.py
Eg:
python ./src/parser.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
Here tweets.txt and ft1.txt are the input and output files respectively and their paths are provided as arguments.

There is a sample input file called tweets.txt and the sample outputs are stored in ft1.txt & ft2.txt located in tweet_input and tweet_output folders respectively.

