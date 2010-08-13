#!/usr/bin/python
import sys;
from randgen import *;
  
if '-h' in sys.argv:
  print 'Veletlenszam generalasa Additiv Congruential Method hasznalataval.';
  print 'Hasznalat: ./linear.py [N min max]';
  sys.exit();

try:
  N = int(sys.argv[1]);
except IndexError:
  N = 1;
except ValueError:
  print 'Error: argumentumnak egy szamot kell megadni';
  sys.exit()

try:
  values['min'] = int(sys.argv[2]);
except IndexError:
  pass;
except ValueError:
  print 'Error: argumentumnak egy szamot kell megadni';
  sys.exit()

try:
  values['max'] = int(sys.argv[3]);
except IndexError:
  pass;
except ValueError:
  print 'Error: argumentumnak egy szamot kell megadni';
  sys.exit()

values['iv'] = values['max'] - values['min'];

for i in range(0, N):
  print linConRandom();
