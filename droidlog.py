#!/usr/bin/python

###
#
# Droid Log v1.0
# http://www.joelambert.co.uk
# 
# Copyright 2012, Joe Lambert.
# Free to use under the MIT license.
# http://joelambert.mit-license.org/
#
###

import os, re, StringIO

# Format and indent the LOG/ERROR message
def format_type(t):
	if t == "E":
		return "\033[0;31m" + "ERROR " + "\033[0m"
	else:
		return "\033[0;33m" + "LOG   " + "\033[0m"

# Get the console output from adb
input = os.popen("adb logcat")

# We're only interested in the output from PhoneGap/Web
pgfilter = re.compile("^(I|E)\/Web Console\([^\)]+\): (.*?) at (.*)$")

while True:
    try:
        line = input.readline()
    except KeyboardInterrupt:
        break
	
    match = pgfilter.match(line)

	# Ignore lines we don't care about
    if not match is None:
		linebuf = StringIO.StringIO()
		
		# Get the component parts we're interested in
		msgtype = match.group(1)
		msg = match.group(2)
		fileref = match.group(3).replace('file:///android_asset/www/', '')
		
		# Format/colour the output
		linebuf.write(format_type(msgtype))
		linebuf.write(msg+" ")
		linebuf.write("\033[38;5;242m" + fileref + "\033[0m")
		line = linebuf.getvalue()
		
		print line

    if len(line) == 0: break