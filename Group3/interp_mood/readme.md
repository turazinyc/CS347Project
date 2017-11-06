# Basic Python Sentiment Analysis 

Ok I used python textblob to make this simple sentiment analysis tool.

### How to use:
In terminal: `python interp_mood.py -s "string to be interpreted"` or `-f file_to_read_from.txt`

You can also see the help page with `python interp_mood.py -h`

### Text File Format
Right now I have the text file to be set up like so:
~~~
taco taco taco taco $$$ 66/66/6666
this is another post $$$ march 3 1999
~~~
basically each line is a post and the body of the post is the text leading up to the `$$$` delimeter. I did this so we coud store other information about the post like the date it was posted or even pre-existing mood data. For example:
~~~
gosh facebook is cool $$$ 10/10/2017 $$$ Positive
~~~
Everything after the first set of `$$$` is **Ignored** by interp_mood.py

For running this code you will need to install python textblob.

Heres How:

~~~
$ pip install -U textblob
$ python -m textblob.download_corpora
~~~
