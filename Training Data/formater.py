#!/usr/bin/env python
# -*- coding: utf-8 -*-
aa = input()
file = open(aa + ".txt", "r", encoding="latin-1")
text = file.read()
text = text.split("\n\n")
print(len(text))
for i in text:
    print (i + "\n")
file.close()
