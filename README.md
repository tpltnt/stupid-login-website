# stupid-login-website
"stupid login website" is, well, a stupid login website. It is a [flask](http://flask.pocoo.org/)
based website with an intentional timing side-channel. The purpose is to demonstrate this attack
vector (along with credential sniffing). It is also a fine beginner-level challenge for a CTF.

# setup flask
* install pyvenv to leverage Python virtual environments

  * setup an environment: ```pyvenv foo```
  * activate the environment: ```source foo/bin/activate```

* install flask: ```pip3 install flask```

# run the website
* *either*: ```python3 stupid-login-website.py```
* *or*: ```chmod +x stupid-login-website.py && ./stupid-login-website.py```

# resources
* [flask](http://flask.pocoo.org/)
* [wikipedia: timing attack](https://en.wikipedia.org/wiki/Timing_attack)
