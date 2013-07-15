This is a python app to monitor some web page containing static thats not supposed to change.
To use this,  run it with the name of the control page as the first parameter and the second parameter 
should be the test page thats being evaluated. At the moment only  <li>, <title>, <div>, <link> and <span> 
are checked by default, butits trivial to add check for more html tags.

Sample session

$ python bs.py  --test http://www.example.com   --control ok.html  
$ 

No news is good news, if the page had an alien edit (addition or removal,)



