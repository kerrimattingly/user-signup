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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
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
user_form = """
            <form action="/AddUser" method=post>
                <label>Username</label>
                <input type="text" name="username"/><br>
                <br><label>Password</label>
                <input type="password" name="password"/><br>
                <br><label>Verify</label>
                <input type="password" name="verify"/><br>
                <br><label>Email (Optional)</label>
                <input type="text" name="email"/><br>
                <br><input type="submit"/>
                </form>
                """

content = page_header + user_form + page_footer

class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(content)

class AddUser(webapp2.RequestHandler):

    def post(self):

        username = self.request.get("username")
        username = cgi.escape(username)
        password = self.request.get("password")
        password = cgi.escape(password)
        verify = self.request.get("verify")
        verify = cgi.escape(verify)
        email = self.request.get("email")
        email = cgi.escape(email)

        welcome_message = '<p>Welcome ' + username + '</p>'
        self.response.write(welcome_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/AddUser', AddUser)
], debug=True)
