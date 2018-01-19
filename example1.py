#!/usr/bin/env python
import sys

arg1 = sys.argv[1]  
with open('example1-output.txt', 'a') as f:
    f.write("hello!! {}. this is python script running on day 0".format(arg1))
