#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
</head>
<body>
    <h1>
        Signup
    </h1>
"""
page_footer = """
</body>
</html>
"""

form = """
        <form method="post">
            <label>Username
                <input type="text" name="username"/>
                </label>
                <br>
            <label>Password
                <input type="password" name="password"/>
            </label>
                <br>
            <label>Verify
                <input type="password" name="verify"/>
            </label>
                <br>
            <label>Email (Optional)
                <input type="text" name="email"/>
            </label>
                <br>
                <br>
            <div style="color:red">%(error)s</div>
                <br>
            <input type="submit"/>
        </form>
        """

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    username = USER_RE.match(username)
    return username

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    password = PASSWORD_RE.match(password)
    return password

#create a function that compares 2 strings
PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_verify(verify):
    verify = PASSWORD_RE.match(verify)
    return verify

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    email = EMAIL_RE.match(email)
    return email


class MainHandler(webapp2.RequestHandler):

    def write_form(self, error=""):
        self.response.write(page_header + form % {"error": error} + page_footer)

    def get(self):
        self.write_form()

    def post(self):
        username = valid_username(self.request.get("username"))
        password = valid_password(self.request.get("password"))
        verify = valid_verify(self.request.get("verify"))
        email = valid_email(self.request.get("email"))

        if email:
            email = valid_email(self.request.get("email"))

        if not username:
            self.write_form(error="That's not a valid username.")

        elif not password:
            self.write_form(error="That wasn't a valid password.")
#even when i type in the same string i get the error message. can't see what's wrong
        elif password != verify:
            self.write_form(error="Your passwords didn't match.")

        elif not email:
            self.write_form(error="That's not a valid email.")

        else:
            self.redirect("/welcome")


class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
        username = self.request.get("username")
        welcome_message = "Welcome " + username
        self.response.write(welcome_message)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)

], debug=True)
