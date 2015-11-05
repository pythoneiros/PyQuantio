#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

t = urllib2.urlopen('http://www.tableless.com.br/').read()

# TAG para colher as informações
tags = t.split('<a')[1:]
tags = [ tag.split('</a>')[0] for tag in tags ]

for i in tags:
    print i
