#Interpret mood from socail media post
import sys, argparse
from textblob import TextBlob

# Read and parse command line arguments
parser = argparse.ArgumentParser(description="Basic Sentiment Analysis tool for Interpreting social media posts.")
parser.add_argument("-s", help= "read sentiment of given string (in quotes)")
parser.add_argument("-f",help = "read from text file")
parser.add_argument("-r",help = "return raw sentiment polarity instead of string", action ='store_true')
args = parser.parse_args()

# TextBlob displays sentiment in a range of -1 to 1, this converts that number to a string
def mood(x):
    if x>0 and x<.25 :
        return "slightly positive"
    elif x>.25 and x<.50 :
        return "fairly positive"
    elif x>.50 and x<.75 :
        return "very positive"
    elif x>.75 and x<=1 :
        return "extremely positive"
    if x>-.25 and x<0 :
        return "slightly negative"
    elif x>-.50 and x<-.25:
        return "fairly negative"
    elif x>-.75 and x<-.50 :
        return "very negative"
    elif x>=-1 and x<.75 :
        return "extremely negative"

# Read and interpret from posts file if -f selected
if args.f:
    file = open(args.f,"r")
    posts = file.readlines()
    # string 'latest' represents most recent facebook post and it's time of creation
    latest = posts[-1]
    # split latest into individaul post and time
    cur_post = TextBlob(latest.split("$$$")[0])
    cur_post_time = TextBlob(latest.split("$$$")[1])
    if args.r:
        print(cur_post.sentiment.polarity)
    else:
        print(mood(cur_post.sentiment.polarity))

# intrepret given string if -s selected
if args.s:
    given_string = TextBlob(args.s)
    if args.r:
        print(given_string.sentiment.polarity)
    else:
        print(mood(given_string.sentiment.polarity))
