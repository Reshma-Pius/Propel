#Q9). Write a python program to remove zeros from an IP address("216.08.094.196")

import re
ip = "216.08.094.196"
string=re.sub('\.[0]*','.',ip)
print(string)

