# dinnerplate 
## Description
This is a python app to monitor some web page containing static thats not supposed to change.
To use this,  run it with the name of the control page as the first parameter and the second parameter 
should be the test page thats being evaluated. At the moment only  <li>, <title>, <div>, <link> and <span> 
are checked by default, butits trivial to add check for more html tags.

## Docs
Sample session

```
$ python bs.py  --test http://www.example.com   --control ok.html --notify myemail@spam.com 
$ 
```

No news is good news, if the page had an alien edit (addition or removal,)

```
$ python bs.py  --test http://www.uoeld.ac.ke   --control ok.html  --notify myemail@spam.com
 here lies the culprit <li class="top"><a href="#Top" title="Back to Top">Top</a></li> thats been added
$
```

The application goes through the page and identifies all the elements that have beed added /removed and
prints(+/emails) out what it finds.

### More to come,
i hope to add more functionality, docs and clean up the code
Cheers
mike
