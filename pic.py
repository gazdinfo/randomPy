#!/usr/bin/python
# import sys;
from randgen import *;

values['max'] = 2;
values['iv'] = 2;



# sorok es oszlopok
columns = 70;
rows = 23;

for i in range(0, rows):
  row = '';
  for j in range(0, columns):
    if adConRandom() == 0:
      row += ' ';
    else:
      row += '*';

  print row;    
