#!/bin/bash

python ./src/parser.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt
