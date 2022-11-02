#!/usr/bin/env python

import cgi
import cgitb
#from __future__ import print_function

cgitb.enable()
form = cgi.FieldStorage() # instantiate only once!

# getlist() returns a list containing the
# values of the fields with the given name
screens = form.getlist('screen')
width = form.getfirst('width')
height = form.getfirst('height')

print "Content-Type: text/html\n"
print '<html><body bgcolor="#000000">'
for screen in screens:
  print '<img src="http://%s" width="%s" height="%s" border="0">' % (screen, width, height),

print '</body></html>'
