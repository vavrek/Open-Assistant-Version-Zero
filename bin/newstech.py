#!/usr/bin/env python

import subprocess
import feedparser

rss = feedparser.parse('http://www.reddit.com/r/technology/.rss')

print(rss['feed']['title'])

for post in rss.entries:
    subprocess.call("echo \"" + post.title + "\n\" | tee /dev/tty | $VOICE", shell=True)
