#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

t = urllib2.urlopen('http://www.gmasson.com.br/').read()

# TAG
tags = t.split('<p')[1:]
tags = [ tag.split('</p>')[0] for tag in tags ]

for i in tags:
    print i
