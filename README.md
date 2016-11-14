# cliche_bot
Function that will rate how cliche your lyrics are

See accompanying page here: (coming soon)
 
### To Use
Run clichebot_prototype.ipynb from the top, replacing your lyrics of choice into the big block string at the bottom.
A higher score means more cliche.  

OR

Run cliche_bot.py from the command line. Takes one argument - either a string in quotes containing lyrics, or a path leading to a file containing lyrics.

&gt;90 = super duper cliche  
&gt;70 = pretty average song  
&gt;60 = interesting lyrics  
&gt;50 = not cliche; similar to natural language  
&gt;35 = very unique lyrics  
&lt;35 = is this even a song?   

### What else is going on in this repo?
cliche_words.tsv is a table of word stems and some other info, including my *proprietary* cliche score. The cliche-ness of a set of lyrics is the weighted average of its elements.

make_cliche_scores.ipynb is also in there, but to run it you're going to have to get a hold of these datasets:  
Top 5000 Most Used English Words: http://www.wordfrequency.info/free.asp  
The MusiXMatch Lyrics dataset: http://labrosa.ee.columbia.edu/millionsong/musixmatch  

Let me know if you have any other ideas how to measure cliche! It must be identified and eliminated wherever found.
