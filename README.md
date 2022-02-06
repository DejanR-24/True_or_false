#True_or_false

This is an entertainment web app where author posts short story and the hidden answer to is it true story or false,
other users try to guess, after some time the author's answer is revealed and users get the points or not.

##Well it's far from done but it has functionalities- login,logout,posting stories, voting -true or false 

Setup:

The first thing to do is to clone the repository:
```
$ git clone https://github.com/DejanR-24/True_or_false.git
$ cd True_or_false
```
Create a virtual environment to install dependencies in and activate it:
```
$ python3.9 -m venv .venv
$ source .venv/bin/activate
(env)$ git checkout try
```
Then install the dependencies:
```
(env)$ pip3 install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by venv

Once pip has finished downloading the dependencies migrate db and load data in it:
```
(env)$python3.9 manage.py migrate
(env)$python3.9 manage.py loaddata db.json
(env)$ python3.9 manage.py runserver
```
```
login for admin is: dejan 
password:1234
```

##Or you can just go to them site
[True or false](trueorfalse.tk)
