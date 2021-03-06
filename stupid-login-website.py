#!/usr/bin/env python3
"""
Create a website with a timing sidechannel.
"""
from flask import Flask
from flask import request
from time import sleep
import sys

app = Flask(__name__)


def password_ok(pwd):
    """
    The password check with a timing sidechannel.

    :param pwd: password to check
    :type pwd: str
    :returns: bool to indicate validity of password (True = valid)
    """
    password = "thisisstupid"

    if len(pwd) < len(password):
        # given password too short
        # to be correct
        return False

    sleep(0.05)  # delay of length comparision

    # check each character
    for i in range(0, len(password)):
        if password[i] != pwd[i]:
            # first characters which do not
            # match indicate the two given
            # strings are not equal
            return False
        sleep(0.1)
    # all characters matched
    return True


def success():
    return """
    <html>
    <head></head>
    <body bgcolor="#66c2a5">
      <br><br>
      <center>
        <h1>login sucessful</h1></center>
      </center>
    </body>
    </html>"""


def prompt():
    """
    Just the login prompt.
    """
    return """
    <html>
    <head></head>
    <body>
      <br><br>
      <center>please log in<br>
        <form action="/login" method="POST">
          <input type="password" name="password"
             placeholder="Enter your password here..." /><br>
          <input type="submit" value="log in">
        </form>
      </center>
    </body>
    </html>"""


@app.route("/", methods=['GET'])
def index():
    return prompt()


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if password_ok(request.form['password']):
            return success()
        else:
            return prompt()
    return prompt()


if __name__ == "__main__":
    app.run()
