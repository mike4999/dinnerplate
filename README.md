# dinnerplate 
## Description
This is a python app to monitor some web page containing static content thats not supposed to change.
To use this,  run it with the name of the control page as the first parameter and the second parameter 
should be the test page thats being evaluated. At the moment only ``` <li>, <title>, <div>, <link> and <span>``` 
are checked by default, but its trivial to add check for more html tags.

## Docs
Sample session

```
$ python bs.py  --test http://www.example.com   --control ok.html --notify myemail@spam.com 
$ 
```

No news is good news, if the page had an alien edit (addition or removal,)

```
$ python bs.py  --test http://www.example.com   --control ok.html  --notify myemail@spam.com
 here lies the culprit <li class="top"><a href="#Top" title="Back to Top">Top</a></li> thats been added
$
```

The application goes through the page and identifies all the elements that have beed added /removed and
prints(+/emails) out what it finds.

## Automating
### Requirements:
To run this create a python file names ```defaults.py``` and  in it place the default values that you use
in this format
```
myurl = 'http://example.com'
myokfile = 'ok.html'
myemail = ['blah@blah.com','blah2@blah.com']
```
##NB:
this is a blocking app, it will hold the terminal till you hit Ctrl-C, <del> later i will turn it into an
init.d service.</del>
The app can be configured to be an init.d service on systems with <del> ```lsb``` not </del> ```rh-lsb```, all that should be done is:

1.	edit the path to the `dinnerplate.py``` script  in the shell script named ```dinnerplated```  and
2.	alter the path to your python executable in ```dinnerplate.py```, 
3.	copy the dinnerplated file to (typically) ```/etc/init.d/``` you can then start the service
	with the command ``` service dinnerplated start``` or the other usual options.

##Convenience
You can create a control file using the hotpot.py script: 

```
$ python hotpot.py --control='http://example.com' >> ok.html
```

### More to come,
i hope to add more functionality, docs and clean up the code
Cheers
mike
