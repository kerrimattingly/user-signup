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
                <input type="text" name="username" value="%(username)s"/>
                </label><span style="color:red">%(error_username)s</span>
                <br>
            <label>Password
                <input type="password" name="password"/>
            </label><span style="color:red">%(error_password)s</span>
                <br>
            <label>Verify
                <input type="password" name="verify"/>
            </label><span style="color:red">%(error_verify)s</span>
                <br>
            <label>Email (Optional)
                <input type="text" name="email" value="%(email)s"/>
            </label><span style="color:red">%(error_email)s</span>
                <br>
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

    def write_form(self, error_username="", username="", error_password="", error_verify="", email="", error_email=""):
        self.response.write(page_header + form % {"error_username": error_username, "username": username, "error_password": error_password, "error_verify": error_verify, "email": email, "error_email": error_email} + page_footer)

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        have_error = False
        error_username=""
        error_password=""
        error_verify=""
        error_email=""
        if not valid_username(username):
            #self.write_form(error="That's not a valid username.", username=username)
            have_error = True
            error_username="That's not a valid username."

        if not valid_password(password):
            #self.write_form(error="That wasn't a valid password.")

            have_error = True
            error_password="That wasn't a valid password."
#even when i type in the same string i get the error message. can't see what's wrong
        if password != verify:
            #self.write_form(error="Your passwords didn't match.")
            have_error = True
            error_verify="Your passwords didn't match."

        if email:
            if not valid_email(email):
            #self.write_form(error="That's not a valid email.")
                have_error = True
                error_email="That's not a valid email."

        if have_error:
            self.write_form(username=username, error_username=error_username, error_password=error_password, error_verify=error_verify, error_email= error_email)

        else:
            self.redirect("/welcome?username="+ username)


class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
        welcome_username = self.request.get("username")
        welcome_message = "Welcome " + welcome_username
        self.response.write(welcome_message)




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)

], debug=True)
